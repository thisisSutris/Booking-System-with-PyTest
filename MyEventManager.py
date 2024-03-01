# Make sure you are logged into your Monash student account.
# Go to: https://developers.google.com/calendar/quickstart/python
# Click on "Enable the Google Calendar API"
# Configure your OAuth client - select "Desktop app", then proceed
# Click on "Download Client Configuration" to obtain a credential.json file
# Do not share your credential.json file with anybody else, and do not commit it to your A2 git repository.
# When app is run for the first time, you will need to sign in using your Monash student account.
# Allow the "View your calendars" permission request.
# can send calendar event invitation to a student using the student.monash.edu email.
# The app doesn't support sending events to non student or private emails such as outlook, gmail etc
# students must have their own api key
# no test cases for authentication, but authentication may required for running the app very first time.
# http://googleapis.github.io/google-api-python-client/docs/dyn/calendar_v3.html


# Code adapted from https://developers.google.com/calendar/quickstart/python
from __future__ import print_function
from datetime import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

from Event import Event
from Time import Time
from Location import Location
from Attendee import Attendee
from Organiser import Organiser
from Reminder import Reminder

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_calendar_api():
    """
    Get an object which allows you to consume the Google Calendar API.
    You do not need to worry about what this function exactly does, nor create test cases for it.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)


def get_upcoming_events(api, starting_time, number_of_events):
    """
    Shows basic usage of the Google Calendar API.
    Prints the start and name of the next n events on the user's calendar.
    """
    if (number_of_events <= 0):
        raise ValueError("Number of events must be at least 1.")

    events_result = api.events().list(calendarId='primary', timeMin=starting_time,
                                      maxResults=number_of_events, singleEvents=True,
                                      orderBy='startTime').execute()
    return events_result.get('items', [])


def get_events(api) -> list:
    events_api = api.events().list(calendarId='primary').execute()
    events_api = events_api.get('items', [])

    # Convert the events to Events
    events = []
    for i in range(len(events_api)):
        events.append(event_to_Event(events_api[i]))
    
    return events


def create_location_address(street_number: str, street_name: str, suburb: str, state: str, postcode: str, country: str) -> Location:
    # Preconditions
    if type(street_number) != str:
        raise ValueError("create_location_address() street_number expected type str")
    if type(street_name) != str:
        raise ValueError("create_location_address() street_name expected type str")
    if type(suburb) != str:
        raise ValueError("create_location_address() suburb expected type str")
    if type(state) != str:
        raise ValueError("create_location_address() state expected type str")
    if type(postcode) != str:
        raise ValueError("create_location_address() postcode expected type str")
    if type(country) != str:
        raise ValueError("create_location_address() country expected type str")

    # Create Location and initialise as an address
    location = Location()
    location.init_address(street_number, street_name, suburb, state, postcode, country)

    return location


def create_location_link(link: str) -> Location:
    # Preconditions
    if type(link) != str:
        raise ValueError("create_location_link() link expected type str")

    # Create Location and initialise as a link
    location = Location()
    location.init_link(link)

    return location


def create_event(api, events: list, starting_time: Time, ending_time: Time, attendees: list, summary: str, description: str, location: Location, reminders: list) -> Event:
    # Preconditions
    # Type preconditions
    if type(events) != list:
        raise ValueError("create_event() events expected type list")
    if type(starting_time) != Time:
        raise ValueError("create_event() starting_time expected type Time")
    if type(ending_time) != Time:
        raise ValueError("create_event() ending_time expected type Time")
    if type(attendees) != list:
        raise ValueError("create_event() attendees expected type list")
    if type(summary) != str:
        raise ValueError("create_event() summary expected type str")
    if type(description) != str:
        raise ValueError("create_event() description expected type str")
    if type(location) != Location:
        raise ValueError("create_event() location expected type Location")
    if type(reminders) != list:
        raise ValueError("create_event() reminders expected type list")
    # Value preconditions
    if str(starting_time) > str(ending_time):
        raise ValueError("starting_time cannot be after ending_time")
    time_now = get_time_now()
    if str(starting_time) < str(time_now):
        raise ValueError("starting_time cannot be in the past")
    if starting_time.get_year() > 2050:
        raise ValueError("cannot create event after the year 2050")

    # Create Event and get event body
    event = Event(starting_time, ending_time, attendees, summary, description, location, reminders)
    event_body = event.get_body()
    
    # Create the event in the calendar
    created_event = api.events().insert(calendarId='primary', body=event_body).execute()

    # Get the ID of the event and initialise the ID of the Event
    event.initialise_event_id(created_event['id'])
    
    # Set the organise to the user
    organiser = organiser_to_Organiser(created_event['organizer'])
    event.set_organiser(organiser)

    # Add event to events
    events.append(event)
    
    # Update event with organiser
    update_event(api, events, event.get_event_id(), event)

    return event


def delete_event(api, events: list, event_id: str) -> None:
    # Preconditions
    if type(events) != list:
        raise ValueError("delete_event() events expected type list")
    if type(event_id) != str:
        raise ValueError("delete_event() event_id expected type str")

    # Delete the event from the calendar
    api.events().delete(calendarId='primary', eventId=event_id).execute()

    # If event is in the past, delete the event from the list of events as well, otherwise cancel the event
    time_now = get_time_now()
    for i in range(len(events)):
        if events[i].get_event_id() == event_id:
            # If in the past, delete
            if str(events[i].get_starting_time()) < str(time_now):
                events.pop(i)
                break
            # Else, cancel
            else:
                events[i].cancel_event()
                break



def update_event(api, events: list, event_id: str, event: Event) -> None:
    # Preconditions
    if type(events) != list:
        raise ValueError("update_event() events expected type list")
    if type(event_id) != str:
        raise ValueError("update_event() event_id expected type str")
    if type(event) != Event:
        raise ValueError("update_event() event expected type Event")
    if not check_self_organiser(event):
        raise Exception("only the organiser of the event can make changes to the event")
    
    event_found = False
    # Update events list
    for i in range(len(events)):
        if events[i].get_event_id() == event_id:
            events[i] = event
            event_found = True
            break
    
    # Update event with the input Event
    if event_found:
        event_body = event.get_body()
        api.events().update(calendarId='primary', eventId=event_id, body=event_body).execute()
    else:
        raise Exception("Event with given event_id does not exist")


def get_events_date(events: list, year: int, month: int = None, day: int = None) -> list:
    # Preconditions
    # Type preconditions
    if type(events) != list:
        raise ValueError("get_events_date() events expected type list")
    if type(year) != int:
        raise ValueError("get_events_date() year expected type int")
    if type(month) != int and month is not None:
        raise ValueError("get_events_date() month expected type int")
    if type(day) != int and day is not None:
        raise ValueError("get_events_date() day expected type int")
    if day is not None and month is None:
        raise ValueError("Cannot obtain events for day without specified month")
    
    # Value preconditions
    if month is not None and (month > 12 or month < 1):
        raise ValueError("Invalid month input")
    if day is not None and (day > 31 or day < 1):
        raise ValueError("Invalid day input")

    # Get events
    res = []
    for i in range(len(events)):
        if events[i].get_starting_time() is not None:
            if events[i].get_starting_time().get_year() == year:
                if month is not None:
                    if events[i].get_starting_time().get_month() == month:
                        if day is not None:
                            if events[i].get_starting_time().get_day() == day:
                                res.append(events[i])
                        else:
                            res.append(events[i])
                else:
                    res.append(events[i])
    return res


def get_time_now() -> Time:
    # Get the current time
    time_now = datetime.utcnow().isoformat() + 'Z'
    time_now = time_to_Time(time_now)

    return time_now


def time_to_Time(time: str) -> Time:
    # Preconditions
    if type(time) != str:
        raise ValueError("time_to_Time() time expected type str")

    # Convert to Time
    year = int(time[0:4])
    month = int(time[5:7])
    day = int(time[8:10])
    hour = int(time[11:13])
    minute = int(time[14:16])

    time = Time(year, month, day, hour, minute)
    hour = time.get_hour()+10
    day = time.get_day()
    if hour > 23:
        hour %= 24
        # Try adding an extra day
        try:
            datetime(year, month, day+1, hour, minute)
        # day += 1 is not valid for the month
        except:
            # Try adding an extra month
            try:
                datetime(year, month+1, 1, hour, minute)
            # month += 1 is not valid, since month is probably now 13
            except:
                datetime(year+1, 1, 1, hour, minute)
                day = 1
                month = 1
                year += 1
            # month += 1 is valid
            else:
                day = 1
                month += 1
        # day += 1 is a valid day
        else:
            day += 1
    time.set_hour(hour) # Convert to Australia/Melbourne time
    time.set_day(day)
    time.set_month(month)
    time.set_year(year)
    
    return time


def attendee_to_Attendee(attendee: dict) -> Attendee:
    # Preconditions
    if type(attendee) != dict:
        raise ValueError("attendee_to_Attendee() attendee expected type dict")
    if 'email' not in attendee.keys():
        raise ValueError("Missing email entry for attendee")
    
    # Convert to Attendee
    organiser = False
    is_self = False
    if 'organizer' in attendee.keys():
        if attendee['organizer']:
            organiser = True
    if 'self' in attendee.keys():
        if attendee['self']:
            is_self = True
    attendee_object = Attendee(attendee['email'], organiser, is_self)
    if 'responseStatus' in attendee.keys():
        attendee_object.set_response_status(attendee['responseStatus'])
    else:
        attendee_object.set_response_status("needsAction")
    
    return attendee_object


def organiser_to_Organiser(organiser: dict) -> Organiser:
    # Preconditions
    if type(organiser) != dict:
        raise ValueError("organiser_to_Organiser() organiser expected type dict")
    if 'email' not in organiser.keys():
        raise ValueError("Missing email entry for attendee")
    
    # Convert to Organiser
    is_self = False
    if 'self' in organiser.keys():
        if organiser['self']:
            is_self = True
    return Organiser(organiser['email'], is_self)


def location_to_Location(location: str) -> Location:
    # Preconditions
    if type(location) != str:
        raise ValueError("location_to_Location() location expected type str")
    
    # Create Location
    location = location.split("\n")
    location_object = Location()

    # Address
    if len(location) > 1:
        for i in range(len(location)):
            location[i] = location[i].split(" ")
        
        street_number = location[0][0]
        street_name = ""
        for i in range(1, len(location[0])-1):
            street_name += location[0][i] + " "
        street_name += location[0][-1]
        suburb = ""
        for i in range(len(location[1])-3):
            suburb += location[1][i] + " "
        suburb += location[1][-3]
        postcode = location[1][-1]
        state = location[1][-2]
        country = location[2][0]

        location_object.init_address(street_number, street_name, suburb, state, postcode, country)
    
    # Link
    else:
        location_object.init_link(location[0])

    return location_object


def reminder_to_Reminder(reminder: dict) -> Reminder:
    # Preconditions
    if type(reminder) != dict:
        raise ValueError("reminder_to_Reminder() reminder expected type dict")
    if 'method' not in reminder.keys():
        raise ValueError("Missing method entry in reminder")
    if 'minutes' not in reminder.keys():
        raise ValueError("Missing minutes entry in reminder")
    
    # Convert to Reminder
    return Reminder(reminder['method'], reminder['minutes'])


def event_to_Event(event: dict) -> Event:
    # Preconditions
    if type(event) != dict:
        raise ValueError("event_to_Event() event expected type dict")
    if 'id' not in event.keys():
        raise ValueError("Missing event_id in event")
    
    # Convert to Event
    # Get Event __init__ arguments
    event_id = event['id']

    if 'start' in event.keys(): # cos apparently u can have an event WITHOUT a start time -____-
        starting_time = event['start']['dateTime']
        starting_time = time_to_Time(starting_time)
    else:
        starting_time = None
    
    if 'end' in event.keys():
        ending_time = event['end']['dateTime']
        ending_time = time_to_Time(ending_time)
    else:
        ending_time = None

    if 'organiser' in event.keys():
        organiser = event['organizer']
        organiser = organiser_to_Organiser(organiser)
    else:
        organiser = None
    
    if 'attendees' in event.keys():
        attendees = event['attendees']
        attendees_list = []
        for i in range(len(attendees)):
            attendees_list.append(attendee_to_Attendee(attendees[i]))
    else:
        attendees = None
        attendees_list = None
    
    if 'summary' in event.keys():
        summary = event['summary']
    else:
        summary = None
    
    if 'description' in event.keys():
        description = event['description']
    else:
        description = None
    
    if 'location' in event.keys():
        location = event['location']
        location = location_to_Location(location)
    else:
        location = None

    if 'reminders' in event.keys():
        if 'overrides' in event['reminders'].keys():
            reminders = event['reminders']['overrides']
            reminders_list = []
            for i in range(len(reminders)):
                reminders_list.append(reminder_to_Reminder(reminders[i]))
        else:
            reminders = None
            reminders_list = None
    else:
        reminders = None
        reminders_list = None
    
    
    
    event = Event(starting_time, ending_time, attendees_list, summary, description, location, reminders_list, event_id)
    event.set_organiser(organiser) # Set organiser
    return event


def check_self_organiser(event: Event) -> bool:
    # Preconditions
    if type(event) != Event:
        raise ValueError("check_self_organiser() event expected type Event")

    if event.get_organiser() is None:
        return True
    
    # Check if user is organiser
    return event.get_organiser().get_is_self()


def search_phrase(events: list, phrase: str) -> list:
    # Preconditions
    if type(events) != list:
        raise ValueError("search_phrase() events expected type list")
    if type(phrase) != str:
        raise ValueError("search_phrase() phrase expected type str")

    res = []

    # Search events
    for i in range(len(events)):
        try:
            summary = events[i].get_summary()
        except:
            raise ValueError("search_phrase() events expected a list of Events")
        else:
            description = events[i].get_description()
            if summary is not None:
                if phrase in summary:
                    res.append(events[i])
                elif description is not None:
                    if phrase in description:
                        res.append(events[i])
            elif description is not None:
                if phrase in description:
                    res.append(events[i])
    
    return res


def import_events(filename: str) -> list:
    # Preconditions
    if type(filename) != str:
        raise ValueError("import_events() filename expected type str")

    # Import data
    try:
        with open(filename) as file:
            data = json.load(file)
        
        data = data['data']
        res = []
        for i in range(len(data)):
            res.append(event_to_Event(data[i]))
        return res
    except:
        raise Exception("Invalid file name")


def export_events(events: list, filename: str):
    # Preconditions
    if type(events) != list:
        raise ValueError("export_events() events expected type list")
    if type(filename) != str:
        raise ValueError("export_events() filename expected type str")
    if filename[-5:] != ".json":
        raise ValueError("export_events() filename must be a .json file")

    # Exporting events
    data = []
    for i in range(len(events)):
        try:
            event_body = events[i].get_body()
        except:
            raise ValueError("export_events() events expected a list of Events")
        event_body['id'] = events[i].get_event_id()
        data.append(event_body)
    data = {'data': data}
    json_string = json.dumps(data)
    
    file = open(filename, "w")
    file.write(json_string)


def transfer_organiser(api, event: Event, organiser: Organiser) -> None:
    # Preconditions
    if type(event) != Event:
        raise ValueError("transfer_organiser() event expected type Event")
    if type(organiser) != Organiser:
        raise ValueError("transfer_organiser() oragniser expected type Organiser")

    # Transfer organiser/ownership
    event.transfer_ownership(organiser)
    api.events().update(calendarId='primary', eventId=event.get_event_id(), body=event.get_body()).execute()


def main():
    # Get the api
    api = get_calendar_api()

    # Get the current time
    time_now = get_time_now()

    # Get events
    events = get_events(api)
    # print(events)

    # Get upcoming events
    upcoming_events_api = get_upcoming_events(api, str(time_now), 10)
    upcoming_events = []
    for i in range(len(upcoming_events_api)):
        upcoming_events.append(event_to_Event(upcoming_events_api[i]))

    # Print the upcoming events
    if not upcoming_events:
        print('No upcoming events found.')
    for upcoming_event in upcoming_events:
        start = upcoming_event.get_starting_time().get_object()['dateTime']
        print(start, upcoming_event.get_summary())
    
    '''
    Create event:
    Example:
    start_time = Time(year, month, day, hour=hour, minute=minute)
    end_time = Time(year, month, day, hour=hour, minute=minute)
    attendee1 = Attendee(email, owner) # owner is a bool dictating whether the attendee is the owner or not
    attendee2 = Attendee(email)
    attendee_list = [attendee1, attendee2]
    location = create_location_address(street_number, street_name, suburb, state, postcode, country)
    reminder = Reminder(method, minutes) # minutes is the minutes before the event
    reminder_list = [reminder]

    create_event(api, start_time, end_time, attendee_list, summary, description, location, reminder_list)
    '''

    '''
    Delete event:
    The event ID can be found using the code below "Print ID and summary of all events", which prints the IDs and events when run.
    delete_event(api, event_id)
    '''

    # TEST
    # starting_time = Time(2022, 10, 22, 12, 0)
    # ending_time = Time(2022, 10, 22, 15, 0)
    # attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
    # summary = "test summary"
    # description = "test description"
    # location = Location()
    # location.init_address("3", "Test Ave", "TESTVILLE", "NEW TEST WALES", "8888", "TESTNA")
    # reminders = [Reminder("email", 15), Reminder("popup", 5)]
    # event = create_event(api, events, starting_time, ending_time, attendees, summary, description, location, reminders)

    # # Print ID and summary of all events
    # for i in range(len(events)):
    #     # print(str(events[i].get_event_id()) + ": " + str(events[i].get_summary()))
    #     pass
    
    # transfer_organiser(api, event, Organiser("jlia0058@student.monash.edu"))

    # print(str(events[-1].get_organiser().get_object()))
    # print([str(attendee.get_object()) for attendee in events[-1].get_attendees()])
    
    # delete_event(api, events, event.event_id)


if __name__ == "__main__":  # Prevents the main() function from being called by the test suite runner
    main()

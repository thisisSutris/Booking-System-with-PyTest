from Time import Time
from Attendee import Attendee
from Organiser import Organiser
from Location import Location
from Reminder import Reminder


class Event():
    def __init__(self, starting_time: Time, ending_time: Time, attendees: list, summary: str, description: str, location: Location, reminders: list, event_id: str = "") -> None:
        # Preconditions
        if type(starting_time) != Time and starting_time is not None:
            raise ValueError("Event __init__() starting_time expected type Time")
        if type(ending_time) != Time and ending_time is not None:
            raise ValueError("Event __init__() ending_time expected type Time")
        if type(attendees) != list and attendees is not None:
            raise ValueError("Event __init__() attendees expected type list")
        if type(summary) != str and summary is not None:
            raise ValueError("Event __init__() summary expected type str")
        if type(description) != str and description is not None:
            raise ValueError("Event __init__() description expected type str")
        if type(location) != Location and location is not None:
            raise ValueError("Event __init__() location expected type Location")
        if type(reminders) != list and reminders is not None:
            raise ValueError("Event __init__() reminders expected type list")
        if type(event_id) != str:
            raise ValueError("Event __inist__() event_id expected type str")
        
        # Initialise
        self.event_id = event_id
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.attendees = attendees
        self.summary = summary
        self.description = description
        self.location = location
        self.reminders = reminders
        self.organiser = None

        self.cancelled = False
    

    def get_event_id(self) -> str:
        if self.event_id == "":
            return None
        else:
            return self.event_id

    def get_starting_time(self) -> Time:
        return self.starting_time
    
    def get_ending_time(self) -> Time:
        return self.ending_time
    
    def get_organiser(self) -> Organiser:
        return self.organiser
    
    def get_attendees(self) -> list:
        return self.attendees
    
    def get_summary(self) -> str:
        return self.summary
    
    def get_description(self) -> str:
        return self.description
    
    def get_location(self) -> Location:
        return self.location
    
    def get_reminders(self) -> list:
        return self.reminders
    

    def initialise_event_id(self, event_id: str) -> None:
        if type(event_id) != str:
            raise ValueError("Event initalise_event_id() event_id expected type str")
        
        if self.event_id == "":
            self.event_id = event_id
        else:
            raise Exception("Event ID already initialised")

    def set_starting_time(self, starting_time: Time) -> None:
        if type(starting_time) != Time and starting_time is not None:
            raise ValueError("Event set_starting_time() starting_time expected type Time")
        if starting_time is not None and self.ending_time is not None:
            if str(starting_time) > str(self.ending_time):
                raise ValueError("starting_time cannot be after ending_time")
        self.starting_time = starting_time
    
    def set_ending_time(self, ending_time: Time) -> None:
        if type(ending_time) != Time and ending_time is not None:
            raise ValueError("Event set_ending_time() ending_time expected type Time")
        if ending_time is not None and self.starting_time is not None:
            if str(ending_time) < str(self.starting_time):
                raise ValueError("ending_time cannot be before starting_time")
        self.ending_time = ending_time
    
    def set_organiser(self, organiser: Organiser) -> None:
        if type(organiser) != Organiser and organiser is not None:
            raise ValueError("Event set_organiser() organiser expected type Organiser")
        self.organiser = organiser
    
    def set_attendees(self, attendees: list) -> None:
        if type(attendees) != list and attendees is not None:
            raise ValueError("Event set_attendees() attendees expected type list")
        if attendees is not None and len(attendees) > 20:
            raise ValueError("Events cannot have more than 20 attendees")
        self.attendees = attendees
    
    def set_summary(self, summary: str) -> None:
        if type(summary) != str and summary is not None:
            raise ValueError("Event set_summary() summary expected type str")
        self.summary = summary
    
    def set_description(self, description: str) -> None:
        if type(description) != str and description is not None:
            raise ValueError("Event set_description() description expected type str")
        self.description = description
    
    def set_location(self, location: Location) -> None:
        if type(location) != Location and location is not None:
            raise ValueError("Event set_location() location expected type Location")
        self.location = location
    
    def set_reminders(self, reminders: list) -> None:
        if type(reminders) != list and reminders is not None:
            raise ValueError("Event set_reminders() reminders expected type list")
        self.reminders = reminders
    

    def add_attendee(self, attendee: Attendee) -> None:
        if len(self.attendees) >= 20:
            raise ValueError("Max number of 20 attendees reached")
        if type(attendee) != Attendee:
            raise ValueError("Event add_attendee() attendee expected type Attendee")
        self.attendees.append(attendee)
    
    def remove_attendee(self, index: int) -> Attendee:
        if type(index) != int:
            raise ValueError("Event remove_attendee() index expected type int")
        return self.attendees.pop(index)
    
    def attendee_accept(self, index: int) -> Attendee:
        if type(index) != int:
            raise ValueError("Event attendee_accept() index expected type int")
        self.attendees[index].accept_invitation()
        return self.attendees[index]
    
    def attendee_decline(self, index: int) -> Attendee:
        if type(index) != int:
            raise ValueError("Event attendee_decline() index expected type int")
        self.attendees[index].decline_invitation()
        return self.attendees[index]
    

    def add_reminder(self, reminder: Reminder) -> None:
        if type(reminder) != Reminder:
            raise ValueError("Event add_reminder() reminder expected type Reminder")
        self.reminders.append(reminder)
    

    def remove_reminder(self, index: int) -> Reminder:
        if type(index) != int:
            raise ValueError("Event add_reminder() index expected type int")
        return self.reminders.pop(index)


    def cancel_event(self) -> None:
        if not self.cancelled:
            self.cancelled = True
    

    def uncancel_event(self) -> None:
        if self.cancelled:
            self.cancelled = False
    

    def transfer_ownership(self, organiser: Organiser) -> None:
        if type(organiser) != Organiser:
            raise ValueError("Event transfer_ownership() organiser expected type Organiser")
        
        self.set_organiser(organiser)
        for i in range(len(self.attendees)):
            # Remove previous organiser's status
            if self.attendees[i].get_organiser():
                if self.attendees[i].get_email() != organiser.get_email():
                    self.attendees[i].set_organiser(False)
            # Find the new organiser and set their organiser status
            elif self.attendees[i].get_email() == organiser.get_email():
                self.attendees[i].set_organiser(True)
    

    def get_body(self) -> dict:
        # Create event body
        body = dict()
        if self.starting_time is not None:
            starting_time = self.starting_time.get_object()['dateTime']
            body['start'] = {
                'dateTime': starting_time,
                'timeZone': 'Australia/Melbourne'
            }
        if self.ending_time is not None:
            ending_time = self.ending_time.get_object()['dateTime']
            body['end'] = {
                'dateTime': ending_time,
                'timeZone': 'Australia/Melbourne'
            }
        if self.attendees is not None:
            attendees = []
            for i in range(len(self.attendees)):
                attendees.append(self.attendees[i].get_object())
            body['attendees'] = attendees
        if self.summary is not None:
            body['summary'] = self.summary
        if self.description is not None:
            body['description'] = self.description
        if self.location is not None:
            location = self.location.get_object()
            body['location'] = location
        if self.reminders is not None:
            reminders = []
            for i in range(len(self.reminders)):
                reminders.append(self.reminders[i].get_object())
            body['reminders'] = {
                'useDefault': False,
                'overrides': reminders
            }
        else:
            body['reminders'] = {
                'useDefault': True
            }

        return body
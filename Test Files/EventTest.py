import unittest
from unittest.mock import MagicMock, Mock, patch
from Event import Event
from Time import Time
from Attendee import Attendee
from Organiser import Organiser
from Location import Location
from Reminder import Reminder


class EventTest(unittest.TestCase):
    '''
    Testing __init__():
    
    Tests the functionality of the __init__ method of Event.py.
    Testing strategies found in EventTest_Testing_Plan.md.
    '''
    def test_init(self):
        starting_time = Time(2022, 9, 20, 15, 52)
        ending_time = Time(2022, 10, 27, 12, 1)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        summary = "test summary"
        description = "test description"
        location = Location()
        location.init_address("1", "Some Street", "Some Suburb", "VIC", "3333", "AUSTRALIA")
        reminders = [Reminder("email", 30), Reminder("popup", 15)]
        event_id = "5kff1ufh2fukdedh2l76h58lf0"

        # starting_time Time input, ending_time Time input, attendees list input, summary str input, description str input, location Location input, reminders list input, event_id str input (Pass)
        event1 = Event(starting_time, ending_time, attendees, summary, description, location, reminders, event_id)
        self.assertEqual(event1.starting_time.get_object(), Time(2022, 9, 20, 15, 52).get_object())
        self.assertEqual(event1.ending_time.get_object(), Time(2022, 10, 27, 12, 1).get_object())
        self.assertEqual([attendee.get_object() for attendee in event1.attendees], [Attendee("ayan0024@student.monash.edu", True, True).get_object(), Attendee("jlia0058@student.monash.edu").get_object(), Attendee("zhua0097@student.monash.edu").get_object()])
        self.assertEqual(event1.summary, "test summary")
        self.assertEqual(event1.description, "test description")
        self.assertEqual(event1.location.get_object(), location.get_object())
        self.assertEqual([reminder.get_object() for reminder in event1.reminders], [Reminder("email", 30).get_object(), Reminder("popup", 15).get_object()])
        self.assertEqual(event1.event_id, "5kff1ufh2fukdedh2l76h58lf0")
        
        # starting_time Time input, ending_time other type input, attendees None input, summary None input, description None input, location None input, reminders None input, event_id no input (Fail)
        with self.assertRaises(ValueError):
            Event(starting_time, "Parker! Parker!", None, None, None, None, None)
        
        # starting_time Time input, ending_time None input, attendees other type input, summary str input, description str input, location Location input, reminders list input, event_id str input (Fail)
        with self.assertRaises(ValueError):
            Event(starting_time, None, "No no no! Stop! Stop!", summary, description, location, reminders, event_id)
        
        # starting_time Time input, ending_time Time input, attendees list input, summary other type input, description str input, location Location input, reminders list input, event_id str input (Fail)
        with self.assertRaises(ValueError):
            Event(starting_time, ending_time, attendees, 39485, description, location, reminders, event_id)
        
        # starting_time Time input, ending time None input, attendees None input, summary None input, description other type input, location None input, reminders None input, event_id no input (Fail)
        with self.assertRaises(ValueError):
            Event(starting_time, None, None, None, ["Parker! You're late man!", "Always late!"], None, None)
        
        # starting_time None input, ending time None input, attendees None input, summary None input, description None input, location other type input, reminders None input, event_id no input (Fail)
        with self.assertRaises(ValueError):
            Event(None, None, None, None, None, "Sorry Mr Aziz, there was a disturbance", None)
        
        # starting_time None input, ending time None input, attendees None input, summary None input, description None input, location None input, reminders other type input, event_id no input (Fail)
        with self.assertRaises(ValueError):
            Event(None, None, None, None, None, None, "Another disturbance, always a disturbance with you! Come on!")
        
        # starting_time None input, ending_time Time input, attendees list input, summary str input, description str input, location Location input, reminders list input, event_id None input (Fail)
        with self.assertRaises(ValueError):
            Event(None, ending_time, attendees, summary, description, location, reminders, None)
        
        # starting_time None input, ending_time Time input, attendees list input, summary str input, description str input, location Location input, reminders list input, event_id other type input (Fail)
        with self.assertRaises(ValueError):
            Event(None, ending_time, attendees, summary, description, location, reminders, ["21 minutes ago,", "in comes order"])
        
        # starting_time other type input, ending_time Time input, attendees list input, summary str input, description str input, location Location input, reminders list input, event_id str input (Fail)
        with self.assertRaises(ValueError):
            Event("Harmarttan, Burton and Smith.", ending_time, attendees, summary, description, location, reminders, event_id)
        
        # starting_time None input, ending_time None input, attendees None input, summary None input, description None input, location None input, reminders None input, event_id no input (Pass)
        event2 = Event(None, None, None, None, None, None, None)
        self.assertEqual(event2.starting_time, None)
        self.assertEqual(event2.ending_time, None)
        self.assertEqual(event2.attendees, None)
        self.assertEqual(event2.summary, None)
        self.assertEqual(event2.description, None)
        self.assertEqual(event2.location, None)
        self.assertEqual(event2.reminders, None)


    '''
    Testing accessors:
    
    Tests the functionalities of the accessor methods in Event.py.
    Tests:
    - get_event_id()
    - get_starting_time()
    - get_ending_time()
    - get_organiser()
    - get_attendees()
    - get_summary()
    - get_description()
    - get_location()
    - get_reminders()

    Testing strategies found in EventTest_Testing_Plan.md.
    '''
    def test_accessors(self):
        starting_time = Time(2022, 9, 20, 15, 52)
        ending_time = Time(2022, 10, 27, 12, 1)
        organiser = Organiser("ayan0024@student.monash.edu", True)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        summary = "test summary"
        description = "test description"
        location = Location()
        location.init_address("1", "Some Street", "Some Suburb", "VIC", "3333", "AUSTRALIA")
        reminders = [Reminder("email", 30), Reminder("popup", 15)]
        event_id = "5kff1ufh2fukdedh2l76h58lf0"
        event = Event(starting_time, ending_time, attendees, summary, description, location, reminders, event_id)
        event.organiser = organiser

        # Testing get_event_id()
        self.assertEqual(event.get_event_id(), "5kff1ufh2fukdedh2l76h58lf0")

        # Testing get_starting_time()
        self.assertEqual(event.get_starting_time().get_object(), Time(2022, 9, 20, 15, 52).get_object())
        
        # Testing get_ending_time()
        self.assertEqual(event.get_ending_time().get_object(), Time(2022, 10, 27, 12, 1).get_object())
        
        # Testing get_organiser()
        self.assertEqual(event.get_organiser().get_object(), Organiser("ayan0024@student.monash.edu", True).get_object())

        # Testing get_attendees()
        self.assertEqual(event.get_attendees(), attendees)

        # Testing get_summary()
        self.assertEqual(event.get_summary(), "test summary")

        # Testing get_description()
        self.assertEqual(event.get_description(), "test description")

        # Testing get_location()
        self.assertEqual(event.get_location().get_object(), location.get_object())

        # Testing get_reminders()
        self.assertEqual(event.get_reminders(), reminders)
        
    
    '''
    Testing mutators:
    
    Tests the functionalities of the mutators methods in Event.py.
    Tests:
    - initialise_event_id()
    - set_starting_time()
    - set_ending_time()
    - set_organiser()
    - set_attendees()
    - set_summary()
    - set_description()
    - set_location()
    - set_reminders()
    
    Testing strategies found in EventTest_Testing_Plan.md.
    '''
    def test_mutators(self):
        starting_time = Time(2022, 9, 20, 15, 52)
        ending_time = Time(2022, 10, 27, 12, 1)
        organiser = Organiser("ayan0024@student.monash.edu", True)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        summary = "test summary"
        description = "test description"
        location = Location()
        location.init_address("1", "Some Street", "Some Suburb", "VIC", "3333", "AUSTRALIA")
        reminders = [Reminder("email", 30), Reminder("popup", 15)]
        event_id = "5kff1ufh2fukdedh2l76h58lf0"
        event = Event(starting_time, ending_time, attendees, summary, description, location, reminders)
        event.organiser = organiser

        # Testing initialise_event_id()
        # - event_id is not properly initialised and str is given
        event.initialise_event_id(event_id)
        self.assertEqual(event.event_id, "5kff1ufh2fukdedh2l76h58lf0")
        
        # - event_id has already been initialised and str is given
        with self.assertRaises(Exception):
            event.initialise_event_id(event_id) # event_id already initialised above
        
        # - Non-str type is given
        with self.assertRaises(ValueError):
            event.initialise_event_id(0.00000000000885418782)
        
        # Testing set_starting_time()
        # - starting_time Time input, starting_time is before ending_time, correct time is set
        event.set_starting_time(Time(2022, 9, 20, 6, 47))
        self.assertEqual(event.starting_time.get_object(), Time(2022, 9, 20, 6, 47).get_object())
        
        # - starting_time Time input, starting_time is after ending_time, error is thrown
        with self.assertRaises(ValueError):
            event.set_starting_time(Time(2022, 12, 25, 0, 0))
        
        # - starting_time None input
        event.set_starting_time(None)
        self.assertEqual(event.starting_time, None)
        
        # - starting_time non-Time input, error is thrown
        with self.assertRaises(ValueError):
            event.set_starting_time("8 extra-large deep-dish pizzas")
        
        # Testing set_ending_time()
        event.starting_time = starting_time

        # - ending_time Time input, ending_time is after starting_time, correct time is set
        event.set_ending_time(Time(2022, 12, 25, 0, 0))
        self.assertEqual(event.ending_time.get_object(), Time(2022, 12, 25, 0, 0).get_object())
        
        # - ending_time Time input, ending_time is before starting_time, error is thrown
        with self.assertRaises(ValueError):
            event.set_ending_time(Time(2022, 4, 25, 0, 0))
        
        # - ending_time None input
        event.set_ending_time(None)
        self.assertEqual(event.ending_time, None)
        
        # - ending_time non-Time input, error is thrown
        with self.assertRaises(ValueError):
            event.set_ending_time("In 8 minutes, I am defaulting on Joe's 29 minute guarantee")
        
        # Testing set_organiser()
        # - organiser Organiser input, correct organiser is set
        event.set_organiser(Organiser("jlia0058@student.monash.edu"))
        self.assertEqual(event.organiser.get_object(), Organiser("jlia0058@student.monash.edu").get_object())
        
        # - organiser None input
        event.set_organiser(None)
        self.assertEqual(event.organiser, None)
        
        # - organiser non-Organiser input, error is thrown
        with self.assertRaises(ValueError):
            event.set_organiser("Then, not only am I receiving no money for these pizzas")
        
        # Testing set_attendees()
        # - attendees list input, len(attendees) <= 20, correct attendees is set
        event.set_attendees([Attendee("ayan0024@student.monash.edu", True, True), Attendee("zhua0097@student.monash.edu")])
        self.assertEqual([attendee.get_object() for attendee in event.attendees], [Attendee("ayan0024@student.monash.edu", True, True).get_object(), Attendee("zhua0097@student.monash.edu").get_object()])
        
        # - attendees list input, len(attendees) > 20, error is thrown
        with self.assertRaises(ValueError):
            event.set_attendees([Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu"), Attendee("email4"), Attendee("email5"), Attendee("email6"), Attendee("email7"), Attendee("email8"), Attendee("email9"), Attendee("email10"), Attendee("email11"), Attendee("email12"), Attendee("email13"), Attendee("email14"), Attendee("email15"), Attendee("email16"), Attendee("email17"), Attendee("email18"), Attendee("email19"), Attendee("email20"), Attendee("email21")])
        
        # - attendees None input
        event.set_attendees(None)
        self.assertEqual(event.attendees, None)
        
        # - attendees non-list input, error is thrown
        with self.assertRaises(ValueError):
            event.set_attendees("But, I will lose the customer forever to Pizza Yurt")
        
        # Testing set_summary()
        # - summary str input, correct summary is set
        event.set_summary("Look, you are my only hope, alright? You have to make it in time")
        self.assertEqual(event.summary, "Look, you are my only hope, alright? You have to make it in time")
        
        # - summary None input
        event.set_summary(None)
        self.assertEqual(event.summary, None)
        
        # - summary non-str input, error is thrown (Fail)
        with self.assertRaises(ValueError):
            event.set_summary(0000000000000000000000000000000000.105457182)
        
        # Testing set_description()
        # - description str input, correct description is set
        event.set_description("Peter, you're a nice guy, but you're just not dependable")
        self.assertEqual(event.description, "Peter, you're a nice guy, but you're just not dependable")
        
        # - description None input
        event.set_description(None)
        self.assertEqual(event.description, None)
        
        # - description non-str input, error is thrown
        with self.assertRaises(ValueError):
            event.set_description(0000000000000000000.160217663)
        
        # Testing set_location()
        
        # - location Location input, correct location is set
        new_location = Location()
        new_location.init_address("12", "Test Road", "Test Waverley", "VIC", "9999", "AUSTRALIA")
        event.set_location(new_location)
        self.assertEqual(event.location.get_object(), new_location.get_object())
        
        # - location None input
        event.set_location(None)
        self.assertEqual(event.location, None)
        
        # - location non-Location input, error is thrown
        with self.assertRaises(ValueError):
            event.set_location("This is your last chance")
        
        # Testing set_reminders()
        # - reminders list input, correct reminders is set
        event.set_reminders([Reminder("email", 30)])
        self.assertEqual([reminder.get_object() for reminder in event.reminders], [Reminder("email", 30).get_object()])
        
        # - reminders None input
        event.set_reminders(None)
        self.assertEqual(event.reminders, None)
        
        # - reminders non-list input, error is thrown
        with self.assertRaises(ValueError):
            event.set_reminders("You have to go 42 blocks in 7 and one half minutes")
    

    '''
    Testing actions:
    
    Tests the functionalities of methods that perform actions in Event.py.
    Tests:
    - add_attendee()
    - remove_attendee()
    - attendee_accept()
    - attendee_decline()
    - add_reminder()
    - remove_reminder()
    - cancel_event()
    - uncancel_event()
    - transfer_ownership()
    
    Testing strategies found in EventTest_Testing_Plan.md.
    '''
    def test_actions(self):
        starting_time = Time(2022, 9, 20, 15, 52)
        ending_time = Time(2022, 10, 27, 12, 1)
        organiser = Organiser("ayan0024@student.monash.edu", True)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        summary = "test summary"
        description = "test description"
        location = Location()
        location.init_address("1", "Some Street", "Some Suburb", "VIC", "3333", "AUSTRALIA")
        reminders = [Reminder("email", 30), Reminder("popup", 15)]
        event = Event(starting_time, ending_time, attendees, summary, description, location, reminders)
        event.organiser = organiser

        # Testing add_attendee()
        # - attendee Attendee input, correct attendees list is set
        event.add_attendee(Attendee("someone@somemail.com"))
        self.assertEqual([attendee.get_object() for attendee in event.attendees], [Attendee("ayan0024@student.monash.edu", True, True).get_object(), Attendee("jlia0058@student.monash.edu").get_object(), Attendee("zhua0097@student.monash.edu").get_object(), Attendee("someone@somemail.com").get_object()])
        
        # - attendee non-Attendee input, error is thrown
        with self.assertRaises(ValueError):
            event.add_attendee("Or your *** is fired")
        
        # - len(attendees) is 20, error is thrown
        event.set_attendees([Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu"), Attendee("email4"), Attendee("email5"), Attendee("email6"), Attendee("email7"), Attendee("email8"), Attendee("email9"), Attendee("email10"), Attendee("email11"), Attendee("email12"), Attendee("email13"), Attendee("email14"), Attendee("email15"), Attendee("email16"), Attendee("email17"), Attendee("email18"), Attendee("email19"), Attendee("email20")])
        with self.assertRaises(ValueError):
            event.add_attendee(Attendee("someone@somemail.com"))
        
        # Testing remove_attendee()
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        event.set_attendees(attendees)
        
        # - index int input, index is in range, correct attendees list is set
        event.remove_attendee(1)
        self.assertEqual([attendee.get_object() for attendee in event.attendees], [Attendee("ayan0024@student.monash.edu", True, True).get_object(), Attendee("zhua0097@student.monash.edu").get_object()])
        
        # - index int input, index is out of range, error is thrown
        with self.assertRaises(IndexError):
            event.remove_attendee(3)
        
        # - index non-int input, error is thrown
        with self.assertRaises(ValueError):
            event.remove_attendee("GOO-OOO!!")
        
        # Testing attendee_accept()
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        event.set_attendees(attendees)
        
        # - index int input, index is in range, correct attendee response status is set
        event.attendee_accept(0)
        self.assertEqual(event.attendees[0].response_status, "accepted")
        
        # - index int input, index is out of range, error is thrown
        with self.assertRaises(IndexError):
            event.attendee_accept(5)
        # - index non-int input, error is thrown
        with self.assertRaises(ValueError):
            event.attendee_accept("Hey, what, are you st***d?")
        
        # Testing attendee_decline()
        # - index int input, index is in range, correct attendee response status is set
        event.attendee_decline(1)
        self.assertEqual(event.attendees[1].response_status, "declined")
        
        # - index int input, index is out of range, error is thrown
        with self.assertRaises(IndexError):
            event.attendee_decline(6)
        
        # - index non-int input, error is thrown
        with self.assertRaises(ValueError):
            event.attendee_decline("Whoa! He stole that guy's pizzas!")
        
        # Testing add_reminder()
        event.set_reminders(reminders)

        # - reminder Reminder input, correct reminder list is set
        event.add_reminder(Reminder("email", 45))
        self.assertEqual([reminder.get_object() for reminder in event.reminders], [Reminder("email", 30).get_object(), Reminder("popup", 15).get_object(), Reminder("email", 45).get_object()])
        
        # - reminder non-Reminder input, error is thrown
        with self.assertRaises(ValueError):
            event.add_reminder("I'm gonna get it!")
        
        # Testing remove_reminder()
        reminders = [Reminder("email", 30), Reminder("popup", 15)]
        event.set_reminders(reminders)
        
        # - index int input, index is in range, correct reminders list is set
        event.remove_reminder(0)
        self.assertEqual([reminder.get_object() for reminder in event.reminders], [Reminder("popup", 15).get_object()])
        
        # - index int input, index is out of range, error is thrown
        with self.assertRaises(IndexError):
            event.remove_reminder(7)
        
        # - index non-int input, error is thrown
        with self.assertRaises(ValueError):
            event.remove_reminder("Hey you guys, no playing in the streets")
        
        # Testing cancel_event()
        event.cancel_event()
        self.assertEqual(event.cancelled, True)
        
        # Testing uncancel_event()
        event.uncancel_event()
        self.assertEqual(event.cancelled, False)
        
        # Testing transfer_ownership()
        # - organiser type Organiser, organiser in attendee list (self.attendees[i].get_organiser() == True), the organiser in the attendee is not the organiser (self.attendees[i].get_email() != organiser.get_email()) (Pass)
        # - organiser type Organiser, organiser not in attendee list, but the new organiser is in the attendee list, the attendee is given organiser status (Pass)
        event.transfer_ownership(Organiser("jlia0058@student.monash.edu"))
        self.assertEqual(event.organiser.get_object(), Organiser("jlia0058@student.monash.edu").get_object())
        self.assertEqual(event.get_attendees()[0].get_organiser(), False)
        self.assertEqual(event.get_attendees()[1].get_organiser(), True)

        # - organiser type Organiser, organiser in attendee list (self.attendees[i].get_organiser() == True), the organiser in the attendee is the organiser (self.attendees[i].get_email() == organiser.get_email()) (Pass)
        event.transfer_ownership(Organiser("ayan0024@student.monash.edu"))
        self.assertEqual(event.organiser.get_object(), Organiser("ayan0024@student.monash.edu").get_object())
        self.assertEqual(event.get_attendees()[0].get_organiser(), True)

        # organiser type Organiser, organiser not in attendee list, and the new organiser is not in the attendee list (Pass)
        event.transfer_ownership(Organiser("adam.yang@monash.edu"))
        self.assertEqual(event.organiser.get_object(), Organiser("adam.yang@monash.edu").get_object())
        self.assertEqual(event.get_attendees()[0].get_organiser(), False)
        
        # - organiser non-Organiser input, error is thrown (Fail)
        with self.assertRaises(ValueError):
            event.transfer_ownership("Yes Mr Spiderman")
        
    
    '''
    Testing get_body():
    
    Tests the functionality of the get_body() method in Event.py and checks that the correct result is returned.
    
    Testing strategies found in EventTest_Testing_Plan.md.
    '''
    def testing_get_body(self):
        starting_time = Time(2022, 9, 20, 15, 52)
        ending_time = Time(2022, 10, 27, 12, 1)
        organiser = Organiser("ayan0024@student.monash.edu", True)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        summary = "test summary"
        description = "test description"
        location = Location()
        location.init_address("1", "Some Street", "Some Suburb", "VIC", "3333", "AUSTRALIA")
        reminders = [Reminder("email", 30), Reminder("popup", 15)]
        event_id = "5kff1ufh2fukdedh2l76h58lf0"
        event = Event(starting_time, ending_time, attendees, summary, description, location, reminders, event_id)
        event.organiser = organiser
        
        # Correct event body is returned for the test Event
        self.assertEqual(event.get_body(), {
                'start': {
                    'dateTime': Time(2022, 9, 20, 15, 52).get_object()['dateTime'],
                    'timeZone': 'Australia/Melbourne'
                },
                'end': {
                    'dateTime': Time(2022, 10, 27, 12, 1).get_object()['dateTime'],
                    'timeZone': 'Australia/Melbourne'
                },
                'attendees': [Attendee("ayan0024@student.monash.edu", True, True).get_object(), Attendee("jlia0058@student.monash.edu").get_object(), Attendee("zhua0097@student.monash.edu").get_object()],
                'summary': "test summary",
                'description': "test description",
                'location': location.get_object(),
                'reminders': {
                    'useDefault': False,
                    'overrides': [Reminder("email", 30).get_object(), Reminder("popup", 15).get_object()]
                }
            }
        )


def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(EventTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
main()
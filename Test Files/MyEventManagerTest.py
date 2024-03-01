import unittest
from unittest.mock import MagicMock, Mock, patch
import MyEventManager
# Add other imports here if needed
import datetime
from Event import Event
from Time import Time
from Organiser import Organiser
from Attendee import Attendee
from Location import Location
from Reminder import Reminder

class MyEventManagerTest(unittest.TestCase):
    # This test tests number of upcoming events.
    def test_get_upcoming_events_number(self):
        num_events = 2
        time = "2020-08-03T00:00:00.000000Z"

        mock_api = Mock()
        events = MyEventManager.get_upcoming_events(mock_api, time, num_events)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['maxResults'], num_events)

    
    '''
    Testing get_events().

    Tests the functionality, preconditions and return result of the function.
    These tests use mocking to mock the api.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_get_events(self):
        mock_api = Mock()

        # Test that the function returns the correct set of events from the api
        events_api = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api
        events = []
        for i in range(len(events_api)):
            events.append(MyEventManager.event_to_Event(events_api[i]))
        
        self.assertEqual([event.get_body() for event in events], [event.get_body() for event in MyEventManager.get_events(mock_api)])
        

    '''
    Testing create_location_address().

    Tests the functionality, preconditions and return result of the function.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_create_location_address(self):
        # street_number str input, street_name str input, suburb str input, state str input, postcode str input, country str input (Pass)
        location = Location()
        location.init_address("3", "Test St", "TESTURB", "TESTORIA", "9999", "TESTRALIA")
        self.assertEqual(MyEventManager.create_location_address("3", "Test St", "TESTURB", "TESTORIA", "9999", "TESTRALIA").get_object(), location.get_object())

        # street_number non-str input, street_name str input, suburb str input, state str input, postcode str input, country str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_location_address(3, "Test St", "TESTURB", "TESTORIA", "9999", "TESTRALIA")

        # street_number str input, street_name non-str input, suburb str input, state str input, postcode str input, country str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_location_address("3", ["Test", "St"], "TESTURB", "TESTORIA", "9999", "TESTRALIA")
        
        # street_number str input, street_name str input, suburb non-str input, state str input, postcode str input, country str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_location_address("3", "Test St", 602214080000000000000000, "TESTORIA", "9999", "TESTRALIA")

        # street_number str input, street_name str input, suburb str input, state non-str input, postcode str input, country str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_location_address("3", "Test St", "TESTURB", {1, 2, 3}, "9999", "TESTRALIA")
        
        # street_number str input, street_name str input, suburb str input, state str input, postcode non-str input, country str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_location_address("3", "Test St", "TESTURB", "TESTORIA", [9, 9, 9, 9], "TESTRALIA")
        
        # street_number str input, street_name str input, suburb str input, state str input, postcode str input, country non-str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_location_address("3", "Test St", "TESTURB", "TESTORIA", "9999", Organiser("test@email.com"))


    '''
    Testing create_location_link().

    Tests the functionality, preconditions and return result of the function.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_create_location_link(self):
        # link str input (Pass)
        location = Location()
        location.init_link("http://www.script-o-rama.com/movie_scripts/s/spider-man-2-script-transcript.html")
        self.assertEqual(MyEventManager.create_location_link("http://www.script-o-rama.com/movie_scripts/s/spider-man-2-script-transcript.html").get_object(), location.get_object())

        # link non-str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_location_link(0.00000000000000000000001380649)
    

    '''
    Testing create_event().

    Tests the functionality, preconditions and return result of the function.
    These tests use mocking to mock the api.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_create_event(self):
        mock_api = Mock()

        starting_time = Time(2022, 10, 22, 12, 0)
        ending_time = Time(2022, 10, 22, 15, 0)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        summary = "test summary"
        description = "test description"
        location = Location()
        location.init_address("3", "Test Ave", "TESTVILLE", "NEW TEST WALES", "8888", "TESTNA")
        reminders = [Reminder("email", 15), Reminder("popup", 5)]

        events_api = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        events = []
        for i in range(len(events_api)):
            events.append(MyEventManager.event_to_Event(events_api[i]))

        # Testing inputs
        # - events non-list input
        # - starting_time Time input, before ending_time, after current time, before 2050
        # - ending_time Time input, after starting_time
        # - attendees list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, 57928, starting_time, ending_time, attendees, summary, description, location, reminders)

        # - events list input
        # - starting_time Time input, after ending_time, after current time, before 2050
        # - ending_time Time input, after starting_time
        # - attendees list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, Time(2022, 10, 22, 18, 0), ending_time, attendees, summary, description, location, reminders)
        
        # - events list input
        # - starting_time Time input, before ending_time, before current time, before 2050
        # - ending_time Time input, after starting_time
        # - attendees list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, Time(2021, 10, 22, 12, 0), ending_time, attendees, summary, description, location, reminders)
        
        # - events list input
        # - starting_time Time input, before ending_time, after current time, after 2050
        # - ending_time Time input, after starting_time
        # - attendees list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, Time(2060, 10, 22, 12, 0), ending_time, attendees, summary, description, location, reminders)
        
        # - events list input
        # - starting_time non-Time input
        # - ending_time Time input, after_starting_time
        # - attendees list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, 12345, ending_time, attendees, summary, description, location, reminders)
        
        # - events list input
        # - starting_time Time input, before ending_time, after current time, before 2050
        # - ending_time Time input, before starting_time
        # - attendees list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders list input 
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, starting_time, Time(2022, 10, 22, 9, 0), attendees, summary, description, location, reminders)

        # - events list input
        # - starting_time Time input, before ending_time, after current time, before 2050
        # - ending_time non-Time input
        # - attendees list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, starting_time, "hello there", attendees, summary, description, location, reminders)
        
        # - events list input
        # - starting_time Time input, before ending_time, after current time, before 2050
        # - ending_time Time input, after starting_time
        # - attendees non-list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, starting_time, ending_time, "general kenobi", summary, description, location, reminders)
        
        # - events list input
        # - starting_time Time input, before ending_time, after current time, before 2050
        # - ending_time Time input, after starting_time
        # - attendees list input; summary non-str input
        # - description str input; location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, starting_time, ending_time, attendees, 385, description, location, reminders)
        
        # - events list input
        # - starting_time Time input, before ending_time, after current time, before 2050
        # - ending_time Time input, after starting_time
        # - attendees list input
        # - summary str input
        # - description non-str input
        # - location Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, starting_time, ending_time, attendees, summary, [1,7,4,6,3], location, reminders)
        
        # - events list input
        # - starting_time Time input, before ending_time, after current time, before 2050
        # - ending_time Time input, after starting_time
        # - attendees list input
        # - summary str input
        # - description str input
        # - location non-Location input
        # - reminders list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, starting_time, ending_time, attendees, summary, description, "you are a bold one", reminders)
        
        # - events list input
        # - starting_time Time input, before ending_time, after current time, before 2050
        # - ending_time Time input, after starting_time
        # - attendees list input
        # - summary str input
        # - description str input
        # - location Location input
        # - reminders non-list input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, events, starting_time, ending_time, attendees, summary, description, location, "kill him")
        
        # Functionality
        events_api = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api
        events = []
        for i in range(len(events_api)):
            events.append(MyEventManager.event_to_Event(events_api[i]))
        self.assertEqual(events_api, mock_api.events().list(calendarId='primary').execute().get('items', []))

        event = Event(starting_time, ending_time, [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")], summary, description, location, reminders, "lu9ar5jcrpovcp5omk8s321m8g")
        event.set_organiser(Organiser("ayan0024@student.monash.edu", True))
        events_api_created1 = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'},
            {'kind': 'calendar#event', 'etag': '"3327661707043000"', 'id': 'lu9ar5jcrpovcp5omk8s321m8g', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=bHU5YXI1amNycG92Y3A1b21rOHMzMjFtOGcgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T07:14:13.000Z', 'updated': '2022-09-22T07:14:13.633Z', 'summary': 'test summary', 'description': 'test description', 'location': '3 Test Ave\nTESTVILLE NEW TEST WALES 8888\nTESTNA', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2022-10-22T23:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-10-23T02:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'lu9ar5jcrpovcp5omk8s321m8g@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'jlia0058@student.monash.edu', 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 5}, {'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.insert.return_value.execute.return_value = {'kind': 'calendar#event', 'etag': '"3327661707043000"', 'id': 'lu9ar5jcrpovcp5omk8s321m8g', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=bHU5YXI1amNycG92Y3A1b21rOHMzMjFtOGcgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T07:14:13.000Z', 'updated': '2022-09-22T07:14:13.633Z', 'summary': 'test summary', 'description': 'test description', 'location': '3 Test Ave\nTESTVILLE NEW TEST WALES 8888\nTESTNA', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2022-10-22T23:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-10-23T02:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'lu9ar5jcrpovcp5omk8s321m8g@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'jlia0058@student.monash.edu', 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 5}, {'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api_created1

        self.assertEqual(MyEventManager.create_event(mock_api, events, starting_time, ending_time, [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")], summary, description, location, reminders).get_body(), event.get_body())
        self.assertEqual(events_api_created1, mock_api.events().list(calendarId='primary').execute().get('items', []))
        self.assertEqual(MyEventManager.create_event(mock_api, events, starting_time, ending_time, [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")], summary, description, location, reminders).get_organiser().get_object(), Organiser("ayan0024@student.monash.edu", True).get_object())
        self.assertEqual(MyEventManager.create_event(mock_api, events, starting_time, ending_time, [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")], summary, description, location, reminders).get_event_id(), "lu9ar5jcrpovcp5omk8s321m8g")


    '''
    Testing delete_event().

    Tests the functionality, preconditions and return result of the function.
    These tests use mocking to mock the api.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_delete_event(self):
        mock_api = Mock()

        # Testing inputs
        # events non-list input, event_id str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.delete_event(mock_api, 299792458, "5kff1ufh2fukdedh2l76h58lf0")
        
        # events list input, event_id non_str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.delete_event(mock_api, ["event1 stub", "event2 stub", "event3 stub"], 0.00000125663706)

        # Functionality
        # events list input, event_id str input
        events_api = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api
        events = []
        for i in range(len(events_api)):
            events.append(MyEventManager.event_to_Event(events_api[i]))
        self.assertEqual(events_api, mock_api.events().list(calendarId='primary').execute().get('items', []))

        # Deleting events in the past
        events_api_deleted1 = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api_deleted1

        events_deleted = []
        for i in range(len(events)):
            if i != 1:
                events_deleted.append(events[i])

        MyEventManager.delete_event(mock_api, events, "4qs1bavmra1i74c7dojvlovdsc")
        self.assertEqual(events_api_deleted1, mock_api.events().list(calendarID='primary').execute().get('items', []))
        self.assertEqual(events_deleted, events)

        # Cancelling upcoming events
        events_api_deleted2 = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api_deleted2

        events = []
        for i in range(len(events_api)):
            events.append(MyEventManager.event_to_Event(events_api[i]))

        events_deleted = events.copy()
        events_deleted[3].cancel_event()
        
        MyEventManager.delete_event(mock_api, events, "h9jp2o34um9jj57hqpubneg52c")
        self.assertEqual(events_api_deleted2, mock_api.events().list(calendarID='primary').execute().get('items', []))
        self.assertEqual(events, events_deleted)


    '''
    Testing update_event().

    Tests the functionality, preconditions and return result of the function.
    These tests use mocking to mock the api.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_update_event(self):
        mock_api = Mock()

        starting_time = Time(2022, 10, 22, 12, 0)
        ending_time = Time(2022, 10, 22, 15, 0)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        summary = "test summary"
        description = "test description"
        location = Location()
        location.init_address("3", "Test Ave", "TESTVILLE", "NEW TEST WALES", "8888", "TESTNA")
        reminders = [Reminder("email", 15), Reminder("popup", 5)]

        events_api = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        events = []
        for i in range(len(events_api)):
            events.append(MyEventManager.event_to_Event(events_api[i]))
        event = Event(starting_time, ending_time, attendees, summary, description, location, reminders, "lu9ar5jcrpovcp5omk8s321m8g")

        # Testing inputs
        # - events non-list input
        # - event_id str input, valid event_id
        # - event Event input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.update_event(mock_api, "back away, i will deal with jedi slime myself", "lu9ar5jcrpovcp5omk8s321m8g", event)
        
        # - events list input
        # - event_id str input, invalid event_id
        # - event Event input
        # - (Fail)
        with self.assertRaises(Exception):
            MyEventManager.update_event(mock_api, events, "you're move?", event)
        
        # - events list input
        # - event_id non-str input
        # - event Event
        # - (Fail)
        with self.assertRaises(Exception):
            MyEventManager.update_event(mock_api, events, 42497, event)
        
        # - events list input
        # - event_id str input, valid event_id
        # - event non-Event input
        # - (Fail)
        with self.assertRaises(Exception):
            MyEventManager.update_event(mock_api, events, "lu9ar5jcrpovcp5omk8s321m8g", "you fool, i was trained in your jedi arts, by count dooku")
        
        # Functionality
        events_api = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'},
            {'kind': 'calendar#event', 'etag': '"3327661707043000"', 'id': 'lu9ar5jcrpovcp5omk8s321m8g', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=bHU5YXI1amNycG92Y3A1b21rOHMzMjFtOGcgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T07:14:13.000Z', 'updated': '2022-09-22T07:14:13.633Z', 'summary': 'test summary', 'description': 'test description', 'location': '3 Test Ave\nTESTVILLE NEW TEST WALES 8888\nTESTNA', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2022-10-22T23:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-10-23T02:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'lu9ar5jcrpovcp5omk8s321m8g@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'jlia0058@student.monash.edu', 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 5}, {'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api
        events = []
        for i in range(len(events_api)):
            events.append(MyEventManager.event_to_Event(events_api[i]))
        self.assertEqual(events_api, mock_api.events().list(calendarId='primary').execute().get('items', []))

        starting_time_updated = Time(2023, 10, 22, 12, 0)
        ending_time_updated = Time(2023, 10, 22, 15, 0)
        attendees_updated = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("zhua0097@student.monash.edu")]
        summary_updated = "tteesstt ssuummmmaarryy"
        description_updated = "tteesstt ddeessccrriippttiioonn"
        location_updated = Location()
        location_updated.init_address("33", "TTeesstt AAvvee", "TTEESSTTVVIILLLLEE", "NNEEWW TTEESSTT WWAALLEESS", "88888888", "TTEESSTTNNAA")
        reminders_updated = [Reminder("email", 30), Reminder("popup", 100)]
        events_api_updated = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'},
            {'kind': 'calendar#event', 'etag': '"3327661707043000"', 'id': 'lu9ar5jcrpovcp5omk8s321m8g', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=bHU5YXI1amNycG92Y3A1b21rOHMzMjFtOGcgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T07:14:13.000Z', 'updated': '2022-09-22T07:14:13.633Z', 'summary': 'tteesstt ssuummmmaarryy', 'description': 'tteesstt ddeessccrriippttiioonn', 'location': '33 TTeesstt AAvvee\nTTEESSTTVVIILLLLEE NNEEWW TTEESSTT WWAALLEESS 88888888\nTTEESSTTNNAA', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2023-10-22T23:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2023-10-23T02:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'lu9ar5jcrpovcp5omk8s321m8g@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 100}, {'method': 'email', 'minutes': 30}]}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api_updated
        event.set_ending_time(ending_time_updated)
        event.set_starting_time(starting_time_updated)
        event.set_attendees(attendees_updated)
        event.set_summary(summary_updated)
        event.set_description(description_updated)
        event.set_location(location_updated)
        event.set_reminders(reminders_updated)

        MyEventManager.update_event(mock_api, events, "lu9ar5jcrpovcp5omk8s321m8g", event)
        self.assertEqual(events_api_updated, mock_api.events().list(calendarID='primary').execute().get('items', []))
        self.assertEqual(event.get_body(), events[4].get_body())
    

    '''
    Testing get_events_date().

    Tests the functionality, preconditions and return result of the function.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_get_events_date(self):
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        description = "test description"
        location = Location()
        location.init_address("17", "Test Drive", "TEST WAVERLEY", "TESTORIA", "3333", "TESTRALIA")
        reminders = [Reminder("email", 30), Reminder("popup", 10)]
        events = [
            Event(Time(2021, 7, 8, 0, 0), Time(2021, 7, 8, 23, 59), attendees, "test date 8/7/2021 (1)", description, location, reminders, "5kff1ufh2fukdedh2l76h58lf0"),
            Event(Time(2022, 7, 8, 0, 0), Time(2022, 7, 8, 23, 59), attendees, "test date 8/7/2022", description, location, reminders, "4qs1bavmra1i74c7dojvlovdsc"),
            Event(Time(2022, 7, 20, 0, 0), Time(2022, 7, 20, 23, 59), attendees, "test date 20/7/2022", description, location, reminders, "tir7t1dfse2qoppsfosh0q16jk"),
            Event(Time(2022, 3, 18, 0, 0), Time(2022, 3, 18, 23, 59), attendees, "test date 18/3/2022", description, location, reminders, "h9jp2o34um9jj57hqpubneg52c"),
            Event(Time(2021, 8, 20, 0, 0), Time(2022, 8, 20, 23, 59), attendees, "test date 20, 8, 2021", description, location, reminders, "lu9ar5jcrpovcp5omk8s321m8g"),
            Event(Time(2021, 7, 8, 0, 0), Time(2021, 7, 8, 23, 59), attendees, "test date 8/7/2021 (2)", description, location, reminders, "sdht6j4bwsbvosugbetoi23obv")
        ]
        
        # Testing inputs
        # - events non-list input
        # - year int input
        # - month int input, month in [1, 12]
        # - day int input, day in [1, 31]
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date("See ya", 2022, 9, 23)
        
        # - events list input
        # - year non-int input
        # - month int input, month in [1, 12]
        # - day int input, day in [1, 31]
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date(events, "2022", 9, 23)
        
        # - events list input
        # - year int input
        # - month int input, month < 1
        # - day int input, day in [1, 31]
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date(events, 2022, 0, 23)
        
        # - events list input
        # - year int input
        # - month int input, month > 12
        # - day int input, day in [1, 31]
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date(events, 2022, 13, 23)
        
        # - events list input
        # - year int input
        # - month None/no input
        # - day int input, day in [1, 31]
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date(events, 2022, day=23)
        
        # - events list input
        # - year int input
        # - month other type input
        # - day int input, day in [1, 31]
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date(events, 2022, "9", 23)
        
        # - events list input
        # - year int input
        # - month int input, month in [1, 12]
        # - day int input, day < 1
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date(events, 2022, 9, 0)

        # - events list input
        # - year int input
        # - month int input, month in [1, 12]
        # - day int input, day > 31
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date(events, 2022, 9, 32)
        
        # - events list input
        # - year int input
        # - month int input, month in [1, 12]
        # - day other type input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.get_events_date(events, 2022, 9, "23")
        
        # Functionality
        # Year input, no month input, no day input: all events in the year are returned
        self.assertEqual([event.get_body() for event in MyEventManager.get_events_date(events, 2022)], [
            Event(Time(2022, 7, 8, 0, 0), Time(2022, 7, 8, 23, 59), attendees, "test date 8/7/2022", description, location, reminders, "4qs1bavmra1i74c7dojvlovdsc").get_body(),
            Event(Time(2022, 7, 20, 0, 0), Time(2022, 7, 20, 23, 59), attendees, "test date 20/7/2022", description, location, reminders, "tir7t1dfse2qoppsfosh0q16jk").get_body(),
            Event(Time(2022, 3, 18, 0, 0), Time(2022, 3, 18, 23, 59), attendees, "test date 18/3/2022", description, location, reminders, "h9jp2o34um9jj57hqpubneg52c").get_body()
        ])

        # Year input, month input, no day input: all events in the month in the year are returned
        self.assertEqual([event.get_body() for event in MyEventManager.get_events_date(events, 2022, 7)], [
            Event(Time(2022, 7, 8, 0, 0), Time(2022, 7, 8, 23, 59), attendees, "test date 8/7/2022", description, location, reminders, "4qs1bavmra1i74c7dojvlovdsc").get_body(),
            Event(Time(2022, 7, 20, 0, 0), Time(2022, 7, 20, 23, 59), attendees, "test date 20/7/2022", description, location, reminders, "tir7t1dfse2qoppsfosh0q16jk").get_body()
        ])

        # Year input, month input, day input: all events in the day in the month in the year are returned
        self.assertEqual([event.get_body() for event in MyEventManager.get_events_date(events, 2021, 7, 8)], [
            Event(Time(2021, 7, 8, 0, 0), Time(2021, 7, 8, 23, 59), attendees, "test date 8/7/2021 (1)", description, location, reminders, "5kff1ufh2fukdedh2l76h58lf0").get_body(),
            Event(Time(2021, 7, 8, 0, 0), Time(2021, 7, 8, 23, 59), attendees, "test date 8/7/2021 (2)", description, location, reminders, "sdht6j4bwsbvosugbetoi23obv").get_body()
        ])
    

    # Testing get_time_now() using patch
    @patch("MyEventManager.datetime")
    def test_get_time_now(self, mock_time):
        # Current time is 13:59 UTC (23:59 Melbourne time) (off-point boundary condition)
        mock_time.utcnow = Mock(return_value=datetime.datetime(2022, 9, 23, hour=13, minute=59))
        time_now = MyEventManager.get_time_now()
        self.assertEqual(time_now.get_object(), Time(2022, 9, 23, 23, 59).get_object())

        # Current time is 14:00 UTC (00:00 next day Melbourne time) (on-point boundary condition)
        mock_time.utcnow = Mock(return_value=datetime.datetime(2022, 9, 23, hour=14, minute=0))
        time_now = MyEventManager.get_time_now()
        self.assertEqual(time_now.get_object(), Time(2022, 9, 24, 0, 0).get_object())
    

    '''
    Testing coverter functions.

    Tests the functionality, preconditions and return result of the following functions:
    - time_to_Time()
    - attendee_to_Attendee()
    - organiser_to_Organiser()
    - location_to_Location()
    - reminder_to_Reminder()
    - event_to_Event()

    Most of these function are tested to maximise path coverage.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_converters(self):
        # Testing time_to_Time()
        # str input, where +10:00 will not change the day/month/year (Pass)
        self.assertEqual(MyEventManager.time_to_Time("2022-09-23T12:33:00.000000Z").get_object(), Time(2022, 9, 23, 22, 33).get_object())

        # str input, where +10:00 will be the next day (Pass)
        self.assertEqual(MyEventManager.time_to_Time("2022-09-24T23:00:00.000000Z").get_object(), Time(2022, 9, 25, 9, 0).get_object())

        # str input, where +10:00 will be the next month (Pass)
        self.assertEqual(MyEventManager.time_to_Time("2022-09-30T23:00:00.000000Z").get_object(), Time(2022, 10, 1, 9, 0).get_object())

        # str input, where +10:00 will be the next year (Pass)
        self.assertEqual(MyEventManager.time_to_Time("2022-12-31T23:00:00.000000Z").get_object(), Time(2023, 1, 1, 9, 0).get_object())

        # Non-str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.time_to_Time(20220923123300000000)
        

        # Testing attendee_to_Attendee()
        # Testing inputs
        # dict input, email absent (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.attendee_to_Attendee({
                'organizer': False,
                'self': False
            })
        
        # Non-dict input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.attendee_to_Attendee("Way to go Spidey")
        
        # Path coverage tests
        # dict input, 'email' present, 'organizer' present, 'organizer': True, 'self' present, 'self': True, 'responseStatus' present (Pass)
        attendee = MyEventManager.attendee_to_Attendee({
            'email': "ayan0024@student.monash.edu",
            'organizer': True,
            'self': True,
            'responseStatus': "accepted"
        })
        self.assertEqual(attendee.get_email(), "ayan0024@student.monash.edu")
        self.assertEqual(attendee.get_organiser(), True)
        self.assertEqual(attendee.get_is_self(), True)
        self.assertEqual(attendee.response_status, "accepted")

        # dict input, 'email' present, 'organizer' present, 'organizer': True, 'self' present, 'self': True, 'responseStatus' absent (Pass)
        attendee = MyEventManager.attendee_to_Attendee({
            'email': "ayan0024@student.monash.edu",
            'organizer': True,
            'self': True
        })
        self.assertEqual(attendee.get_email(), "ayan0024@student.monash.edu")
        self.assertEqual(attendee.get_organiser(), True)
        self.assertEqual(attendee.get_is_self(), True)
        self.assertEqual(attendee.response_status, "needsAction")

        # dict input, 'email' present, 'organizer' present, 'organizer': False, 'self' present, 'self': False, 'responseStatus' present (Pass)
        attendee = MyEventManager.attendee_to_Attendee({
            'email': "ayan0024@student.monash.edu",
            'organizer': False,
            'self': False,
            'responseStatus': "accepted"
        })
        self.assertEqual(attendee.get_email(), "ayan0024@student.monash.edu")
        self.assertEqual(attendee.get_organiser(), False)
        self.assertEqual(attendee.get_is_self(), False)
        self.assertEqual(attendee.response_status, "accepted")

        # dict input, 'email' present, 'organizer' absent, 'self' absent, 'responseStatus' present (Pass)
        attendee = MyEventManager.attendee_to_Attendee({
            'email': "ayan0024@student.monash.edu",
            'responseStatus': "accepted"
        })
        self.assertEqual(attendee.get_email(), "ayan0024@student.monash.edu")
        self.assertEqual(attendee.get_organiser(), False)
        self.assertEqual(attendee.get_is_self(), False)
        self.assertEqual(attendee.response_status, "accepted")
        

        # Testing organiser_to_Organiser()
        # Testing inputs
        # dict input, email present (Pass)
        self.assertEqual(MyEventManager.organiser_to_Organiser({
            'email': "ayan0024@student.monash.edu",
            'self': True
        }).get_object(), Organiser("ayan0024@student.monash.edu", True).get_object())

        # dict input, email absent (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.organiser_to_Organiser({
                'self': True
            })
        
        # Non-dict input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.organiser_to_Organiser("Pizza time!")
        
        # Path coverage tests
        # dict input, email present, 'self' present, 'self': True (Pass)
        organiser = MyEventManager.organiser_to_Organiser({
            'email': "ayan0024@student.monash.edu",
            'self': True
        })
        self.assertEqual(organiser.get_email(), "ayan0024@student.monash.edu")
        self.assertEqual(organiser.get_is_self(), True)

        # dict input, email present, 'self' present, 'self': False (Pass)
        organiser = MyEventManager.organiser_to_Organiser({
            'email': "ayan0024@student.monash.edu",
            'self': False
        })
        self.assertEqual(organiser.get_email(), "ayan0024@student.monash.edu")
        self.assertEqual(organiser.get_is_self(), False)

        # dict input, email present, 'self' absent (Pass)
        organiser = MyEventManager.organiser_to_Organiser({
            'email': "ayan0024@student.monash.edu"
        })
        self.assertEqual(organiser.get_email(), "ayan0024@student.monash.edu")
        self.assertEqual(organiser.get_is_self(), False)
        

        # Testing location_to_Location()
        # str input (Pass)
        location = Location()
        location.init_address("17", "Test Street", "TEST WAVERLEY", "TESTORIA", "3333", "TESTRALIA")
        self.assertEqual(MyEventManager.location_to_Location("17 Test Street\nTEST WAVERLEY TESTORIA 3333\nTESTRALIA").get_object(), location.get_object())

        # Non-str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.location_to_Location(395729)
        

        # Testing reminder_to_Reminder()
        # dict input, method present, minutes present (Pass)
        self.assertEqual(MyEventManager.reminder_to_Reminder({
            'method': "email",
            'minutes': 25
        }).get_object(), Reminder("email", 25).get_object())

        # dict input, method missing, minutes present (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.reminder_to_Reminder({
                'minutes': 25
            })
        
        # dict input, method present, minutes missing (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.reminder_to_Reminder({
                'method': "email"
            })
        
        # Non-dict input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.reminder_to_Reminder(92749)
        

        # Testing event_to_Event()
        # dict input, all entries present (Pass)
        starting_time = Time(2022, 10, 23, 9, 00)
        ending_time = Time(2022, 10, 23, 12, 0)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        location = Location()
        location.init_address("3", "Test Ave", "TESTVILLE", "NTS", "8888", "TESTNA")
        reminders = [Reminder("popup", 5), Reminder("email", 15)]
        event_id = "lu9ar5jcrpovcp5omk8s321m8g"
        self.assertEqual(MyEventManager.event_to_Event(
            {'kind': 'calendar#event', 'etag': '"3327661707043000"', 'id': 'lu9ar5jcrpovcp5omk8s321m8g', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=bHU5YXI1amNycG92Y3A1b21rOHMzMjFtOGcgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T07:14:13.000Z', 'updated': '2022-09-22T07:14:13.633Z', 'summary': 'test summary', 'description': 'test description', 'location': '3 Test Ave\nTESTVILLE NTS 8888\nTESTNA', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2022-10-22T23:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-10-23T02:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'lu9ar5jcrpovcp5omk8s321m8g@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'jlia0058@student.monash.edu', 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 5}, {'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ).get_body(), Event(starting_time, ending_time, attendees, "test summary", "test description", location, reminders, event_id).get_body())

        # dict input, no entries present (except event_id) (Pass)
        self.assertEqual(MyEventManager.event_to_Event({
            'id': "lu9ar5jcrpovcp5omk8s321m8g"
        }).get_body(), Event(None, None, None, None, None, None, None, "lu9ar5jcrpovcp5omk8s321m8g").get_body())

        # dict input, no entries present, except for reminders ('overrides': True) (and event_id) (Pass)
        self.assertEqual(MyEventManager.event_to_Event({
            'reminders': {
                'useDefault': False,
                'overrides': [{
                        'method': 'popup',
                        'minutes': 5
                    }, {
                        'method': "email",
                        'minutes': 15
                    }
                ]
            },
            'id': "lu9ar5jcrpovcp5omk8s321m8g"
        }).get_body(), Event(None, None, None, None, None, None, reminders, event_id).get_body())

        # dict input, no entries present, except for reminders ('overrides': False) (and event_id) (Pass)
        self.assertEqual(MyEventManager.event_to_Event({
            'reminders': {
                'useDefault': True
            },
            'id': "lu9ar5jcrpovcp5omk8s321m8g"
        }).get_body(), Event(None, None, None, None, None, None, None, event_id).get_body())

        # dict input, missing event_id (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.event_to_Event({'kind': 'calendar#event', 'etag': '"3327661707043000"', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=bHU5YXI1amNycG92Y3A1b21rOHMzMjFtOGcgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T07:14:13.000Z', 'updated': '2022-09-22T07:14:13.633Z', 'summary': 'test summary', 'description': 'test description', 'location': '3 Test Ave\nTESTVILLE NTS 8888\nTESTNA', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2022-10-22T23:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-10-23T02:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'lu9ar5jcrpovcp5omk8s321m8g@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'jlia0058@student.monash.edu', 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 5}, {'method': 'email', 'minutes': 15}]}, 'eventType': 'default'})
        
        # Non-dict input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.event_to_Event(35082364)
    

    '''
    Testing check_self_organiser().

    Tests the functionality, preconditions and return result of the function.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_check_self_organiser(self):
        starting_time = Time(2022, 10, 23, 9, 00)
        ending_time = Time(2022, 10, 23, 12, 0)
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        location = Location()
        location.init_address("3", "Test Ave", "TESTVILLE", "NTS", "8888", "TESTNA")
        reminders = [Reminder("popup", 5), Reminder("email", 15)]
        event_id = "lu9ar5jcrpovcp5omk8s321m8g"
        event = Event(starting_time, ending_time, attendees, "test summary", "test description", location, reminders, event_id)

        # Testing inputs
        # Non-Event input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.check_self_organiser("Joe's 29 minute guarantee is a promise, man")

        # Functionality
        # Event has no organiser (somehow)
        self.assertEqual(MyEventManager.check_self_organiser(event), True)

        # The user is the event organiser (event obtained from api will have determined the organiser)
        event.set_organiser(Organiser("ayan0024@student.monash.edu", True))
        self.assertEqual(MyEventManager.check_self_organiser(event), True)

        # The user is not the event organiser (event obtained from api will have determined the organiser)
        event.set_organiser(Organiser("jlia0058@student.monash.edu"))
        self.assertEqual(MyEventManager.check_self_organiser(event), False)
    

    '''
    Testing test_search_phrase().

    Tests the functionality, preconditions and return result of the function.
    Testing was done to maximise path coverage.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_search_phrase(self):
        attendees = [Attendee("ayan0024@student.monash.edu", True, True), Attendee("jlia0058@student.monash.edu"), Attendee("zhua0097@student.monash.edu")]
        location = Location()
        location.init_address("17", "Test Drive", "TEST WAVERLEY", "TESTORIA", "3333", "TESTRALIA")
        reminders = [Reminder("email", 30), Reminder("popup", 10)]
        events = [
            Event(Time(2021, 7, 8, 0, 0), Time(2021, 7, 8, 23, 59), attendees, "birthday 2021", "someone's birthday in 2021", location, reminders, "5kff1ufh2fukdedh2l76h58lf0"),
            Event(Time(2022, 7, 8, 0, 0), Time(2022, 7, 8, 23, 59), attendees, "birthday 2022", "someone's birthday in 2022", location, reminders, "4qs1bavmra1i74c7dojvlovdsc"),
            Event(Time(2022, 7, 20, 0, 0), Time(2022, 7, 20, 23, 59), attendees, "a friend's gathering", "a gathering with a long time friend", location, reminders, "tir7t1dfse2qoppsfosh0q16jk"),
            Event(Time(2022, 3, 18, 0, 0), Time(2022, 3, 18, 23, 59), attendees, "brother's big day", "a day that my brother would celebrate", location, reminders, "h9jp2o34um9jj57hqpubneg52c"),
            Event(Time(2021, 8, 20, 0, 0), Time(2022, 8, 20, 23, 59), attendees, "day with mother", "a day that I would spend with my mum", location, reminders, "lu9ar5jcrpovcp5omk8s321m8g"),
            Event(Time(2021, 7, 8, 0, 0), Time(2021, 7, 8, 23, 59), attendees, "birthday 2021 (2)", "duplicate of someone's birthday in 2021", location, reminders, "sdht6j4bwsbvosugbetoi23obv"),
            Event(Time(2020, 3, 9, 0, 0), Time(2020, 3, 9, 23, 59), attendees, None, "an event description that has no event summary", location, reminders, "sdht6j4bwsbvosugbetoi23obv")
        ]

        # - events list input of non-Events
        # - phrase str input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.search_phrase([1, 2, 3], "birthday")
        
        # - events non-list input
        # - phrase str input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.search_phrase("test", "birthday")
        
        # - events list input of Events
        # - phrase non-str input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.search_phrase(events, 123)

        # - events list input of Events
        # - phrase str input
        # - (Pass)

        # Functionality
        # events is a list of events, event has a summary, phrase is in the summary
        self.assertEqual([event.get_body() for event in MyEventManager.search_phrase(events, "birthday")], [Event(Time(2021, 7, 8, 0, 0), Time(2021, 7, 8, 23, 59), attendees, "birthday 2021", "someone's birthday in 2021", location, reminders, "5kff1ufh2fukdedh2l76h58lf0").get_body(), Event(Time(2022, 7, 8, 0, 0), Time(2022, 7, 8, 23, 59), attendees, "birthday 2022", "someone's birthday in 2022", location, reminders, "4qs1bavmra1i74c7dojvlovdsc").get_body(), Event(Time(2021, 7, 8, 0, 0), Time(2021, 7, 8, 23, 59), attendees, "birthday 2021 (2)", "duplicate of someone's birthday in 2021", location, reminders, "sdht6j4bwsbvosugbetoi23obv").get_body()])    

        # events is a list of events, event has a summary, phrase is not in the summary, event has a description, phrase is in the description
        self.assertEqual([event.get_body() for event in MyEventManager.search_phrase(events, "gathering")], [Event(Time(2022, 7, 20, 0, 0), Time(2022, 7, 20, 23, 59), attendees, "a friend's gathering", "a gathering with a long time friend", location, reminders, "tir7t1dfse2qoppsfosh0q16jk").get_body()])

        # events is a list of events, event has no summary, event has a description, phrase is in the description
        self.assertEqual([event.get_body() for event in MyEventManager.search_phrase(events, "no event summary")], [Event(Time(2020, 3, 9, 0, 0), Time(2020, 3, 9, 23, 59), attendees, None, "an event description that has no event summary", location, reminders, "sdht6j4bwsbvosugbetoi23obv").get_body()])

        # events is a list of events, event has no summary, event has a description, phrase is not in the description
        # events is a list of events, event has no summary and no description
        self.assertEqual([event.get_body() for event in MyEventManager.search_phrase(events, "no results for this search phrase")], [])

    '''
    Testing the passing cases of import_events().

    Tests the functionality, preconditions and return result of the function.
    patch was used to simulate the opening of files.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    # str input, .json ending (Pass)
    @patch("MyEventManager.json.load")
    @patch("MyEventManager.open")
    def test_import_events_passes(self, mock_open, mock_json_load):
        mock_json_load.return_value = {'data': [
            {'start': {'dateTime': '2022-09-20T02:11:00Z', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00Z', 'timeZone': 'Australia/Melbourne'}, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'response_status': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'organizer': False, 'self': False, 'response_status': 'needsAction'}], 'summary': 'test event', 'description': 'testing a test event with this description', 'location': 'www.google.com.au', 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'id': '5kff1ufh2fukdedh2l76h58lf0'}, 
            {'start': {'dateTime': '2022-09-22T01:37:00Z', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00Z', 'timeZone': 'Australia/Melbourne'}, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': False, 'self': True, 'response_status': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'organizer': False, 'self': False, 'response_status': 'needsAction'}], 'summary': 'test event', 'description': 'testing a test event with this description', 'location': '3 Test Ave\nTEST WAVERLEY TST 3333\nTESTRALIA', 'reminders': {'useDefault': True}, 'id': '4qs1bavmra1i74c7dojvlovdsc'}
        ]}
        events_json = MyEventManager.import_events("mocked_file.json")

        location1 = Location()
        location1.init_link("www.google.com.au")
        location2 = Location()
        location2.init_address("3", "Test Ave", "TEST WAVERLEY", "TST", "3333", "TESTRALIA")
        events = [
            Event(Time(2022, 9, 20, 12, 11), Time(2022, 12, 25, 22, 0), [Attendee("ayan0024@student.monash.edu", True, True), Attendee("zhua0097@student.monash.edu")], "test event", "testing a test event with this description", location1, [Reminder("email", 15)], "5kff1ufh2fukdedh2l76h58lf0"),
            Event(Time(2022, 9, 22, 11, 37), Time(2022, 12, 25, 22, 0), [Attendee("ayan0024@student.monash.edu", False, True), Attendee("zhua0097@student.monash.edu")], "test event", "testing a test event with this description", location2, None, "4qs1bavmra1i74c7dojvlovdsc")
        ]
        self.assertEqual([event.get_body() for event in events_json], [event.get_body() for event in events])
    

    '''
    Testing the fail cases of import_events().

    Tests the functionality, preconditions and return result of the function.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_import_events_fails(self):        
        # Non-str input (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.import_events(123)
    

    '''
    Testing the passing cases of export_events().

    Tests the functionality, preconditions and return result of the function.
    patch was used to simulate the opening of files.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    # - events list input of Events
    # - filename str input, .json ending
    # - (Pass)
    @patch("MyEventManager.open")
    def test_export_events_passes(self, mocked_open):
        filename = "mocked_file.json"
        location1 = Location()
        location1.init_link("www.google.com.au")
        location2 = Location()
        location2.init_address("3", "Test Ave", "TEST WAVERLEY", "TST", "3333", "TESTRALIA")
        events = [
            Event(Time(2022, 9, 20, 12, 11), Time(2022, 12, 25, 22, 0), [Attendee("ayan0024@student.monash.edu", True, True), Attendee("zhua0097@student.monash.edu")], "test event", "testing a test event with this description", location1, [Reminder("email", 15)], "5kff1ufh2fukdedh2l76h58lf0"),
            Event(Time(2022, 9, 22, 11, 37), Time(2022, 12, 25, 22, 0), [Attendee("ayan0024@student.monash.edu", False, True), Attendee("zhua0097@student.monash.edu")], "test event", "testing a test event with this description", location2, None, "4qs1bavmra1i74c7dojvlovdsc")
        ]
        MyEventManager.export_events(events, filename)
        mocked_open.assert_called_with(filename, "w")
    

    '''
    Testing the fail cases of export_events().

    Tests the functionality, preconditions and return result of the function.
    patch was used to simulate the opening of files.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_export_events_fails(self):
        location1 = Location()
        location1.init_link("www.google.com.au")
        location2 = Location()
        location2.init_address("3", "Test Ave", "TEST WAVERLEY", "TST", "3333", "TESTRALIA")
        events = [
            Event(Time(2022, 9, 20, 12, 11), Time(2022, 12, 25, 22, 0), [Attendee("ayan0024@student.monash.edu", True, True), Attendee("zhua0097@student.monash.edu")], "test event", "testing a test event with this description", location1, [Reminder("email", 15)], "5kff1ufh2fukdedh2l76h58lf0"),
            Event(Time(2022, 9, 22, 11, 37), Time(2022, 12, 25, 22, 0), [Attendee("ayan0024@student.monash.edu", False, True), Attendee("zhua0097@student.monash.edu")], "test event", "testing a test event with this description", location2, None, "4qs1bavmra1i74c7dojvlovdsc")
        ]

        # - events list input of non-Events
        # - filename str input, .json ending
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.export_events([1, 2, 3], "test.json")
        
        # - events non-list input
        # - filename str input, .json ending
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.export_events("test", "test.json")
        
        # - events list input of Events
        # - filename str input, not .json ending
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.export_events(events, "test")
        
        # - events list input of Events
        # - filename non-str input
        with self.assertRaises(ValueError):
            MyEventManager.export_events(events, 123)
    

    '''
    Testing transfer_organiser().

    Tests the functionality, preconditions and return result of the function.
    Mocking was used to mock the api.

    Testing strategies in MyEventManagerTest_Testing_Plan.md.
    '''
    def test_transfer_organiser(self):
        mock_api = Mock()

        # Testing inputs
        # - Non-Event input
        # - Organiser input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.transfer_organiser(mock_api, "all these test cases are destroying my brain", Organiser("ayan0024@student.monash.edu", True))
        
        # - Event input
        # - Non-Organiser input
        # - (Fail)
        with self.assertRaises(ValueError):
            MyEventManager.transfer_organiser(mock_api, Event(None, None, None, None, None, None, None, "97rtcn83ige9273"), "pls send help :(")
        
        # Functionality
        events_api = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'jlia0058@student.monash.edu', 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api
        events = []
        for i in range(len(events_api)):
            events.append(MyEventManager.event_to_Event(events_api[i]))
        self.assertEqual(events_api, mock_api.events().list(calendarId='primary').execute().get('items', []))

        events_api_updated = [
            {'kind': 'calendar#event', 'etag': '"3327135783671000"', 'id': '5kff1ufh2fukdedh2l76h58lf0', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NWtmZjF1ZmgyZnVrZGVkaDJsNzZoNThsZjAgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2021-09-19T06:11:31.000Z', 'updated': '2021-09-19T06:11:32.343Z', 'summary': 'test event 1', 'description': 'testing a test event with this description 1', 'location': 'www.google.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'start': {'dateTime': '2021-10-20T02:11:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2021-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '5kff1ufh2fukdedh2l76h58lf0@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477257624000"', 'id': '4qs1bavmra1i74c7dojvlovdsc', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=NHFzMWJhdm1yYTFpNzRjN2RvanZsb3Zkc2MgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:08.000Z', 'updated': '2022-09-21T05:37:08.812Z', 'summary': 'test event 2', 'description': 'testing a test event with this description 2', 'location': '5 Test Rd\nTEST SUBURB VIC 3150\nAUSTRALIA', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-22T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': '4qs1bavmra1i74c7dojvlovdsc@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'accepted'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'declined'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327477352524000"', 'id': 'tir7t1dfse2qoppsfosh0q16jk', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=dGlyN3QxZGZzZTJxb3Bwc2Zvc2gwcTE2amsgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-21T05:37:55.000Z', 'updated': '2022-09-21T05:37:56.262Z', 'summary': 'test event 3', 'description': 'testing a test event with this description 3', 'location': '2 Test Ave\nTESTURB VIC 3150\nTEST COUNTRY', 'creator': {'email': 'jlia0058@student.monash.edu'}, 'organizer': {'email': 'jlia0058@student.monash.edu'}, 'start': {'dateTime': '2022-09-23T01:37:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2022-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'tir7t1dfse2qoppsfosh0q16jk@google.com', 'sequence': 0, 'attendees': [{'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'ayan0024@student.monash.edu', 'self': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': True}, 'eventType': 'default'}, 
            {'kind': 'calendar#event', 'etag': '"3327617215755000"', 'id': 'h9jp2o34um9jj57hqpubneg52c', 'status': 'confirmed', 'htmlLink': 'https://www.google.com/calendar/event?eid=aDlqcDJvMzR1bTlqajU3aHFwdWJuZWc1MmMgYXlhbjAwMjRAc3R1ZGVudC5tb25hc2guZWR1', 'created': '2022-09-22T01:03:27.000Z', 'updated': '2022-09-22T01:03:28.397Z', 'summary': 'test event 4', 'description': 'testing a test event with this description 4', 'location': 'www.monash.zoom.com.au', 'creator': {'email': 'ayan0024@student.monash.edu', 'self': True}, 'organizer': {'email': 'jlia0058@student.monash.edu', 'self': False}, 'start': {'dateTime': '2025-09-22T21:03:00+10:00', 'timeZone': 'Australia/Melbourne'}, 'end': {'dateTime': '2025-12-25T12:00:00+11:00', 'timeZone': 'Australia/Melbourne'}, 'iCalUID': 'h9jp2o34um9jj57hqpubneg52c@google.com', 'sequence': 0, 'attendees': [{'email': 'ayan0024@student.monash.edu', 'organizer': False, 'self': True, 'responseStatus': 'needsAction'}, {'email': 'jlia0058@student.monash.edu', 'organizer': True, 'responseStatus': 'needsAction'}, {'email': 'zhua0097@student.monash.edu', 'responseStatus': 'needsAction'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 15}]}, 'eventType': 'default'}
        ]
        events_test = events.copy()
        events_test[3].transfer_ownership(Organiser("jlia0058@student.monash.edu"))
        mock_api.events.return_value.list.return_value.execute.return_value.get.return_value = events_api_updated

        MyEventManager.transfer_organiser(mock_api, events[3], Organiser("jlia0058@student.monash.edu"))
        self.assertEqual(events_api_updated, mock_api.events().list(calendarId='primary').execute().get('items', []))
        self.assertEqual(events[3].get_organiser().get_object(), Organiser("jlia0058@student.monash.edu").get_object())
        self.assertEqual(events[3].get_attendees()[0].get_organiser(), False)
        self.assertEqual(events[3].get_attendees()[1].get_organiser(), True)


def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(MyEventManagerTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
main()
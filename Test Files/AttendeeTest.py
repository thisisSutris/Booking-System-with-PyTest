import unittest
from unittest.mock import MagicMock, Mock, patch
from Attendee import Attendee


class AttendeeTest(unittest.TestCase):
    '''
    Testing __init__():
    
    Tests the functionality of the __init__ method of Attendee.py.
    Testing strategies found in AttendeeTest_Testing_Plan.md.
    '''
    def test_init(self):
        # email str input, organiser bool, is_self bool (Pass)
        attendee = Attendee("ayan0024@student.monash.edu", False, True)
        self.assertEqual(attendee.email, "ayan0024@student.monash.edu")
        self.assertEqual(attendee.organiser, False)
        self.assertEqual(attendee.is_self, True)

        # email str input, organiser Non-bool input, is_self No input (Fail)
        with self.assertRaises(ValueError):
            Attendee("jlia0058@student.monash.edu", "hello there")

        # email str input, organiser No input, is_self Non-bool input (Fail)
        with self.assertRaises(ValueError):
            Attendee("zhua0097@student.monash.edu", is_self=[1,2,3])

        # email str Non-str input, organiser bool, is_self bool (Fail)
        with self.assertRaises(ValueError):
            Attendee(37456293, True, True)

        # email str Non-str input, organiser Non-bool input, is_self No input (Fail)
        with self.assertRaises(ValueError):
            Attendee(2.718281828459045, {1,2,3})

        # email str Non-str input, organiser No input, is_self Non-bool input (Fail)
        with self.assertRaises(ValueError):
            Attendee(False, is_self="general kenobi")
    

    '''
    Testing accessors:
    
    Tests the functionalities of the accessor methods in Attendee.py.
    Tests:
    - get_email()
    - get_organiser()
    - get_is_self()

    Testing strategies found in AttendeeTest_Testing_Plan.md.
    '''
    def test_accessors(self):
        attendee = Attendee("ayan0024@student.monash.edu", False, True)

        # Testing get_email()
        self.assertEqual(attendee.get_email(), "ayan0024@student.monash.edu")

        # Testing get_organiser()
        self.assertEqual(attendee.get_organiser(), False)

        # Testing get_is_self()
        self.assertEqual(attendee.get_is_self(), True)
    

    '''
    Testing mutators:
    
    Tests the functionalities of the mutators methods in Attendee.py.
    Tests:
    - set_email()
    - set_organiser()
    - set_is_self()
    
    Testing strategies found in AttendeeTest_Testing_Plan.md.
    '''
    def test_mutators(self):
        attendee = Attendee("ayan0024@student.monash.edu", False, True)

        # Testing set_email()
        # - email str input, correct email is set (Pass)
        attendee.set_email("jlia0058@student.monash.edu")
        self.assertEqual(attendee.email, "jlia0058@student.monash.edu")
        
        # - email Non-str input (Fail)
        with self.assertRaises(ValueError):
            attendee.set_email(3.14159265359)
        
        # Testing set_organiser()
        # - organiser bool input, correct status is set (Pass)
        attendee.set_organiser(True)
        self.assertEqual(attendee.organiser, True)
        
        # - organiser Non-str input (Fail)
        with self.assertRaises(ValueError):
            attendee.set_organiser("you are a bold one")

        # Testing set_response_status()
        # - Valid response status is given, correct status is set
        attendee.set_response_status("needsAction")
        self.assertEqual(attendee.response_status, "needsAction")

        # - Invalid response status is given, error is thrown
        with self.assertRaises(ValueError):
            attendee.set_response_status("kill him")
        
        # - Non-str input is given, error is thrown
        with self.assertRaises(ValueError):
            attendee.set_response_status(9.8067)
    

    '''
    Testing actions:
    
    Tests the functionalities of methods that perform actions in Attendee.py.
    Tests:
    - accept_invitation()
    - decline_invitation()
    
    Testing strategies found in AttendeeTest_Testing_Plan.md.
    '''
    def test_actions(self):
        attendee = Attendee("ayan0024@student.monash.edu", False, True)

        # Testing accept_invitation()
        attendee.accept_invitation()
        self.assertEqual(attendee.response_status, "accepted")

        # Testing decline_invitation
        attendee.decline_invitation()
        self.assertEqual(attendee.response_status, "declined")


    '''
    Testing get_object():
    
    Tests the functionality of the get_object() method in Attendee.py and checks that the correct result is returned.
    
    Testing strategies found in AttendeeTest_Testing_Plan.md.
    '''
    def test_get_object(self):
        attendee = Attendee("ayan0024@student.monash.edu", False, True)
        self.assertEqual(attendee.get_object(), {
                'email': "ayan0024@student.monash.edu",
                'organizer': False,
                'self': True,
                'response_status': "needsAction"
            }
        )
    

    # Testing __str__()
    '''
    Testing __str__:
    
    Tests the functionality of the string method in Attendee.py and checks that the correct string is returned.
    
    Testing strategies found in AttendeeTest_Testing_Plan.md.
    '''
    def test_str(self):
        attendee = Attendee("ayan0024@student.monash.edu", False, True)
        self.assertEqual(str(attendee), "ayan0024@student.monash.edu")


def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(AttendeeTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
main()
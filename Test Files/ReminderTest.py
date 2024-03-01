import unittest
from Reminder import Reminder


class ReminderTestCase(unittest.TestCase):
    def test_init(self):
        reminder = Reminder("email", 50)
        # method is a str and can only be either "email" or "popup"
        self.assertIn(reminder.method, ["email", "popup"])
        # minutes before Event must be int
        self.assertEqual(reminder.minutes, 50)

        reminder2 = Reminder("popup", 20)
        # method is a str and can only be either "email" or "popup"
        self.assertIn(reminder2.method, ["email", "popup"])
        # minutes before Event must be int
        self.assertEqual(reminder2.minutes, 20)

        # method wrong value input, minutes valid input
        with self.assertRaises(ValueError):
            reminder = Reminder("phone call", 50)
        # method valid input, minutes invalid input
        with self.assertRaises(TypeError):
            reminder = Reminder("email", "50")
        # method wrong type, minutes valid inputs
        with self.assertRaises(TypeError):
            reminder = Reminder(60, 60)
        # method valid input,  minutes invalid int inputs with non-positive integer
        with self.assertRaises(ValueError):
            reminder = Reminder("email", -10)


    def test_accessors(self):
        reminder = Reminder("email", 60)
        # test get_method()
        self.assertEqual(reminder.get_method(), "email")
        # test get_minutes()
        self.assertEqual(reminder.get_minutes(), 60)

    def test_mutators(self):
        reminder = Reminder("email", 60)
        # test set_method()
        # happy path with valid input (Pass)
        reminder.set_method("popup")
        self.assertEqual(reminder.method, "popup")
        # invalid str input for method (Fail)
        with self.assertRaises(ValueError):
            reminder.set_method("phone call")
        # invalid type for method input (Fail)
        with self.assertRaises(TypeError):
            reminder.set_method(3.4)
        # test set_minutes()
        # happy path with positive int input (Pass)
        reminder.set_minutes(10)
        self.assertEqual(reminder.minutes, 10)
        # non-positive int input (Fail)
        with self.assertRaises(ValueError):
            reminder.set_minutes(0)
        # non-int input (Fail)
        with self.assertRaises(TypeError):
            reminder.set_minutes("20")



        # test set_minutes()
        # happy path with valid input
        reminder.set_minutes(20)
        self.assertEqual(reminder.minutes, 20)
        # invalid type of input
        with self.assertRaises(TypeError):
            reminder.set_minutes("20")
        # invalid input value
        with self.assertRaises(ValueError):
            reminder.set_minutes(-10)

    def test_get_objects(self):
        reminder = Reminder("email", 60)
        self.assertEqual(reminder.get_object(), {
            'method': 'email',
            'minutes': 60
        })

    def test_str(self):
        reminder = Reminder("email", 60)
        self.assertEqual(str(reminder), "Method: " + "email" + ", Minutes before: " + str(60))


def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(ReminderTestCase)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
main()
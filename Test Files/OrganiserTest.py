import unittest
from Organiser import Organiser


class OrganiserTestCase(unittest.TestCase):

    # Test __init__()
    def test_init(self):
        # call init method with input of is_self
        organiser = Organiser("zhua0097@student.monash.edu", True)
        self.assertEqual(organiser.email, "zhua0097@student.monash.edu")
        self.assertEqual(organiser.is_self, True)
        # call init method without input of is_self
        organiser2 = Organiser("jlia0058@student.monash.edu")
        self.assertEqual(organiser2.email, "jlia0058@student.monash.edu")

        # email str input, is_self non-bool input (Fail)
        with self.assertRaises(TypeError):
            Organiser("zhua0097@student.monash.edu", [2])
        # email non-str input, is_self bool input (Fail)
        with self.assertRaises(TypeError):
            Organiser(23, False)
        # email non-str input, is_self no input (Fail)
        with self.assertRaises(TypeError):
            Organiser([12,34])

    def test_accessors(self):
        organiser = Organiser("zhua0097@student.monash.edu", True)
        # test get_email
        self.assertEqual(organiser.get_email(), "zhua0097@student.monash.edu")
        # test get_is_self
        self.assertEqual(organiser.get_is_self(), True)

    def test_mutators(self):
        organiser = Organiser("jlia0058@student.monash.edu", False)
        # test set_email
        organiser.set_email("ayan0024@student.monash.edu")
        self.assertEqual(organiser.email, "ayan0024@student.monash.edu")
        # wrong input type
        with self.assertRaises(TypeError):
            organiser.set_email([23])

    def test_get_object(self):
        organiser = Organiser("zhua0097@student.monash.edu", True)
        self.assertEqual(organiser.get_object(), {
            'email': "zhua0097@student.monash.edu",
            'self': True,
        })





def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(OrganiserTestCase)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
main()
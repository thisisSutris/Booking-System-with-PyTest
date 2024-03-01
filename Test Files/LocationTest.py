import unittest
from Location import Location


class LocationTest(unittest.TestCase):

    def test_init_address(self):
        location = Location()
        # street number, street name, suburb, state, postcode, country
        location.init_address("10", "Clayton Road", "Clayton", "Victoria", "3173", "Australia")
        # street number has to be integer
        self.assertEqual(location.street_number, "10")
        self.assertEqual(location.street_name, "Clayton Road")
        self.assertEqual(location.suburb, "Clayton")
        self.assertEqual(location.state, "Victoria")
        self.assertEqual(location.postcode, "3173")
        self.assertEqual(location.country, "Australia")

        # street number not str.
        with self.assertRaises(TypeError):
            location.init_address(32, "Clayton Road", "Clayton", "Victoria", "3173", "Australia")

        # street name not str
        with self.assertRaises(TypeError):
            location.init_address("10", 3.1415926535897932384626, "Clayton", "Victoria", "3173", "Australia")

        # suburb not str.
        with self.assertRaises(TypeError):
            location.init_address("10", "Clayton Road", {1, 6}, "Victoria", "3173", "Australia")

        # state not str.
        with self.assertRaises(TypeError):
            location.init_address("10", "Clayton Road", "Clayton", [3], "3173", "Australia")

        # postcode not str.
        with self.assertRaises(TypeError):
            location.init_address("10", "Clayton Road", "Clayton", "Victoria", None, "Australia")

        # country not str.
        with self.assertRaises(TypeError):
            location.init_address("10", "Clayton Road", "Clayton", "Victoria", "3173", [2, [3]])

    def test_init_link(self):
        location = Location()
        location.init_link("https://my.monash/campusm/home#menu")
        self.assertEqual(location.get_link(), "https://my.monash/campusm/home#menu")

        # link not str
        with self.assertRaises(TypeError):
            location.init_link(12)

    def test_accessors(self):
        # type 1 of location
        l1 = Location()
        l1.init_address("10", "Clayton Road", "Clayton", "Victoria", "3173", "Australia")
        # test get_street_number
        self.assertEqual(l1.get_street_number(), "10")
        # test get_street_name
        self.assertEqual(l1.get_street_name(), "Clayton Road")
        # test get_suburb
        self.assertEqual(l1.get_suburb(), "Clayton")
        # test get_state
        self.assertEqual(l1.get_state(), "Victoria")
        # test get_postcode
        self.assertEqual(l1.get_postcode(), "3173")
        # test get_country
        self.assertEqual(l1.get_country(), "Australia")

        # type 2 of location
        l2 = Location()
        l2.init_link("https://google.com.au")
        # test get_link
        self.assertEqual(l2.get_link(), "https://google.com.au")

    def test_mutators(self):
        location = Location()
        location.init_address("10", "Clayton Road", "Clayton", "Victoria", "3173", "Australia")

        # test set_street_number
        # street number is str (Pass)
        location.set_street_number("9")
        self.assertEqual(location.street_number, "9")
        # street number not str (Fail)
        with self.assertRaises(TypeError):
            location.set_street_number(9)

        # test set_street_name
        # street name is str (Pass)
        location.set_street_name("Blackburn Road")
        self.assertEqual(location.street_name, "Blackburn Road")
        # street name not str (Fail)
        with self.assertRaises(TypeError):
            location.set_street_name([3])

        # test set_suburb
        # suburb is str (Pass)
        location.set_suburb("Caulfield")
        self.assertEqual(location.suburb, "Caulfield")
        # suburb not str (Fail)
        with self.assertRaises(TypeError):
            location.set_suburb(3.1415926)

        # test set_state
        # state is str (Pass)
        location.set_state("NSW")
        self.assertEqual(location.state, "NSW")
        # state not str (Fail)
        with self.assertRaises(TypeError):
            location.set_state([])

        # test set_postcode
        # postcode is str (Pass)
        location.set_postcode("3150")
        self.assertEqual(location.postcode, "3150")
        # postcode not str (Fail)
        with self.assertRaises(TypeError):
            location.set_postcode(3150)

        # test set_country
        # country is str (Pass)
        location.set_country("Japan")
        self.assertEqual(location.country, "Japan")
        # country not str (Fail)
        with self.assertRaises(TypeError):
            location.set_country(["Japan"])

        l2 = Location()
        l2.init_link("https://baidu.com")
        # test set_link
        # link is str
        l2.set_link("https://bing.com")
        self.assertEqual(l2.link, "https://bing.com")
        # link not str
        with self.assertRaises(TypeError):
            l2.set_link(["https something"])

    def test_get_object(self):
        location = Location()
        location.init_address("10", "Clayton Road", "Clayton", "Victoria", "3173", "Australia")
        # test get object for address init
        self.assertEqual(location.get_object(),
                         "10 Clayton Road\nClayton Victoria 3173\nAustralia")

        location2 = Location()
        location2.init_link("https://baidu.com")
        # test get object for link init
        self.assertEqual(location2.get_object(), "https://baidu.com")

    def test_str(self):
        location = Location()
        location.init_address("10", "Clayton Road", "Clayton", "Victoria", "3173", "Australia")
        # test __str__ for address init
        self.assertEqual(str(location), "10 Clayton Road\nClayton Victoria 3173\nAustralia")

        location2 = Location()
        location2.init_link("https://baidu.com")
        self.assertEqual(str(location2), "https://baidu.com")


def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(LocationTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
main()
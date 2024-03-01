import unittest
from Time import Time


class TimeTestCase(unittest.TestCase):
    def test_init(self):
        time = Time(2022, 9, 23, 10, 54)
        # valid input for year
        self.assertEqual(time.year, 2022)
        # valid input for month
        self.assertEqual(time.month, 9)
        # valid input for day
        self.assertEqual(time.day, 23)
        # valid input for hour
        self.assertEqual(time.hour, 10)
        # valid input for minute
        self.assertEqual(time.minute, 54)
        # Invalid value for year (outside low boundary)
        with self.assertRaises(ValueError):
            time = Time(1941, 9, 23, 10, 54)
        # Invalid value for year (outside high boundary)
        with self.assertRaises(ValueError):
            time = Time(2051, 9, 23, 10, 54)
        # Invalid value for month (outside low boundary)
        with self.assertRaises(ValueError):
            time = Time(2022, 0, 23, 10, 54)
        # Invalid value for month (outside high boundary)
        with self.assertRaises(ValueError):
            time = Time(2022, 13, 23, 10, 54)
        # Invalid value for day (outside low boundary)
        with self.assertRaises(ValueError):
            time = Time(2022, 9, 0, 10, 54)
        # Invalid value for day (outside high boundary)
        with self.assertRaises(ValueError):
            time = Time(2022, 9, 32, 10, 54)
        # Invalid value for hour (outside low boundary)
        with self.assertRaises(ValueError):
            time = Time(2022, 9, 23, -1, 54)
        # Invalid value for hour (outside high boundary)
        with self.assertRaises(ValueError):
            time = Time(2022, 9, 23, 24, 54)
        # Invalid value for minute (low boundary)
        with self.assertRaises(ValueError):
            time = Time(2022, 9, 23, 10, -1)
        # Invalid value for minute (high boundary)
        with self.assertRaises(ValueError):
            time = Time(2022, 9, 23, 10, 60)

        # Invalid type for year
        with self.assertRaises(TypeError):
            time = Time("2022", 9, 23, 10, 54)
        # Invalid type for month
        with self.assertRaises(TypeError):
            time = Time(2022, "9", 23, 10, 54)
        # Invalid type for day
        with self.assertRaises(TypeError):
            time = Time(2022, 9, "23", 10, 54)
        # Invalid type for hour
        with self.assertRaises(TypeError):
            time = Time(2022, 9, 23, 0.2, 54)
        # Invalid type for minute
        with self.assertRaises(TypeError):
            time = Time(2022, 9, 23, 10, [54])

    def test_accessors(self):
        time = Time(2022, 9, 23, 10, 54)
        # test get_year()
        self.assertEqual(time.get_year(), 2022)
        # test get_month()
        self.assertEqual(time.get_month(), 9)
        # test get_day()
        self.assertEqual(time.get_day(), 23)
        # test get_hour()
        self.assertEqual(time.get_hour(), 10)
        # test get_minute()
        self.assertEqual(time.get_minute(), 54)

    def test_mutators(self):
        time = Time(2022, 9, 23, 10, 54)
        # test set_year()
        # valid value
        time.set_year(2050)
        self.assertEqual(time.year, 2050)
        # invalid value (outside low boundary)
        with self.assertRaises(ValueError):
            time.set_year(1949)
        # invalid value (outside high boundary)
        with self.assertRaises(ValueError):
            time.set_year(2051)
        # invalid type
        with self.assertRaises(TypeError):
            time.set_month("2022")

        # test set_month()
        # valid value
        time.set_month(1)
        self.assertEqual(time.month, 1)
        # invalid value (outside low boundary)
        with self.assertRaises(ValueError):
            time.set_month(0)
        # invalid value (outside high boundary)
        with self.assertRaises(ValueError):
            time.set_month(13)
        # invalid type
        with self.assertRaises(TypeError):
            time.set_month("12")

        # test set_day()
        # valid value
        time.set_day(28)
        self.assertEqual(time.day, 28)
        # invalid value (outside low boundary)
        with self.assertRaises(ValueError):
            time.set_day(0)
        # invalid value (outside high boundary)
        with self.assertRaises(ValueError):
            time.set_day(32)
        with self.assertRaises(TypeError):
            time.set_day("20")

        # test set_hour()
        # valid value
        time.set_hour(16)
        self.assertEqual(time.hour, 16)
        # invalid value (outside low boundary)
        with self.assertRaises(ValueError):
            time.set_hour(-1)
        # invalid value (outside high boundary)
        with self.assertRaises(ValueError):
            time.set_hour(24)
        with self.assertRaises(TypeError):
            time.set_hour("20")

        # test set_minute()
        # valid value
        time.set_minute(28)
        self.assertEqual(time.minute, 28)
        # invalid value (outside low boundary)
        with self.assertRaises(ValueError):
            time.set_minute(-1)
        # invalid value (outside high boundary)
        with self.assertRaises(ValueError):
            time.set_minute(60)
        with self.assertRaises(TypeError):
            time.set_minute("59")

    def test_get_object(self):
        time = Time(2022, 9, 23, 10, 54)
        self.assertEqual(time.get_object(), {
            'dateTime': '2022-09-23T10:54:00Z',
            'timeZone': 'Australia/Melbourne'
        })

    def test_str(self):
        time = Time(2022, 9, 23, 10, 54)
        self.assertEqual(str(time), "2022-09-23T10:54:00Z")



def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(TimeTestCase)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
main()
import unittest

from measurement_converter.Conversions import to_feet, to_meters, to_kilos, to_pounds, kelvin_to_celsius,\
    celsius_to_kelvin, to_secs, to_hrsmins

class MyTestCase(unittest.TestCase):
    def test_to_feet_integer(self):
        self.assertEqual(to_feet(1), ("3ft, 3.4in"))

    def test_to_feet_float(self):
        self.assertEqual(to_feet(2.2), ("7ft, 2.6in"))

    def test_to_meters_integer(self):
        self.assertEqual(to_meters(3), "0.91m")

    def test_to_meters_float(self):
        self.assertEqual(to_meters(3.28), "1.0m")

    def test_to_kilos_integer(self):
        self.assertEqual(to_kilos(1), "0.45kg")

    def test_to_kilos_float(self):
        self.assertEqual(to_kilos(2.2), "1.0kg")

    def test_to_pounds_integer(self):
        self.assertEqual(to_pounds(1), "2.2lbs")

    def test_to_pounds_float(self):
        self.assertEqual(to_pounds(2.5), "5.51lbs")

    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(5), "-268.15C")

    def test_kelvin_to_celsius_negative_returns_error(self):
        self.assertEqual(kelvin_to_celsius(-1), 'Error')

    def test_celsius_to_kelvin_positive(self):
        self.assertEqual(celsius_to_kelvin(0), "273.15K")

    def test_celsius_to_kelvin_negative(self):
        self.assertEqual(celsius_to_kelvin(-20), "253.15K")

    def test_celsius_to_kelvin_below_zero_kelvin_returns_error(self):
        self.assertEqual(celsius_to_kelvin(-280), 'Error')

    def test_to_secs_integer(self):
        self.assertEquals(to_secs(1), "60secs")

    def test_to_secs_float(self):
        self.assertEqual(to_secs(61.5), "3690.0secs")

    def test_to_hrsmins_mins_only(self):
        self.assertEqual(to_hrsmins(60), "0hrs, 1mins, 0secs")

    def test_to_hrsmins_hours_only(self):
        self.assertEqual(to_hrsmins(3600), "1hrs, 0mins, 0secs")

    def test_to_hrsmins_float(self):
        self.assertEqual(to_hrsmins(3660.5), "1hrs, 1mins, 0.5secs")

if __name__ == '__main__':
    unittest.main()

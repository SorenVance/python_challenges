import unittest
from math import pi


def convert_radians_to_degrees(radians):
    return (180/pi)*radians


class RadianToDegreeConverterTests(unittest.TestCase):
    def test_converter_exists(self):
        self.assertEqual(286.4788975654116, convert_radians_to_degrees(5))


if __name__ == '__main__':
    unittest.main()
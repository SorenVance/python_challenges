import unittest

from value_format import is_float, is_int, format_value, is_exponential, space_ify_string


class MyTestCase(unittest.TestCase):
    def test_is_float(self):
        self.assertTrue(is_float('123'))
        self.assertTrue(is_float('-123'))
        self.assertTrue(is_float('123.456'))
        self.assertTrue(is_float('-123.456'))
        self.assertFalse(is_float('123a'))
        self.assertFalse(is_float('-123a'))
        self.assertFalse(is_float('1.23456e3'))
        self.assertFalse(is_float('--123.456'))
        self.assertTrue(is_float('  123  '))
        self.assertFalse(is_float('    123a'))
        self.assertFalse(is_float('123.456\n\n'))

    def test_is_int(self):
        self.assertTrue(is_int('123'))
        self.assertTrue(is_int('-123'))
        self.assertFalse(is_int('123a'))
        self.assertFalse(is_int('-123a'))
        self.assertFalse(is_int('123.456'))
        self.assertFalse(is_int('-123.456'))
        self.assertFalse(is_int('1.23456e3'))
        self.assertFalse(is_int('--123.456'))
        self.assertTrue(is_int('  123  '))
        self.assertFalse(is_int('    123a'))
        self.assertFalse(is_int('123.456\n\n'))

    def test_is_exponential(self):
        self.assertTrue(is_exponential('1.23456e3'))
        self.assertTrue(is_exponential('-1.23456e3'))
        self.assertTrue(is_exponential('1.23456e+3'))
        self.assertTrue(is_exponential('-1.23456e-3'))
        self.assertFalse(is_exponential('1.23456e'))
        self.assertFalse(is_exponential('-1.23456e'))
        self.assertFalse(is_exponential('1.23456e3a'))
        self.assertFalse(is_exponential('-1.23456e3a'))
        self.assertFalse(is_exponential('1.23456e+3a'))
        self.assertFalse(is_exponential('-1.23456'))
        self.assertTrue(is_exponential('  123  '))
        self.assertFalse(is_exponential('    123a'))
        self.assertFalse(is_exponential('123.456\n\n'))

    def test_format_value(self):
        self.assertIsNone(format_value(None))
        self.assertIsNotNone(format_value('None'))
        self.assertEqual(123, format_value('123'))
        self.assertEqual(-123, format_value('-123'))
        self.assertEqual(123.456, format_value('123.456'))
        self.assertEqual(-123.456, format_value('-123.456'))
        self.assertEqual('1.23456e3', format_value('1.23456e3'))
        self.assertEqual('1, 2, 3', format_value([1, 2, 3]))
        self.assertEqual(123, format_value('  123  '))
        self.assertEqual('123a', format_value('    123a'))
        self.assertEqual(123.456, format_value('123.456\n\n'))

    def test_space_ify_string(self):
        self.assertIsNone(space_ify_string(None))
        self.assertEqual('', space_ify_string(''))
        self.assertEqual('', space_ify_string(' '))
        self.assertEqual('lower', space_ify_string('lower'))
        self.assertEqual('UPPER', space_ify_string('UPPER'))
        self.assertEqual('Initial', space_ify_string('Initial'))
        self.assertEqual('dromedary Case', space_ify_string('dromedaryCase'))
        self.assertEqual('Camel Case', space_ify_string('CamelCase'))
        self.assertEqual('ABC Word DEF', space_ify_string('ABCWordDEF'))


if __name__ == '__main__':
    unittest.main()

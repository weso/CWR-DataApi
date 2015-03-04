# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import special


"""
Tests for IPI Base Number fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestIPIBaseNumberValid(unittest.TestCase):
    """
    Tests that the IPI Base Number accepts and parses valid values.
    """

    def setUp(self):
        self.ipi = special.ipi_base_number()

    def test_common(self):
        """
        Tests an average code.
        """
        code = 'I-000000229-7'

        result = self.ipi.parseString(code)[0]

        self.assertEqual('I', result.header)
        self.assertEqual(229, result.id_code)
        self.assertEqual(7, result.check_digit)

    def test_empty(self):
        """
        Tests an empty code.
        """
        code = '             '

        result = self.ipi.parseString(code)[0]

        self.assertEqual(None, result)

    def test_max(self):
        """
        Tests the highest possible value.
        """
        code = 'I-999999999-9'

        result = self.ipi.parseString(code)[0]

        self.assertEqual('I', result.header)
        self.assertEqual(999999999, result.id_code)
        self.assertEqual(9, result.check_digit)

    def test_min(self):
        """
        Tests the lowest possible value.
        """
        code = 'I-000000000-0'

        result = self.ipi.parseString(code)[0]

        self.assertEqual('I', result.header)
        self.assertEqual(0, result.id_code)
        self.assertEqual(0, result.check_digit)


class TestIPIBaseNumberCompulsoryValid(unittest.TestCase):
    """
    Tests that the IPI Base Number accepts and parses valid values.
    """

    def setUp(self):
        self.ipi = special.ipi_base_number(compulsory=True)

    def test_common(self):
        """
        Tests an average code.
        """
        code = 'I-000000229-7'

        result = self.ipi.parseString(code)[0]

        self.assertEqual('I', result.header)
        self.assertEqual(229, result.id_code)
        self.assertEqual(7, result.check_digit)

    def test_max(self):
        """
        Tests the highest possible value.
        """
        code = 'I-999999999-9'

        result = self.ipi.parseString(code)[0]

        self.assertEqual('I', result.header)
        self.assertEqual(999999999, result.id_code)
        self.assertEqual(9, result.check_digit)

    def test_min(self):
        """
        Tests the lowest possible value.
        """
        code = 'I-000000000-0'

        result = self.ipi.parseString(code)[0]

        self.assertEqual('I', result.header)
        self.assertEqual(0, result.id_code)
        self.assertEqual(0, result.check_digit)


class TestIPIBaseNumberException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.ipi = special.ipi_base_number()

    def test_no_numbers(self):
        """
        Tests that an exception is thrown when no numbers are set.
        """
        code = 'I-         - '

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_only_numbers_no_header(self):
        """
        Tests that an exception is thrown when only 10 numbers and no header are received.
        """
        code = '-999999999-9'

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_only_numbers(self):
        """
        Tests that an exception is thrown when 11 numbers are received.
        """
        code = '9-999999999-9'

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty
        """
        code = ''

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_too_short_empty(self):
        """
        Tests that an exception is thrown when the string is too short
        """
        code = '          '

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_too_short_no_check_digit(self):
        """
        Tests that an exception is thrown when the string is too short
        """
        code = 'T-999999999-'

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_too_short_id(self):
        """
        Tests that an exception is thrown when the string is too short
        """
        code = 'T-99999999-9'

        self.assertRaises(ParseException, self.ipi.parseString, code)


class TestIPIBaseNumberCompulsoryException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.ipi = special.ipi_base_number(compulsory=True)

    def test_no_numbers(self):
        """
        Tests that an exception is thrown when no numbers are set.
        """
        code = 'I-         - '

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_only_numbers_no_header(self):
        """
        Tests that an exception is thrown when only 10 numbers and no header are received.
        """
        code = '-999999999-9'

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_only_numbers(self):
        """
        Tests that an exception is thrown when 11 numbers are received.
        """
        code = '9-999999999-9'

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty
        """
        code = ''

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_too_empty(self):
        """
        Tests that an exception is thrown when the string is empty
        """
        code = '           '

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_too_short_no_check_digit(self):
        """
        Tests that an exception is thrown when the string is too short
        """
        code = 'T-999999999-'

        self.assertRaises(ParseException, self.ipi.parseString, code)

    def test_too_short_id(self):
        """
        Tests that an exception is thrown when the string is too short
        """
        code = 'T-99999999-9'

        self.assertRaises(ParseException, self.ipi.parseString, code)
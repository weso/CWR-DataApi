# -*- encoding: utf-8 -*-
import unittest

from cwr.parsing.grammar import field
from pyparsing import ParseException

"""
CWR file name parsing tests.

The following cases are tested:
- CWRFileNameDecoder decodes correctly formatted CWR file names (using both the old and new format)
- CWRFileNameDecoder decodes correctly formatted zip file file names (using both the old and new format)
- CWRFileNameEncoder encodes valid FileTags (using both the old and new format)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

class TestAlphanumValid(unittest.TestCase):
    """
    Tests that the alphanumeric field accepts and parse valid values.
    """

    def setUp(self):
        self.alpha = field.alphanum(5)

    def test_alphanum_full(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('ABCD1')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_full_only_number(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('12345')
        self.assertEqual('12345', result[0])

    def test_alphanum_full_only_letters(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('ABCDE')
        self.assertEqual('ABCDE', result[0])


    def test_alphanum_trailing_whites(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters and trailed by white spaces.
        """
        result = self.alpha.parseString('AB   ')
        self.assertEqual('AB', result[0])


    def test_alphanum_head_whites(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters and headed by white spaces.
        """
        result = self.alpha.parseString('   DE')
        self.assertEqual('DE', result[0])


    def test_alphanum_empty(self):
        """
        Tests that the alphanum field accepts an empty string of the correct number of characters.
        """
        result = self.alpha.parseString('     ')
        self.assertEqual('', result[0])

class TestNumericValid(unittest.TestCase):
    """
    Tests that the numeric field accepts and parse valid values.
    """

    def setUp(self):
        self.num = field.numeric(5)

    def test_numeric(self):
        """
        Tests that the numeric field accepts values of the correct number of characters.
        """
        result = self.num.parseString('12340')
        self.assertEqual(12340, result[0])

    def test_numeric_head_zeros(self):
        """
        Tests that the numeric field accepts values starting with zeros.
        """
        result = self.num.parseString('00123')
        self.assertEqual(123, result[0])

class TestNumericFloatValid(unittest.TestCase):
    """
    Tests that the numeric float field accepts and parse valid values.
    """

    def setUp(self):
        self.num = field.numeric_float(4,2)

    def test_numeric(self):
        """
        Tests that the numeric float field accepts values of the correct number of characters.
        """
        result = self.num.parseString('1234')
        self.assertEqual(12.34, result[0])

    def test_numeric_head_zeros(self):
        """
        Tests that the numeric float field accepts values starting with zeros.
        """
        result = self.num.parseString('0123')
        self.assertEqual(1.23, result[0])

    def test_numeric_tail_zeros(self):
        """
        Tests that the numeric float field accepts values ending with zeros.
        """
        result = self.num.parseString('1230')
        self.assertEqual(12.3, result[0])

class TestBooleanValid(unittest.TestCase):
    """
    Tests that the boolean field accepts and parse valid values.
    """

    def setUp(self):
        self.boolean = field.boolean_field

    def test_true(self):
        """
        Tests that the boolean field accepts true ('Y').
        """
        result = self.boolean.parseString('Y')
        self.assertEqual(True, result[0])

    def test_false(self):
        """
        Tests that the boolean field accepts false ('N').
        """
        result = self.boolean.parseString('N')
        self.assertEqual(False, result[0])

class TestFlagValid(unittest.TestCase):
    """
    Tests that the flag field accepts and parse valid values.
    """

    def setUp(self):
        self.flag = field.flag_field

    def test_true(self):
        """
        Tests that the boolean field accepts true ('Y').
        """
        result = self.flag.parseString('Y')
        self.assertEqual('Y', result[0])

    def test_false(self):
        """
        Tests that the boolean field accepts false ('N').
        """
        result = self.flag.parseString('N')
        self.assertEqual('N', result[0])

    def test_unknown(self):
        """
        Tests that the boolean field accepts unknown ('U').
        """
        result = self.flag.parseString('U')
        self.assertEqual('U', result[0])

class TestDateValid(unittest.TestCase):
    """
    Tests that the date field accepts and parse valid values.
    """

    def setUp(self):
        self.date = field.date_field

    def test_common(self):
        """
        Tests that the date field accepts a valid date.
        """
        result = self.date.parseString('20121121')[0]

        self.assertEqual(2012, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

    def test_small_year(self):
        """
        Tests that the date field accepts an uncommonly short year.
        """
        result = self.date.parseString('00121121')[0]

        self.assertEqual(12, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

class TestTimeValid(unittest.TestCase):
    """
    Tests that the date field accepts and parse valid values.
    """

    def setUp(self):
        self.time = field.time_field

    def test_common(self):
        """
        Tests that the time field accepts a valid time.
        """
        result = self.time.parseString('201510')[0]

        self.assertEqual(20, result.hour)
        self.assertEqual(15, result.minute)
        self.assertEqual(10, result.second)

    def test_max(self):
        """
        Tests that the time field accepts the highest possible time.
        """
        result = self.time.parseString('235959')[0]

        self.assertEqual(23, result.hour)
        self.assertEqual(59, result.minute)
        self.assertEqual(59, result.second)

    def test_min(self):
        """
        Tests that the time field accepts the lowest possible time.
        """
        result = self.time.parseString('000000')[0]

        self.assertEqual(0, result.hour)
        self.assertEqual(0, result.minute)
        self.assertEqual(0, result.second)

class TestAlphanumException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.alpha = field.alphanum(5)

    def test_alphanum_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.alpha.parseString, '')

    def test_alphanum_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'AB')

    def test_alphanum_wrong_no_caps(self):
        """
        Tests that an exception is thrown when the field is not using capitol letters.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'ABcDE')

class TestNumericException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.num = field.numeric(5)

    def test_numeric_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.num.parseString, '')

    def test_numeric_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.num.parseString, '123')

    def test_numeric_alphanumeric(self):
        """
        Tests that an exception is thrown when the field contains letters.
        """
        self.assertRaises(ParseException, self.num.parseString, '123ab')

class TestNumericFloatException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.num = field.numeric_float(4,2)

    def test_numeric_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.num.parseString, '')

    def test_numeric_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.num.parseString, '123')

    def test_numeric_alphanumeric(self):
        """
        Tests that an exception is thrown when the field contains letters.
        """
        self.assertRaises(ParseException, self.num.parseString, '123ab')

class TestBooleanException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.boolean = field.boolean_field

    def test_true_lower(self):
        """
        Tests that an exception is thrown when the true code is in lower letters.
        """
        self.assertRaises(ParseException, self.boolean.parseString, 'y')

    def test_false_lower(self):
        """
        Tests that an exception is thrown when the false code is in lower letters.
        """
        self.assertRaises(ParseException, self.boolean.parseString, 'n')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.boolean.parseString, '')

class TestFlagException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.flag = field.flag_field

    def test_true_lower(self):
        """
        Tests that an exception is thrown when the true code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'y')

    def test_false_lower(self):
        """
        Tests that an exception is thrown when the false code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'n')

    def test_unknown_lower(self):
        """
        Tests that an exception is thrown when the unknown code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'u')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.flag.parseString, '')

class TestDateException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.date = field.date_field

    def test_wrong_day(self):
        """
        Tests that an exception is thrown when the day is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121133')

    def test_wrong_month(self):
        """
        Tests that an exception is thrown when the month is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '201213112')

    def test_spaces_head(self):
        """
        Tests that an exception is thrown when the string is headed by empty spaces.
        """
        self.assertRaises(ParseException, self.date.parseString, ' 20121121')

    def test_spaces_letters(self):
        """
        Tests that an exception is thrown when the string contains letters.
        """
        self.assertRaises(ParseException, self.date.parseString, '201211XV')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.date.parseString, '')

class TestTimeException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.time = field.time_field

    def test_wrong_hour(self):
        """
        Tests that an exception is thrown when the hour is invalid.
        """
        self.assertRaises(ParseException, self.time.parseString, '241122')

    def test_wrong_minute(self):
        """
        Tests that an exception is thrown when the minute is invalid.
        """
        self.assertRaises(ParseException, self.time.parseString, '206022')

    def test_wrong_second(self):
        """
        Tests that an exception is thrown when the second is invalid.
        """
        self.assertRaises(ParseException, self.time.parseString, '203060')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.time.parseString, '')

    def test_spaces_head(self):
        """
        Tests that an exception is thrown when the string is headed by spaces.
        """
        self.assertRaises(ParseException, self.time.parseString, ' 203020')

    def test_too_short(self):
        """
        Tests that an exception is thrown when the string is too short.
        """
        self.assertRaises(ParseException, self.time.parseString, '03020')
# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic

"""
Tests for Alphanumeric (A) fields.

The following cases are tested (all tests are done for default and compulsory fields):

- Default name is set correctly
- Given name is set correctly
- Creating a new field does not change the existing ones names

- Accepts values with the correct number of characters
- Cuts strings which are longer than the required size
- Accepts values composed only of numbers
- Accepts values composed only of letters
- Accepts values trailed by whitespaces
- Accepts values headed by whitespaces.
- Accepts values surrounded by whitespaces
- Accepts values divided by whitespaces

- Accepts a string composed of whitespaces if it is not compulsory

- Accepts a string with non ASCII characters if it is extended

- Accepts a huge field with whitespaces
- Accepts a huge field with no whitespaces

- Accepts an empty string when the size is zero

- An exception is thrown when the columns are set as negative

- An exception is thrown when the field is empty and it shouldn't be
- An exception is thrown when the field is smaller than expected
- An exception is thrown when the field contains lowercase letters
- An exception is thrown when the field is not using capitol letters
- An exception is thrown when the field contains not ASCII characters
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAlphanumName(unittest.TestCase):
    """
    Tests that the Alphanumeric field name is set correctly.

    The following cases are tested:

    - Default name is set correctly
    - Given name is set correctly
    """

    def test_name_default(self):
        """
        Tests that the default field name is correct for optional fields.
        """
        field = basic.alphanum(5)

        self.assertEqual('Alphanumeric Field', field.name)

    def test_name_set(self):
        """
        Tests that the given field name is set correctly for optional fields.
        """
        name = "Field Name"
        field = basic.alphanum(5, name=name)

        self.assertEqual(name, field.name)

    def test_name_set_no_changes(self):
        """
        Tests that the field name does not change for creating a new one
        """
        field1 = basic.alphanum(5, name='field1')
        field2 = basic.alphanum(5, name='field2')

        self.assertEqual('field1', field1.name)
        self.assertEqual('field2', field2.name)


class _BaseAlphanumValid:
    """
    Base test for valid Alphanumeric fields.

    The following cases are tested:

    - Accepts values with the correct number of characters
    - Cuts strings which are longer than the required size
    - Accepts values composed only of numbers
    - Accepts values composed only of letters
    - Accepts values trailed by whitespaces
    - Accepts values headed by whitespaces.
    - Accepts values surrounded by whitespaces
    - Accepts values divided by whitespaces
    """

    def __init__(self):
        # A default field is created
        self.field = None

    def assertEqual(self, obj1, obj2):
        # To avoid warnings for not having this method
        pass

    def test_alphanum_full(self):
        """
        Tests that the alphanum field accepts values with the correct number of characters.
        """
        result = self.field.parseString('ABCD1')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_longer(self):
        """
        Tests that the alphanum field cuts strings which are longer than the required size.
        """
        result = self.field.parseString('ABCD1234')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_full_only_number(self):
        """
        Tests that the alphanum field accepts values composed only of numbers.
        """
        result = self.field.parseString('12345')
        self.assertEqual('12345', result[0])

    def test_alphanum_full_only_letters(self):
        """
        Tests that the alphanum field accepts values composed only of letters.
        """
        result = self.field.parseString('ABCDE')
        self.assertEqual('ABCDE', result[0])

    def test_alphanum_trailing_whites(self):
        """
        Tests that the alphanum field accepts values trailed by whitespaces.
        """
        result = self.field.parseString('AB   ')
        self.assertEqual('AB', result[0])

    def test_alphanum_head_whites(self):
        """
        Tests that the alphanum field accepts values headed by whitespaces.
        """
        result = self.field.parseString('   DE')
        self.assertEqual('DE', result[0])

    def test_alphanum_whites(self):
        """
        Tests that the alphanum field accepts values surrounded by whitespaces.
        """
        result = self.field.parseString('  C  ')
        self.assertEqual('C', result[0])

    def test_spaces_between(self):
        """
        Tests that the alphanum field accepts values divided by whitespaces.
        """
        result = self.field.parseString('AB CD')
        self.assertEqual('AB CD', result[0])


class TestAlphanumValid(unittest.TestCase, _BaseAlphanumValid):
    """
    Tests that the Alphanumeric field accepts and parse valid values.

    Implements the basic Alphanumeric test case for valid numbers.

    Adds the following cases:

    - Accepts a string composed of whitespaces
    """

    def setUp(self):
        self.field = basic.alphanum(5)


class TestAlphanumExtendedValid(unittest.TestCase, _BaseAlphanumValid):
    """
    Tests that the Alphanumeric field accepts and parse valid values.

    Implements the basic Alphanumeric test case for valid numbers.

    Adds the following cases:

    - Accepts a string composed of whitespaces
    - Accepts a string with non ASCII characters
    """

    def setUp(self):
        self.field = basic.alphanum(5, extended=True)

    def test_extended(self):
        """
        Tests that the alphanum field accepts a string with non ASCII characters.
        """
        text = 'AB\xc6\x8fC'
        result = self.field.parseString(text)
        self.assertEqual('AB\xc6\x8fC', result[0])


class TestAlphanumHugeValid(unittest.TestCase):
    """
    Tests that the Alphanumeric field accepts and parse very long valid values.

    The following cases are tested:
    - Accepts a huge field with whitespaces
    - Accepts a huge field with no whitespaces
    """

    def setUp(self):
        self.field = basic.alphanum(480)

    def test_common(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters containing whitespaces.
        """
        result = self.field.parseString(
            'THE NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ')
        self.assertEqual('THE NAME', result[0])

    def test_full(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters with no whitespaces.
        """
        result = self.field.parseString(
            'THEANAMEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(
            'THEANAMEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
            result[0])


class TestAlphanumEmptyValid(unittest.TestCase):
    """
    Tests that the Alphanumeric field accepts and parse valid values when empty.
    """

    def setUp(self):
        self.field = basic.alphanum(0)

    def test_alphanum_empty(self):
        """
        Tests that the alphanum field accepts an empty string.
        """
        result = self.field.parseString('')
        self.assertEqual('', result[0])


class TestAlphanumConstructorException(unittest.TestCase):
    """
    Tests that the Alphanumeric field constructor throws exceptions for erroneous values.

    Adds the following cases:

    - An exception is thrown when the columns are set as negative
    - An exception is thrown when the columns are set as zero
    """

    def test_cols_negative(self):
        """
        Tests that an exception is thrown when the columns are set as negative.
        """
        self.assertRaises(BaseException, basic.alphanum, -1)


class _BaseAlphanumException:
    """
    Base test for Alphanumeric fields exceptions.

    The following cases are tested:
    - An exception is thrown when the field is empty and it shouldn't be
    - An exception is thrown when the field is smaller than expected
    - An exception is thrown when the field contains lowercase letters
    - An exception is thrown when the field is not using capitol letters
    - An exception is thrown when the field contains not ASCII characters
    """

    def __init__(self):
        # A default field is created
        self.field = None

    def assertRaises(self, obj1, obj2, obj3):
        # To avoid warnings for not having this method
        pass

    def test_alphanum_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.field.parseString, '')

    def test_alphanum_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.field.parseString, 'AB')

    def test_alphanum_wrong_no_caps(self):
        """
        Tests that an exception is thrown when the field contains lowercase letters.
        """
        self.assertRaises(ParseException, self.field.parseString, 'ABcDE')

    def test_invalid_char(self):
        """
        Tests that an exception is thrown when the field contains not ASCII characters.
        """
        self.assertRaises(ParseException, self.field.parseString, 'AB\xc6\x8fE')


class TestAlphanumException(unittest.TestCase, _BaseAlphanumException):
    """
    Tests that exceptions are thrown when using invalid values

    Implements the basic Alphanumeric exception test case.
    """

    def setUp(self):
        self.field = basic.alphanum(5)


class TestAlphanumHugeException(unittest.TestCase, _BaseAlphanumException):
    """
    Tests that exceptions are thrown when using invalid values

    Implements the basic Alphanumeric exception test case.
    """

    def setUp(self):
        self.field = basic.alphanum(480)

    def test_empty(self):
        """
        Tests that the alphanum field accepts an empty string of the correct number of characters containing only
        whitespaces.
        """
        text = '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '
        self.assertRaises(ParseException, self.field.parseString, text)

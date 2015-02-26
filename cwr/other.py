# -*- encoding: utf-8 -*-

"""
Classes for other data structures.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class ISWCCode(object):
    def __init__(self, id_code, check_digit):
        self._id_code = id_code
        self._check_digit = check_digit

    def __str__(self):
        return 'ISWC T-%s-%s' % (self._printable_id_code(), self._check_digit)

    def __repr__(self):
        return '<class %s>(id_code=%r, check_digit=%r)' % ('ISWCCode', self._id_code, self._check_digit)

    def _printable_id_code(self):
        """
        Returns the code in a printable form, filling with zeros if needed.

        :return: the ID code in a printable form
        """
        code = str(self.id_code)
        while len(code) < 9:
            code = '0' + code

        return code

    @property
    def id_code(self):
        """
        Unique number for this ISWC.

        This is composed of up to nine digits.

        :return: the ISWC unique code
        """
        return self._id_code

    @property
    def check_digit(self):
        """
        Check digit for the ISWC code.

        This is composed of a single digit

        :return: the check digit
        """
        return self._check_digit
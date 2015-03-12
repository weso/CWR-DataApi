# -*- coding: utf-8 -*-

"""
Classes for other data structures.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class _ThreePartsCode(object):
    """
    Represents a code composed of a header, an ID and a check digit.

    These codes are used by CISAC for identification purposes.
    """

    _code_size = 9

    def __init__(self, header, id_code, check_digit):
        self._header = header
        self._id_code = id_code
        self._check_digit = check_digit

    def __str__(self):
        return '%s-%s-%s' % (self._header, self._printable_id_code(), self._check_digit)

    def __repr__(self):
        return '<class %s>(header=%r, id_code=%r, check_digit=%r)' % ('ThreePartsCode', self._header,
                                                                      self._id_code, self._check_digit)

    def _printable_id_code(self):
        """
        Returns the code in a printable form, filling with zeros if needed.

        :return: the ID code in a printable form
        """
        code = str(self.id_code)
        while len(code) < self._code_size:
            code = '0' + code

        return code

    @property
    def header(self):
        """
        The header identifying the type of code.

        This is a single character.

        :return: the header of the code
        """
        return self._header

    @property
    def id_code(self):
        """
        Identification code.

        This is usully composed of up to nine digits.

        :return: the ISWC unique code
        """
        return self._id_code

    @property
    def check_digit(self):
        """
        Check digit.

        This is composed of a single digit

        :return: the check digit
        """
        return self._check_digit


class ISWCCode(_ThreePartsCode):
    """
    Represents a ISWC Code.

    This stands for International Standard Musical Work Code, and are codes identifying a single musical work.

    It is composed of a prefix, nine digits identifying the work and a check digit.

    Currently the only prefix allowed is T, used to refer to musical works.
    """

    def __init__(self, id_code, check_digit):
        super(ISWCCode, self).__init__('T', id_code, check_digit)

    def __str__(self):
        return 'ISWC T-%s-%s' % (self._printable_id_code(), self._check_digit)

    def __repr__(self):
        return '<class %s>(id_code=%r, check_digit=%r)' % ('ISWCCode', self._id_code, self._check_digit)

    def _printable_id_code(self):
        """
        Returns the code in a printable form, separating it into groups of three characters using a point between them.

        :return: the ID code in a printable form
        """
        code = super(ISWCCode, self)._printable_id_code()

        code1 = code[:3]
        code2 = code[3:6]
        code3 = code[-3:]

        return '%s.%s.%s' % (code1, code2, code3)


class IPIBaseNumber(_ThreePartsCode):
    """
    Represents an IPI Base Number Code.

    IPI stands for Interested party information.

    These are codes identifying a party on a musical work transaction.

    It is composed of a prefix, nine digits identifying the party and a check digit.
    """

    def __init__(self, header, id_code, check_digit):
        super(IPIBaseNumber, self).__init__(header, id_code, check_digit)

    def __str__(self):
        return '%s-%s-%s' % (self.header, self._printable_id_code(), self.check_digit)

    def __repr__(self):
        return '<class %s>(header=%r, id_code=%r, check_digit=%r)' % ('IPIBaseNumber', self._header,
                                                                      self._id_code, self._check_digit)


class VISAN(object):
    """
    Represents a V-ISAN code.

    This is a variation on the ISAN (International Standard Audiovisual Number)
    """

    def __init__(self, version, isan, episode, check_digit):
        self._version = version
        self._isan = isan
        self._episode = episode
        self._check_digit = check_digit

    @property
    def check_digit(self):
        """
        Returns the check digit.

        :return: the check digit
        """
        return self._check_digit

    @property
    def episode(self):
        """
        Returns the episode number.
        :return: the episode number
        """
        return self._episode

    @property
    def isan(self):
        """
        Returns the ISAN code
        :return: the ISAN code
        """
        return self._isan

    @property
    def version(self):
        """
        Returns the version number.
        :return: the version number
        """
        return self._version


class AVIKey(object):
    """
    Represents an AVI key.
    """

    def __init__(self, society_code, av_number):
        self._society_code = society_code
        self._av_number = av_number

    @property
    def av_number(self):
        """
        Returns the audio-visual number.
        :return: the audio-visual number
        """
        return self._av_number

    @property
    def society_code(self):
        """
        Returns the society code.
        :return: the society code
        """
        return self._society_code
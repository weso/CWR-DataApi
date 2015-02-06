# -*- encoding: utf-8 -*-
from abc import ABCMeta

"""
Interested party model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class InterestedParty(object):
    """
    Represents a CWR interested party.
    """
    __metaclass__ = ABCMeta

    def __init__(self, ip_id, ip_name, ip_base_id):
        # IP info
        self._ip_id = ip_id
        self._ip_name = ip_name
        self._ip_base_id = ip_base_id

    @property
    def ip_base_id(self):
        """
        Interested Party Base Number field.

        This number is the unique identifier associated with this IP. The IP Base Number is a unique identifier
        allocated automatically by the IPI System to each interested party (IP), being either a natural person or legal
        entity. The number consists of 13 characters: letter i (I), hyphen (-), nine digits, hyphen (-), one
        check-digit. I-999999999-9. (weighted modulus 10, I weight = 2, adapted from ISO 7064). You can find more
        information in the CISAC web site.

        :return: the Publisher IP base number
        """
        return self._ip_base_id

    @property
    def ip_id(self):
        """
        Interested Party Number field.

        This is your unique numerical code for this IP. It is important that this number refer only to the
        publisher named on the registration. Never re-use an interested party number for a different publisher since
        this could cause the societies to merge the catalogue of the first publisher with the catalogue of the second
        publisher with the same interested party.

        :return: the Publisher's ID
        """
        return self._ip_id

    @property
    def ip_name(self):
        """
        Interested Party Name field.

        The unique identifier associated with this publisher name.

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the CAE number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the Published IP name
        """
        return self._ip_name


class Publisher(InterestedParty):
    """
    Represents a CWR Publisher.

    This encompasses several types of interested parties, such as sub-publisher, original publisher, acquirer or
    administrator.
    """

    def __init__(self, name, ip_id, ip_name, ip_base_id, tax_id):
        super(Publisher, self).__init__(ip_id, ip_name, ip_base_id)
        # General info
        self._name = name

        # Other info
        self._tax_id = tax_id

    @property
    def name(self):
        """
        Publisher Name field.

        The name of this publishing company as it is on file with its rights organization.

        For a publisher not under your control, it is not required to provide a name (see publisher_unknown_indicator).

        :return: the Publisher's name
        """
        return self._name

    @property
    def tax_id(self):
        """
        Tax ID number field.

        A number used to identify this publisher for tax reporting.

        :return: the Publisher's Tax ID
        """
        return self._tax_id


class Writer(InterestedParty):
    """
    Represents a CWR writer.
    """

    def __init__(self, first_name, personal_number, ip_id, ip_name, ip_base_id, last_name=None):
        super(Writer, self).__init__(ip_id, ip_name, ip_base_id)
        self._first_name = first_name
        self._last_name = last_name
        self._personal_number = personal_number

    @property
    def first_name(self):
        """
        Writer First Name field.

        The first name of the writer.

        :return: the Writer first name
        """
        return self._first_name

    @property
    def last_name(self):
        """
        Writer Last Name field.

        The last name of the writer. If you do not have the ability to separate the last name from the first name, then
        you may include both the last and first name in this field—pr separated by a comma. This field is mandatory for
        writers that you control.

        :return: the Writer last name
        """
        return self._last_name

    @property
    def personal_number(self):
        """
        Personal Number field.

        This field contains the personal number assigned to this individual in the country of residence. For Sweden, it
        has the format YYMMDD9999.

        :return: the Writer country-based personal number
        """
        return self._personal_number

class WriterPublisher(object):
    """
    Represents a relationship between a Writer and a Publisher.

    It is valuable for the societies to know the publisher associated with each writer. This provides a complete trail
    of the rights -- from the creator to the publisher to sub- publishers or administrators. For each writer who is
    under your control, complete one PWR record for each publisher to which they have assigned rights for this work.

    Some societies require that the society assigned agreement numbers be present in a work registration. The
    writer-to-publisher agreement numbers are recorded in this record. The reason is that if two or more writers for a
    work have an agreement with the same original publisher, it is possible to record each Society-Assigned Agreement
    Number and Submitter Agreement Number in the PWR record that links that writer to the original publisher.

    It is the society of the original publisher that assigns the society-assigned agreement number. The submitter
    agreement number is included in an agreement transaction (AGR) if it exists.
    """

    def __init__(self, publisher, writer, submitter_agreement, society_agreement=None):
        self._publisher = publisher
        self._writer = writer
        self._submitter_agreement = submitter_agreement
        self._society_agreement = society_agreement

    @property
    def publisher(self):
        """
        Publisher IP # field.

        This field contains the unique identifier of the publisher to whom this writer has assigned rights.

        :return: the Publisher's ID
        """
        return self._publisher

    @property
    def society_agreement(self):
        """
        Society Agreement # field.

        This field contains the agreement number assigned to this agreement by the society of the original publisher
        (if known).

        :return: the society's Agreement ID
        """
        return self._society_agreement

    @property
    def submitter_agreement(self):
        """
        Submitter Agreement # field.

        This field contains your unique number used to identify the agreement between the writer and publisher being
        linked.

        :return: the submitter's Agreement ID
        """
        return self._submitter_agreement

    @property
    def writer(self):
        """
        Writer IP # field.

        The writer interested party number pointing back to the writer in the immediately preceding SWR record in an
        explicit link.

        :return: the Writer's ID
        """
        return self._writer


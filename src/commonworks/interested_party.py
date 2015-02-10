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

    def __init__(self, ip_id, ip_name, ip_base_id, tax_id, cae_ipi_name):
        # IP info
        self._ip_id = ip_id
        self._ip_name = ip_name
        self._ip_base_id = ip_base_id

        # Other info
        self._tax_id = tax_id
        self._cae_ipi_name = cae_ipi_name

    @property
    def cae_ipi_name(self):
        """
        Publisher CAE/IPI Name # field.

        The CAE number assigned to this publisher with 2 leading zero’s or the IPI Name #.

        :return: the Publisher CAE/IPI name number
        """
        return self._cae_ipi_name

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

    @property
    def tax_id(self):
        """
        Tax ID number field.

        A number used to identify this publisher for tax reporting.

        :return: the Publisher's Tax ID
        """
        return self._tax_id


class Publisher(InterestedParty):
    """
    Represents a CWR Publisher.

    This encompasses several types of interested parties, such as sub-publisher, original publisher, acquirer or
    administrator.
    """

    def __init__(self, name, ip_id, ip_name, ip_base_id=None, tax_id=None, cae_ipi_name=None):
        super(Publisher, self).__init__(ip_id, ip_name, ip_base_id, tax_id, cae_ipi_name)
        # General info
        self._name = name

    @property
    def name(self):
        """
        Publisher Name field.

        The name of this publishing company as it is on file with its rights organization.

        For a publisher not under your control, it is not required to provide a name (see publisher_unknown_indicator).

        :return: the Publisher's name
        """
        return self._name


class Writer(InterestedParty):
    """
    Represents a CWR writer.

    This can be a Writer Controlled by Submitter (SWR) or Other Writer (OWR).
    """

    def __init__(self, ip_id, last_name, personal_number, ip_name, ip_base_id=None, first_name=None, tax_id=None,
                 cae_ipi_name=None, pr_affiliation=None, pr_ownership_share=None,
                 mr_affiliation=None, mr_ownership_share=None,
                 sr_affiliation=None, sr_ownership_share=None):
        super(Writer, self).__init__(ip_id, ip_name, ip_base_id, tax_id, cae_ipi_name)
        self._first_name = first_name
        self._last_name = last_name
        self._personal_number = personal_number

        # Shares
        self._pr_affiliation = pr_affiliation
        self._pr_ownership_share = pr_ownership_share
        self._mr_affiliation = mr_affiliation
        self._mr_ownership_share = mr_ownership_share
        self._sr_affiliation = sr_affiliation
        self._sr_ownership_share = sr_ownership_share

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

    @property
    def mr_affiliation(self):
        """
        MR Affiliation Society # field.

        Number assigned to the Mechanical Rights Society with which the writer is affiliated.

        These values reside on the Society Code Table.

        :return: the MR affiliation number
        """
        return self._mr_affiliation

    @property
    def mr_ownership_share(self):
        """
        MR Ownership Share field.

        Defines the percentage of the writer’s ownership of the mechanical rights to the work.
        Within an individual SPU record, this value can range from 0 to 100.0.

        :return: the MR ownership share
        """
        return self._mr_ownership_share

    @property
    def pr_affiliation(self):
        """
        PR Affiliation Society # field.

        Number assigned to the Performing Rights Society with which the writer is affiliated.

        These values reside on the Society Code Table.

        :return: the PR affiliation number
        """
        return self._pr_affiliation

    @property
    def pr_ownership_share(self):
        """
        PR Ownership Share field.

        Defines the percentage of the writer’s ownership of the performance rights to the work.  Within an individual
        SWR record, this value can range from 0 to 100.0.  Note that writers both own and collect the performing right
        interest.

        :return: the PR ownership share
        """
        return self._pr_ownership_share

    @property
    def sr_affiliation(self):
        """
        SR Affiliation Society # field.

        Number assigned to the Mechanical Rights Society with which the publisher is affiliated.

        These values reside on the Society Code Table.

        :return: the SR affiliation number
        """
        return self._pr_affiliation

    @property
    def sr_ownership_share(self):
        """
        SR Ownership Share field.

        Defines the percentage of the writer’s ownership of the synchronization rights to the work.

        Within an individual SPU record, this value can range from 0 to 100.0.

        :return: the SR ownership share
        """
        return self._sr_ownership_share

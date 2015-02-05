# -*- encoding: utf-8 -*-
from commonworks.entity import Entity

"""
Interested party model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class InterestedParty(Entity):
    """
    Represents a CWR interested party.
    """

    def __init__(self, submitter_id, cae_ipi_id, ipi_base_number, ipa_number, last_name, agreements=None):
        super(InterestedParty, self).__init__(submitter_id)
        self._cae_ipi_id = cae_ipi_id
        self._ipi_base_number = ipi_base_number
        self._ipa_number = ipa_number
        self._last_name = last_name

        if agreements is None:
            self._agreements = []
        else:
            self._agreements = agreements

    def add_agreement(self, agreement):
        self._agreements.append(agreement)

    def remove_agreement(self, agreement):
        self._agreements.remove(agreement)

    @property
    def agreements(self):
        return self._agreements

    @property
    def cae_ipi_id(self):
        return self._cae_ipi_id

    @property
    def ipa_number(self):
        return self._ipa_number

    @property
    def ipi_base_number(self):
        return self._ipi_base_number

    @property
    def last_name(self):
        return self._last_name


class Publisher(object):
    """
    Represents a CWR Publisher.

    This encompasses several types of interested parties, such as sub-publisher, original publisher, acquirer or
    administrator.
    """

    def __init__(self, name, ip_id, ip_name, ip_base_id, tax_id):
        # General info
        self._name = name

        # IP info
        self._ip_id = ip_id
        self._ip_name = ip_name
        self._ip_base_id = ip_base_id

        # Other info
        self._tax_id = tax_id

    @property
    def ip_base_id(self):
        """
        Publisher IP Base Number field.

        This number is the unique identifier associated with this publisher. The IP Base Number is a unique identifier
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

        This is your unique numerical code for this publisher. It is important that this number refer only to the
        publisher named on the registration. Never re-use an interested party number for a different publisher since
        this could cause the societies to merge the catalogue of the first publisher with the catalogue of the second
        publisher with the same interested party.

        :return: the Publisher's ID
        """
        return self._ip_id

    @property
    def ip_name(self):
        """
        Publisher IP Name field.

        The unique identifier associated with this publisher name.

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the CAE number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the Published IP name
        """
        return self._ip_name

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


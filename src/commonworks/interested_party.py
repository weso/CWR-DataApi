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
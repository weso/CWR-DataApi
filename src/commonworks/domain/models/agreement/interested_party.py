# -*- encoding: utf-8 -*-
from commonworks.domain.models.entity import Entity

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


class IPAAgreement(object):
    """
    Represents a CWR interested party agreement.
    """

    def __init__(self, agreement_id, agreement_role_code, pr_society, pr_share, mr_society,
                 mr_share, sr_society, sr_share):
        self._agreement_id = agreement_id
        self._agreement_role_code = agreement_role_code
        self._pr_society = pr_society
        self._pr_share = pr_share
        self._mr_society = mr_society
        self._mr_share = mr_share
        self._sr_society = sr_society
        self._sr_share = sr_share

    @property
    def agreement_id(self):
        return self._agreement_id

    @property
    def agreement_role_code(self):
        return self._agreement_role_code

    @property
    def mr_share(self):
        return self._mr_share

    @property
    def mr_society(self):
        return self._mr_society

    @property
    def pr_share(self):
        return self._pr_share

    @property
    def sr_share(self):
        return self._sr_share

    @property
    def pr_society(self):
        return self._pr_society

    @property
    def sr_society(self):
        return self._sr_society
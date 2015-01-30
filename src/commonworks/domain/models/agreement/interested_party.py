# -*- encoding: utf-8 -*-
from commonworks.domain.models.entity import Entity

"""
Interested party model classes.
"""

__author__ = 'Borja Garrido Bear'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class InterestedParty(Entity):
    """
    Represents a CWR interested party.
    """

    def __init__(self, submitter_id, cae_ipi_id, ipi_base_number, ipa_number, last_name,
    ):
        super(InterestedParty, self).__init__(submitter_id)
        self.cae_ipi_id = cae_ipi_id
        self.ipi_base_number = ipi_base_number
        self.ipa_number = ipa_number
        self.last_name = last_name
        self.agreements = []

    def add_agreement(self, agreement):
        self.agreements.append(agreement)


class IPAAgreement(object):
    """
    Represents a CWR interested party agreement.
    """

    def __init__(self, agreement_id, agreement_role_code, pr_society, pr_share, mr_society,
                 mr_share, sr_society, sr_share):
        self.agreement_id = agreement_id
        self.agreement_role_code = agreement_role_code
        self.pr_society = pr_society
        self.pr_share = pr_share
        self.mr_society = mr_society
        self.mr_share = mr_share
        self.sr_society = sr_society
        self.sr_share = sr_share
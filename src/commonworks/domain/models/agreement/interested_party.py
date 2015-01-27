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

    def __init__(self, submitter_id):
        super(InterestedParty, self).__init__(submitter_id)

    def add_agreement(self, agreement):
        self.agreements.append(agreement)


class IPAAgreement(object):
    """
    Represents a CWR interested party agreement.
    """

    def __init__(self, agreement_id):
        self.agreement_id = agreement_id
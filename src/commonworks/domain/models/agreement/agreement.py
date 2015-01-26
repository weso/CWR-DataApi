# -*- encoding: utf-8 -*-
from commonworks.domain.models.entity import Entity

"""
Agreement model classes.
"""

__author__ = 'Borja Garrido Bear'
__version__ = '0.0.0'
__status__ = 'Development'


class Agreement(Entity):
    """
    Represents a CWR agreement.
    """

    def __init__(self, submitter_id):
        super(Agreement, self).__init__(submitter_id)

    def add_interested_party(self, ipa_id):
        self.interested_parties.append(ipa_id)

    def add_territory(self, territory):
        self.territories.append(Territory(territory))


class Territory(object):
    """
    Represents a CWR agreement territory
    """

    def __init__(self):
        pass
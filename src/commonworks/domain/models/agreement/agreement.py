# -*- encoding: utf-8 -*-
from commonworks.domain.models.entity import Entity

"""
Agreement model classes.
"""

__author__ = 'Borja Garrido Bear'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Agreement(Entity):
    """
    Represents a CWR agreement.
    """

    def __init__(self, submitter_id, agreement_number, international_standard_number
                 , type, start_date, end_date, retention_end_date, prior_royalty_status,
                 prior_royalty_status_date, post_term_collection_status,
                 post_term_collection_end_date, signature_date,
                 works_number, sales_manufacture_clause, shares_change,
                 advance_given, society_assigned_number):
        super(Agreement, self).__init__(submitter_id)
        self.agreement_number = agreement_number
        self.international_standard_number = international_standard_number
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.retention_end_date = retention_end_date
        self.prior_royalty_status = prior_royalty_status
        self.prior_royalty_status_date = prior_royalty_status_date
        self.post_term_collection_status = post_term_collection_status
        self.post_term_collection_end_date = post_term_collection_end_date
        self.signature_date = signature_date
        self.works_number = works_number
        self.sales_manufacture_clause = sales_manufacture_clause
        self.shares_change = shares_change
        self.advance_given = advance_given
        self.society_assigned_number = society_assigned_number
        self.interested_parties = []
        self.territories = []

    def add_interested_party(self, ipa_id):
        self.interested_parties.append(ipa_id)

    def add_territory(self, territory):
        self.territories.append(AgreementTerritory(territory))


class AgreementTerritory(object):
    """
    Represents a CWR agreement territory
    """

    def __init__(self, inclusion_exclusion_indicator, tis_numeric_code):
        self.inclusion_exclusion_indicator = inclusion_exclusion_indicator
        self.tis_numeric_code = tis_numeric_code
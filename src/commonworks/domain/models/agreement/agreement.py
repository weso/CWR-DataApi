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
        self._agreement_number = agreement_number
        self._international_standard_number = international_standard_number
        self._type = type
        self._start_date = start_date
        self._end_date = end_date
        self._retention_end_date = retention_end_date
        self._prior_royalty_status = prior_royalty_status
        self._prior_royalty_status_date = prior_royalty_status_date
        self._post_term_collection_status = post_term_collection_status
        self._post_term_collection_end_date = post_term_collection_end_date
        self._signature_date = signature_date
        self._works_number = works_number
        self._sales_manufacture_clause = sales_manufacture_clause
        self._shares_change = shares_change
        self._advance_given = advance_given
        self._society_assigned_number = society_assigned_number

        self._interested_parties = []
        self._territories = []

    def add_interested_party(self, ipa):
        self._interested_parties.append(ipa)

    def add_territory(self, territory):
        self._territories.append(AgreementTerritory(territory))

    def remove_interested_party(self, ipa):
        self._interested_parties.remove(ipa)

    def remove_territory(self, territory):
        self._interested_parties.remove(territory)

    @property
    def agreement_number(self):
        return self._agreement_number

    @property
    def advance_given(self):
        return self._advance_given

    @property
    def end_date(self):
        return self._end_date

    @property
    def interested_parties(self):
        return self._interested_parties

    @property
    def international_standard_number(self):
        return self._international_standard_number

    @property
    def post_term_collection_end_date(self):
        return self._post_term_collection_end_date

    @property
    def post_term_collection_status(self):
        return self._post_term_collection_status

    @property
    def prior_royalty_status(self):
        return self._prior_royalty_status

    @property
    def prior_royalty_status_date(self):
        return self._prior_royalty_status_date

    @property
    def retention_end_date(self):
        return self._retention_end_date

    @property
    def sales_manufacture_clause(self):
        return self._sales_manufacture_clause

    @property
    def shares_change(self):
        return self._shares_change

    @property
    def signature_date(self):
        return self._signature_date

    @property
    def society_assigned_number(self):
        return self._society_assigned_number

    @property
    def start_date(self):
        return self._start_date

    @property
    def territories(self):
        return self._territories

    @property
    def type(self):
        return self._type

    @property
    def works_number(self):
        return self._works_number


class AgreementTerritory(object):
    """
    Represents a CWR agreement territory
    """

    def __init__(self, inclusion_exclusion_indicator, tis_numeric_code):
        self._inclusion_exclusion_indicator = inclusion_exclusion_indicator
        self._tis_numeric_code = tis_numeric_code

    @property
    def inclusion_exclusion_indicator(self):
        return self._inclusion_exclusion_indicator

    @property
    def tis_numeric_code(self):
        return self._tis_numeric_code
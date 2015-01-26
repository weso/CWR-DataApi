from abc import ABCMeta
from commonworks.domain.models.entity import Entity

__author__ = 'borja'


class Agreement(Entity):

    def __init__(self, submitter_id, json_item):
        super(Agreement, self).__init__(submitter_id)

        self.submitter_number = json_item['submitter_number']
        self.international_standard_number = json_item['international_standard_number']
        self.type = json_item['type']
        self.start_date = json_item['start_date']
        self.end_date = json_item['end_date']
        self.retention_end_date = json_item['retention_end_date']
        self.prior_royalty_status = json_item['prior_royalty_status']
        self.prior_royalty_status_date = json_item['prior_royalty_status_date']
        self.post_term_collection_status = json_item['post_term_collection_status']
        self.post_term_collection_end_date = json_item['post_term_collection_end_date']
        self.signature_date = json_item['signature_date']
        self.works_number = json_item['works_number']
        self.sales_manufacture_clause = json_item['sales_manufacture_clause']
        self.shares_change = json_item['shares_change']
        self.advance_given = json_item['advance_given']
        self.society_assigned_number = json_item['society_assigned_number']

        self.interested_parties = []
        self.territories = []

    def add_interested_party(self, ipa_id):
        self.interested_parties.append(ipa_id)

    def add_territory(self, territory):
        self.territories.append(Territory(territory))

    def to_mongo_dict(self):
        agreement_dict = {}

        agreement_dict['_id'] = self.creation_id
        agreement_dict['submitter_id'] = self.submitter_id
        agreement_dict['agreement_number'] = self.submitter_number
        agreement_dict['international_standard_number'] = self.international_standard_number
        agreement_dict['type'] = self.type
        agreement_dict['start_date'] = self.start_date
        agreement_dict['end_date'] = self.end_date
        agreement_dict['retention_end_data'] = self.retention_end_date
        agreement_dict['prior_royalty_status'] = self.prior_royalty_status
        agreement_dict['prior_royalty_status_date'] = self.prior_royalty_status_date
        agreement_dict['post_term_collection_status'] = self.post_term_collection_status
        agreement_dict['post_term_collection_end_date'] = self.post_term_collection_end_date
        agreement_dict['signature_date'] = self.signature_date
        agreement_dict['works_number'] = self.works_number
        agreement_dict['sales_manufacture_clause'] = self.sales_manufacture_clause
        agreement_dict['shares_change'] = self.shares_change
        agreement_dict['advance_given'] = self.advance_given
        agreement_dict['society_assigned_number'] = self.society_assigned_number

        agreement_dict['interested_parties'] = self.interested_parties
        agreement_dict['territories'] = []

        for territory in self.territories:
            agreement_dict['territories'].append(territory.to_mongo_dict())

        return agreement_dict


class Territory(object):

    def __init__(self, json_item):
        self.inclusion_exclusion_indicator = json_item['inclusion_exclusion_indicator']
        self.tis_numeric_code = json_item['tis_numeric_code']

    def to_mongo_dict(self):
        terrioty_dict = {}

        terrioty_dict['inclusion_exclusion_indicator'] = self.inclusion_exclusion_indicator
        terrioty_dict['tis_numeric_code'] = self.tis_numeric_code


class Repository(object):
    __metaclass__ = ABCMeta

    def find_agreement_by_id(self, agreement_id):
        pass

    def find_agreements_by_submitter(self, submitter_id):
        pass

    def find_agreements_by_submitter_id(self, submitter_id, agreement_number):
        pass

    def insert_agreement(self, agreement):
        pass
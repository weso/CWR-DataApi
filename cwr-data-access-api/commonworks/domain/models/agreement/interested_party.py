from abc import ABCMeta
from commonworks.domain.models.entity import Entity

__author__ = 'borja'


class InterestedParty(Entity):

    def __init__(self, submitter_id, json_item):
        super(InterestedParty, self).__init__(submitter_id)

        self.cae_ipi_id = json_item['cae_ipi_id']
        self.ipi_base_number = json_item['ipi_base_number']
        self.id = json_item['id']
        self.last_name = json_item['last_name']

        self.agreements = []

    def add_agreement(self, agreement_id, json_item):
        self.agreements.append(self.create_ipa_agreement(agreement_id, json_item))

    def to_mongo_dict(self):
        ipa_dict = {}

        ipa_dict['_id'] = self.creation_id
        ipa_dict['submitter_id'] = self.submitter_id

        ipa_dict['cae_ipi_id'] = self.cae_ipi_id
        ipa_dict['ipi_base_number'] = self.ipi_base_number
        ipa_dict['ipa_number'] = self.id
        ipa_dict['last_name'] = self.last_name

        ipa_dict['agreements'] = []

        for agreement in self.agreements:
            ipa_dict['agreements'].append(agreement.to_mongo_dict())

        return ipa_dict

    @staticmethod
    def create_ipa_agreement(agreement_id, json_item):
        return Agreement(agreement_id, json_item)


class Agreement(object):

    def __init__(self, agreement_id, json_item):
        self.agreement_id = agreement_id

        self.agreement_role_code = json_item['agreement_role_code']
        self.pr_society = json_item['pr_society']
        self.pr_share = json_item['pr_share']
        self.mr_society = json_item['mr_society']
        self.mr_share = json_item['mr_share']
        self.sr_society = json_item['sr_society']
        self.sr_share = json_item['sr_share']

    def to_mongo_dict(self):
        agr_dict = {}

        agr_dict['agreement_id'] = self.agreement_id
        agr_dict['role_code'] = self.agreement_role_code
        agr_dict['pr_society'] = self.pr_society
        agr_dict['pr_share'] = self.pr_share
        agr_dict['mr_society'] = self.mr_society
        agr_dict['mr_share'] = self.mr_share
        agr_dict['sr_society'] = self.sr_society
        agr_dict['sr_share'] = self.sr_share

        return agr_dict


class Repository(object):
    __metaclass__ = ABCMeta

    def find_ipa_by_id(self, ipa_id):
        pass

    def find_ipa_by_submitter(self, submitter_id):
        pass

    def find_ipa_by_submitter_id(self, submitter_id, ipa_id):
        pass

    def insert_ipa(self, ipa):
        pass
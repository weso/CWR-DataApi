from commonworks.domain.models.entity import Entity

__author__ = 'borja'


class Publisher(Entity):
    def __init__(self, submitter_id, json_item):
        super(Publisher, self).__init__(submitter_id)

        self.agreement_number = json_item['agreement_number']
        self.interested_party_id = json_item['interested_party_id']

        self.mongo_agreement_id = None
        self.mongo_ipa_id = None

    def to_mongo_dict(self):
        publisher_dict = {}

        publisher_dict['agreement_id'] = self.mongo_agreement_id
        publisher_dict['interested_party'] = self.mongo_ipa_id

        return publisher_dict
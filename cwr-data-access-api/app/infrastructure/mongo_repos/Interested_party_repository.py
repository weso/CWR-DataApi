from app.infrastructure.mongo_repos.generic_repository import GenericRepository
from commonworks.domain.models.agreement.interested_party import Repository

__author__ = 'borja'


class InterestedPartyRepository(GenericRepository, Repository):
    def __init__(self, url_root):
        super(InterestedPartyRepository, self).__init__(url_root, 'interested_parties')

    def find_ipa_by_submitter(self, submitter_id):
        ipas = list(self._db[self.collection].find({'submitter_id': submitter_id}))

        if ipas is None:
            return "Interested party not found not found"

        return ipas

    def find_ipa_by_submitter_id(self, submitter_id, ipa_id):
        ipa = self._db[self.collection].find_one({'submitter_id': submitter_id, 'ipa_number': ipa_id})

        return ipa

    def add_agreement(self, ipa_id, agreement):
        self._db[self.collection].update({'_id': ipa_id}, {'$push': {'agreements': agreement.to_mongo_dict()}}, True)
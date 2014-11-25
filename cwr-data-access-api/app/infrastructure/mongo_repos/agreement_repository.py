from app.infrastructure.mongo_repos.generic_repository import GenericRepository
from commonworks.domain.models.agreement.agreement import Repository

__author__ = 'borja'


class AgreementRepository(GenericRepository, Repository):
    def __init__(self, url_root):
        super(AgreementRepository, self).__init__(url_root, 'agreements')

    def find_agreements_by_submitter(self, submitter_id):
        agreements = list(self._db[self.collection].find({'submitter_id': int(submitter_id)}))

        if agreements is None:
            return "Agreement not found"

        return agreements

    def find_agreement_by_submitter_id(self, submitter_id, agreement_number):
        agreement = self._db[self.collection].find_one({'submitter_id': int(submitter_id), 'agreement_number': agreement_number})

        return agreement

    def find_agreements_by_ipa(self, ipa_id):
        agreements = list(self._db[self.collection].find({'interested_parties': ipa_id}))

        return agreements
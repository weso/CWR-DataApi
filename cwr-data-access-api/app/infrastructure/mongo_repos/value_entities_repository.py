from app.infrastructure.mongo_repos.generic_repository import GenericRepository
from commonworks.domain.models.agreement.agreement import Repository

__author__ = 'borja'


class ValueEntityRepository(GenericRepository, Repository):
    def __init__(self, url_root, collection):
        super(ValueEntityRepository, self).__init__(url_root, collection)
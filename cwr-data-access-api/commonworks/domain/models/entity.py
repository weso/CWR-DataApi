from abc import ABCMeta, abstractmethod
import uuid

__author__ = 'borja'


class Entity(object):
    __metaclass__ = ABCMeta

    def __init__(self, submitter_id):
        self._creation_id = uuid.uuid4().hex[:24]
        self._submitter_id = submitter_id

    @property
    def creation_id(self):
        return self._creation_id

    @property
    def submitter_id(self):
        return self._submitter_id

    @abstractmethod
    def to_mongo_dict(self):
        pass
# -*- encoding: utf-8 -*-
from commonworks.utils.dict_encoder import CWRDictionaryEncoder
from commonworks.entity import Entity

"""
Offers classes to create Mongo dictionaries from model objects.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class MongoDictionaryEncoder(CWRDictionaryEncoder):
    """
    Encodes CWR model classes into Mongo dictionaries.
    """

    def __init__(self):
        super(MongoDictionaryEncoder, self).__init__()

    def encode(self, d):
        encoded = super(MongoDictionaryEncoder, self).encode(d)

        if isinstance(d, Entity):
            encoded = self.__encode_entity(d, encoded)

        return encoded

    @staticmethod
    def __encode_entity(entity, encoded):
        encoded['_id'] = entity.creation_id

        return encoded
# -*- coding: utf-8 -*-

import json

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.parser.common import Encoder


"""
Offers classes to parse CWR objects from and into JSON structures.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class JSONEncoder(Encoder):
    def __init__(self):
        super(JSONEncoder, self).__init__()
        self._dict_encoder = CWRDictionaryEncoder()

    def encode(self, object):
        encoded = self._dict_encoder.encode(object)

        return json.dumps(encoded, default=_date_handler)


def _date_handler(obj):
    if hasattr(obj, 'isoformat'):
        result = obj.isoformat()
    else:
        raise TypeError("Unserializable object {} of type {}".format(obj,
                                                                     type(obj)))

    return result
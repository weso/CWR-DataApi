# -*- coding: utf-8 -*-

import json

from cwr.parser.common import Encoder
from cwr.parser.dictionary import CWRDictionaryEncoder


"""
Offers classes to parse CWR objects from and into JSON structures.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class JSONDecoder(Encoder):
    def __init__(self):
        super(JSONDecoder, self).__init__()
        self._dict_encoder = CWRDictionaryEncoder()

    def encode(self, object):
        encoded = self._dict_encoder.encode(object)

        return json.dumps(encoded, default=self._date_handler)

    def _date_handler(self, obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj
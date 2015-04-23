# -*- coding: utf-8 -*-

import json

from cwr.parser.dictionary import CWRDictionaryEncoder


"""
Offers classes to parse CWR objects from and into JSON structures.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class JSONEncoder(CWRDictionaryEncoder):
    def __init__(self):
        super(JSONEncoder, self).__init__()

    def encode(self, object):
        encoded = super(JSONEncoder, self).encode(object)

        return json.dumps(encoded, default=self._date_handler)

    def _date_handler(self, obj):

        if hasattr(obj, 'isoformat'):
            result = obj.isoformat()
        else:
            result = obj

        return result
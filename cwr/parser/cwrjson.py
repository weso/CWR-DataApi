# -*- coding: utf-8 -*-

import json

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.other import ISWCCode, VISAN


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
        elif isinstance(obj, ISWCCode):
            result = self.encode(obj)
        elif isinstance(obj, VISAN):
            result = self.encode(obj)
        else:
            result = obj

        return result
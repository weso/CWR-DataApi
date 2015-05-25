# -*- coding: utf-8 -*-

import json

from cwr.parser.decoder.common import Decoder
from cwr.parser.decoder.dictionary import FileDictionaryDecoder

"""
Classes for decoding CWR classes from JSON dictionaries.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class JSONDecoder(Decoder):
    def __init__(self):
        super(JSONDecoder, self).__init__()
        self._dict_decoder = FileDictionaryDecoder()

    def decode(self, data):
        decoded = json.loads(data)

        return self._dict_decoder.decode(decoded)

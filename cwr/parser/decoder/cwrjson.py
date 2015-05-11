# -*- coding: utf-8 -*-

from cwr.parser.decoder.common import Decoder

"""
Classes for decoding CWR classes from JSON dictionaries.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class JSONDecoder(Decoder):
    def __init__(self):
        super(JSONDecoder, self).__init__()

    def decode(self, data):
        pass
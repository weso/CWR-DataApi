# -*- coding: utf-8 -*-

import json

from cwr.parser.encoder.dictionary import CWRDictionaryEncoder
from cwr.parser.encoder.common import Encoder


"""
Classes for encoding CWR classes into dictionaries.

It just consists of a single parser, the JSONEncoder, which delegates most of the work to an instance of the
CWRDictionaryEncoder.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class JSONEncoder(Encoder):
    """
    Encodes a CWR class instance into a JSON.

    For this, first the instance is transformed into a dictionary, then dumped into a JSON.

    A bit of additional work is done for handling the dates, which are transformed into the ISO format.
    """

    def __init__(self):
        super(JSONEncoder, self).__init__()
        self._dict_encoder = CWRDictionaryEncoder()

    def encode(self, instance):
        """
        Encodes the data, creating a JSON structure from an instance from the domain model.

        :param instance: the instance to encode
        :return: a JSON structure created from the received data
        """
        encoded = self._dict_encoder.encode(instance)

        return json.dumps(encoded, ensure_ascii=False, default=_iso_handler, encoding='latin1')


def _unicode_handler(obj):
    """
    Transforms an unicode string into a UTF-8 equivalent.

    :param obj: object to transform into it's UTF-8 equivalent
    :return: the UTF-8 equivalent of the string
    """
    if isinstance(obj, str):
        result = obj.isoformat()
    else:
        raise TypeError("Unserializable object {} of type {}".format(obj,
                                                                     type(obj)))

    return result


def _iso_handler(obj):
    """
    Transforms an object into it's ISO format, if possible.

    If the object can't be transformed, then an error is raised for the JSON parser.

    This is meant to be used on datetime instances, but will work with any object having a method called isoformat.

    :param obj: object to transform into it's ISO format
    :return: the ISO format of the object
    """
    if hasattr(obj, 'isoformat'):
        result = obj.isoformat()
    else:
        raise TypeError("Unserializable object {} of type {}".format(obj,
                                                                     type(obj)))

    return result
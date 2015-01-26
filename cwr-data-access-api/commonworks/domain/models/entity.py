# -*- encoding: utf-8 -*-
from abc import ABCMeta
import uuid

"""
Base entity model classes.
"""

__author__ = 'Borja Garrido Bear'
__version__ = '0.0.0'
__status__ = 'Development'


class Entity(object):
    """
    Represents a base CWR entity.
    """
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
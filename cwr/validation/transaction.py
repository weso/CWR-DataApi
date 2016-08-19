# -*- coding: utf-8 -*-
from apt_pkg import __init__

from cwr.validation.common import Validation

"""
Base classes for implementing validation rules.

"""

__author__ = 'Yaroslav O. Golub'
__license__ = 'MIT'
__status__ = 'Development'


class ValidationTransaction(Validation):

    def __init__(self):
        pass

    def validate(self, transaction):
        pass



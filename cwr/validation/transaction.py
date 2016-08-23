# -*- coding: utf-8 -*-
from apt_pkg import __init__

from cwr.validation.common import Validation, ValidationStatus, ASValidationStatus

"""
Base classes for implementing validation rules.

"""

__author__ = 'Yaroslav O. Golub'
__license__ = 'MIT'
__status__ = 'Development'


class ValidationTransaction(Validation):

    config = None

    def __init__(self, config):
        self.config = config

    def validate(self, transaction):
        return ASValidationStatus()



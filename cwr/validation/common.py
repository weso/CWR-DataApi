# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

"""
Base classes for implementing validation rules.

"""

__author__ = 'Yaroslav O. Golub'
__license__ = 'MIT'
__status__ = 'Development'


class ValidationStatus(object):

    status = False

    message = []

    def __init__(self, code, message=''):
        self.code = code
        self.message = message


class Validation(object):
    """
    Interface for implementing validation. This is abstract class.
    """
    __metaclass__ = ABCMeta

    data = None

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def validate(self, entity):
        """
        Validate entity and return ValidationStatus

        :param entity: the instance to validate
        :return: ValidationStatus class
        """
        raise NotImplementedError('The validate method must be implemented')

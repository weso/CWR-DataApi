# -*- encoding: utf-8 -*-
from abc import ABCMeta

"""
Offers interfaces to create repositories for the CWR model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class AgreementRepository(object):
    """
    Repository for Agreement instances.
    """
    __metaclass__ = ABCMeta

    def find_agreement_by_id(self, agreement_id):
        pass

    def find_agreements_by_submitter(self, submitter_id):
        pass

    def find_agreements_by_submitter_id(self, submitter_id, agreement_number):
        pass

    def insert_agreement(self, agreement):
        pass


class InterestedPartyRepository(object):
    """
    Repository for InterestedParty instances.
    """
    __metaclass__ = ABCMeta

    def find_ipa_by_id(self, ipa_id):
        pass

    def find_ipa_by_submitter(self, submitter_id):
        pass

    def find_ipa_by_submitter_id(self, submitter_id, ipa_id):
        pass

    def insert_ipa(self, ipa):
        pass


class WorkRepository(object):
    """
    Repository for Work instances.
    """
    __metaclass__ = ABCMeta

    def find_work_by_id(self, work_id):
        pass

    def find_works_by_submitter(self, submitter_id):
        pass

    def find_works_by_submitter_id(self, submitter_id, work_number):
        pass

    def insert_work(self, work):
        pass
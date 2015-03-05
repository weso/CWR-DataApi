# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar import transaction

"""
CWR Test Work grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAcknowledgementTransactionValid(unittest.TestCase):
    def setUp(self):
        self.grammar = transaction.work_transaction

    def test_work_min(self):
        work = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        record = work

        result = self.grammar.parseString(record)

        self.assertEqual(1, len(result))

        self.assertEqual('NWR', result[0].record_type)

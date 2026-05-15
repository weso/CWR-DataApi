# -*- coding: utf-8 -*-

from cwr.record import TransactionRecord

"""
CWR 2.2 § 5.32 Work ID Cross Reference (XRF) record.

This record links a work transaction to identifiers issued by any organisation
including the intended recipient, other PROs, ISWC (org_code='ISW'), or ISRC
(org_code='ISR').

The XRF record is an optional trailing record inside NWR, REV, and ISW
transactions (see CWR 2.2 §6.1 BNF).
"""

__author__ = 'Rightstune'
__license__ = 'MIT'
__status__ = 'Development'


class XrfRecord(TransactionRecord):
    """CWR 2.2 § 5.32 Work ID Cross Reference (XRF).

    Field layout after the 19-char Record Prefix:
      organisation_code  3  alphanum  M
      identifier        14  alphanum  M
      identifier_type    1  alphanum  M  W=Work, R=Recording, P=Product, V=Video
      validity           1  alphanum  M  Y=valid, U=link invalid, N=identifier invalid
    """

    def __init__(self, transaction_sequence_n, record_sequence_n,
                 organisation_code, identifier,
                 identifier_type='W', validity='Y'):
        super(XrfRecord, self).__init__(
            'XRF', transaction_sequence_n, record_sequence_n
        )
        org = str(organisation_code)
        if org.isdigit():
            org = org.zfill(3)
        self.organisation_code = org[:3]
        self.identifier = str(identifier)[:14]
        self.identifier_type = identifier_type
        self.validity = validity

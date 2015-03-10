# -*- coding: utf-8 -*-
from abc import ABCMeta

"""
CWR file record model.

This contains classes representing CWR file records.

Two types of records exists: basic ones and transaction ones. Both contain a header indicating their type, the
difference is that the transaction ones also indicate their position in the file structure.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Record(object):
    """
    Represents a CWR file Record.

    A Record, at its core, just contains an alphanumeric code identifying its type.

    Albeit it's name, this prefix appears in both detail record and Transaction headers, being always the
    first values on their lines.

    With this prefix it is possible to identify each record or transaction, and also to verify it's correct
    position on the file.

    This is so because it is composed of three values: the record type,
    """

    def __init__(self, record_type):
        """
        Constructs a RecordPrefix.

        :param record_type: type code
        """
        self._record_type = record_type

    def __str__(self):
        return '%s' % (
            self._record_type)

    def __repr__(self):
        return '<class %s>(record_type=%rr)' % (
            'Record', self._record_type)

    @property
    def record_type(self):
        """
        Record Type field. Table Lookup (Record Type).

        The transaction type or detail record type.

        :return: the record type
        """
        return self._record_type


class TransactionRecord(Record):
    """
    Represents a CWR Transaction Record.

    This is meant to be used with those records containing a prefix and sequence numbering, which are transaction and detail records.

    The prefix serves both to identify them and to validate their position on the file.

    This is done with the transaction sequence number and the record sequence number.

    So, for example, a Transaction header's prefix could be: INS - 12 - 0. Meaning it is an Instrumentation transaction
    and that it should be the 13th (the numeration begins with 0) transaction on the file. As transactions are not
    records, the second number should be always zero.

    In the case of a detail record, it could be: IND - 12 - 3. Meaning it is an Instrumentation Detail record, owned
    by the 13th transaction (which is the one of the previous paragraph), and that it is the 3th (starting with
    1) detail on the file.
    """
    __metaclass__ = ABCMeta

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n):
        """
        Constructs a record with the specified information.

        Note that the sequence numbering differs if this is the header for a Transaction or a detail record.

        In the first case, the record sequence is always zero. In the second, the Transaction sequence
        is equal to its parent Transaction sequence number.

        In both cases the sequence number should be equal or great than zero.

        :param transaction_sequence_n: position in the transactions sequence
        :param record_sequence_n: position in the records sequence
        """
        super(TransactionRecord, self).__init__(record_type)
        self._transaction_sequence_n = transaction_sequence_n
        self._record_sequence_n = record_sequence_n

    def __str__(self):
        return '%s (%s-%s)' % (
            self._record_type, self._transaction_sequence_n, self._record_sequence_n)

    def __repr__(self):
        return '<class %s>(record_type=%r, transaction_sequence_n=%r, record_sequence_n=%r)' % (
            'TransactionRecord', self._record_type,
            self._transaction_sequence_n,
            self._record_sequence_n)

    @property
    def record_sequence_n(self):
        """
        Record Sequence number field. Numeric.

        Transactions always have this value set to 0.

        For detail records this value is equal to the record sequence number of the previous detail record stored
        on the file, plus 1. So Detail numbering will start with 1.

        :return: the record sequence number
        """
        return self._record_sequence_n

    @property
    def transaction_sequence_n(self):
        """
        Transaction Sequence number field. Numeric.

        In each Group the transaction sequence starts with 0, so the first Transaction of each Group should have
        0 as the sequence number.

        The following Transactions should have a sequence number equal to the previous Transaction header's number
        incremented by 1.

        In the case of detail records the transaction sequence should be equal to the transaction sequence of the
        previous Transaction header, the owner of the detail.

        :return: the transaction sequence number
        """
        return self._transaction_sequence_n


class NRARecord(TransactionRecord):
    """
    Represents a CWR Non-Roman Alphabet record.

    These are the records to represent alternate names out of the ASCII table.
    """
    __metaclass__ = ABCMeta

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, language=None):
        super(NRARecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._language = language

    @property
    def language(self):
        """
        Language Code field. Table Lookup (Language Code Table).

        The Language code of the record.

        :return: the language code of the record
        """
        return self._language
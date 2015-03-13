# -*- coding: utf-8 -*-

from cwr.record import Record

"""
CWR file groups model.

This consists on the Group Header (GRH) and Group Trailer (GRT).

These represent groups inside a CWR file or transmission. These serve two purposes: first they group together
all the transactions of a kind, and second they serve to check the integrity of the data.

The Group Header indicates which type of Transaction will be stored inside the group, while the Group Trailer indicates
how many transactions and records should be inside the Group, as measure to avoid tampering.

It is important to note again that while there can be multiple groups each should contain a single type of transaction,
and all transactions of the same type should be on the same group.

So if the group contains NWR transactions all of the should be on a single group, which can not contain any other type
of transaction. Just to remark this, no other group on that file should contain NWR transactions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class GroupHeader(Record):
    """
    Represents a CWR file Group Header (GRH).

    The GRH record is used to indicate the presence of a group (or batch) of transactions within the file.

    A group can only contain one type of transaction and this is indicated in the Transaction Type field.
    """

    def __init__(self, record_type, group_id, transaction_type, version_number="02.10", batch_request_id=0):
        super(GroupHeader, self).__init__(record_type)
        self._group_id = group_id
        self._transaction_type = transaction_type
        self._version_number = version_number
        self._batch_request_id = batch_request_id

    def __str__(self):
        return '%s(%s)' % (
            self._transaction_type,
            self._group_id)

    def __repr__(self):
        return '<class %s>(group_id=%r, transaction_type=%r, version_number=%r, batch_request_id=%r)' % (
            'GroupHeader', self._group_id,
            self._transaction_type,
            self._version_number,
            self._batch_request_id)

    @property
    def batch_request_id(self):
        """
        Batch request ID field. Numeric.

        A unique sequential number to identify the group. This number is managed by the submitter to identify the group
        among multiple submission files.

        :return: the submitter's batch request id
        """
        return self._batch_request_id

    @property
    def group_id(self):
        """
        Group ID field. Numeric.

        A unique sequential number for this group within this file.

        :return: the group id
        """
        return self._group_id

    @property
    def transaction_type(self):
        """
        Transaction Type field. Table lookup (Transaction Type table).

        Indicates the type of transactions included in this group. No other type of transaction may be included.

        Values for this field reside in the Transaction Type table.

        :return: the transaction type
        """
        return self._transaction_type

    @property
    def version_number(self):
        """
        Version Number for this transaction type field. Alphanumeric.

        Indicates the version of the transaction type on this group.

        By default this is '02.10', meaning CWR v2.1.

        :return: transaction version number
        """
        return self._version_number


class GroupTrailer(Record):
    """
    Represents a CWR file Group Trailer (GRT).

    The Group Trailer Record indicates the end of a group and provides both transaction and record counts for the group.
    """

    def __init__(self, record_type, group_id, transaction_count, record_count):
        """
        Constructs a GroupTrailer.

        :param group_id: group ID
        :param transaction_count: number of transactions in the group
        :param record_count: number of records in the group
        """
        super(GroupTrailer, self).__init__(record_type)
        self._group_id = group_id
        self._transaction_count = transaction_count
        self._record_count = record_count

    def __str__(self):
        return '%s(g:%s, t:%s)' % (
            self._group_id,
            self._group_id,
            self._transaction_count)

    def __repr__(self):
        return '<class %s>(group_id=%r, transaction_count=%r, record_count=%r)' % (
            'GroupTrailer', self._group_id,
            self._transaction_count,
            self._record_count)

    @property
    def group_id(self):
        """
        Group ID field. Numeric.

        A unique sequential number for this group within this file.

        It is the same group id that was present on the preceding GRH record.

        :return: the group id
        """
        return self._group_id

    @property
    def record_count(self):
        """
        Record Count field. Numeric.

        The number of physical records included within this group including GRH and GRT records.

        :return: the record count
        """
        return self._record_count

    @property
    def transaction_count(self):
        """
        Transaction Count field. Numeric.

        The number of transactions included within this group.

        :return: the number of transactions
        """
        return self._transaction_count
# -*- coding: utf-8 -*-

from cwr.record import Record

"""
CWR file groups model.

This consists on the Group Header (GRH) and Group Trailer (GRT).

These represent groups inside a CWR file or transmission. These serve two
purposes: first they group together all the transactions of a kind, and second
they serve to check the integrity of the data.

The Group Header indicates which type of Transaction will be stored inside the
group, while the Group Trailer indicates how many transactions and records
should be inside the Group, as measure to avoid tampering.

It is important to note again that while there can be multiple groups each
should contain a single type of transaction, and all transactions of the same
type should be on the same group.

So if the group contains NWR transactions all of the should be on a single
group, which can not contain any other type of transaction. Just to remark
this, no other group on that file should contain NWR transactions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class GroupHeader(Record):
    """
    Represents a CWR file Group Header (GRH).

    The GRH record is used to indicate the presence of a group (or batch) of
    transactions within the file.

    A group can only contain one type of transaction and this is indicated in
    the Transaction Type field.
    """

    def __init__(self,
                 record_type='',
                 group_id=0,
                 transaction_type='',
                 version_number='02.10',
                 batch_request_id=0
                 ):
        super(GroupHeader, self).__init__(
            record_type
        )
        self._group_id = group_id
        self._transaction_type = transaction_type
        self._version_number = version_number
        self._batch_request_id = batch_request_id

    def __str__(self):
        return '%s(%s)' % (
            self._transaction_type,
            self._group_id)

    def __repr__(self):
        return '<class %s>(group_id=%r, transaction_type=%r, ' \
               'version_number=%r, batch_request_id=%r)' % (
                   'GroupHeader', self._group_id,
                   self._transaction_type,
                   self._version_number,
                   self._batch_request_id)

    @property
    def batch_request_id(self):
        """
        Batch request ID field. Numeric.

        A unique sequential number to identify the group. This number is
        managed by the submitter to identify the group among multiple
        submission files.

        :return: the submitter's batch request id
        """
        return self._batch_request_id

    @batch_request_id.setter
    def batch_request_id(self, value):
        self._batch_request_id = value

    @property
    def group_id(self):
        """
        Group ID field. Numeric.

        A unique sequential number for this group within this file.

        :return: the group id
        """
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value

    @property
    def transaction_type(self):
        """
        Transaction Type field. Table lookup (Transaction Type table).

        Indicates the type of transactions included in this group. No other
        type of transaction may be included.

        Values for this field reside in the Transaction Type table.

        :return: the transaction type
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self._transaction_type = value

    @property
    def version_number(self):
        """
        Version Number for this transaction type field. Alphanumeric.

        Indicates the version of the transaction type on this group.

        By default this is '02.10', meaning CWR v2.1.

        :return: transaction version number
        """
        return self._version_number

    @version_number.setter
    def version_number(self, value):
        self._version_number = value


class GroupTrailer(Record):
    """
    Represents a CWR file Group Trailer (GRT).

    The Group Trailer Record indicates the end of a group and provides both
    transaction and record counts for the group.
    """

    def __init__(self,
                 record_type='',
                 group_id=0,
                 transaction_count=0,
                 record_count=0,
                 currency_indicator=None,
                 total_monetary_value=None
                 ):
        """
        Constructs a GroupTrailer.

        :param group_id: group ID
        :param transaction_count: number of transactions in the group
        :param record_count: number of records in the group
        """
        super(GroupTrailer, self).__init__(
            record_type
        )
        self._group_id = group_id
        self._transaction_count = transaction_count
        self._record_count = record_count
        self._currency_indicator = currency_indicator
        self._total_monetary_value = total_monetary_value

    def __str__(self):
        return '%s(g:%s, t:%s)' % (
            self._group_id,
            self._group_id,
            self._transaction_count)

    def __repr__(self):
        return '<class %s>(group_id=%r, transaction_count=%r, ' \
               'record_count=%r)' % (
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

    @group_id.setter
    def group_id(self, value):
        self._group_id = value

    @property
    def record_count(self):
        """
        Record Count field. Numeric.

        The number of physical records included within this group including
        GRH and GRT records.

        :return: the record count
        """
        return self._record_count

    @record_count.setter
    def record_count(self, value):
        self._record_count = value

    @property
    def transaction_count(self):
        """
        Transaction Count field. Numeric.

        The number of transactions included within this group.

        :return: the number of transactions
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, value):
        self._transaction_count = value

    @property
    def total_monetary_value(self):
        """
        Total monetary value represented by the group.
        :return: the monetary value
        """
        return self._total_monetary_value

    @total_monetary_value.setter
    def total_monetary_value(self, value):
        self._total_monetary_value = value

    @property
    def currency_indicator(self):
        """
        ISO Code of the currency used for the total monetary value. ISO codes can be found in ISO 4217 table
        (actually ISO 3166 country codes 2A plus the first letter of the currency of the country:
        for example, USD for Dollar in US).
        :return: the ISO Code
        """
        return self._currency_indicator

    @currency_indicator.setter
    def currency_indicator(self, value):
        self._currency_indicator = value


class Group(object):
    """
    Represents a CWR file group of transactions inside a transmission.

    All transactions of the same type should be contained in the same group
    (i.e. all NWR transactions should appear in one single NWR group), and
    each group type can only be used once per file (i.e there can only be one
    NWR and one REV group per file).

    The type of the group is indicated by the header.
    """

    def __init__(self,
                 group_header,
                 group_trailer,
                 transactions=None
                 ):
        """
        Constructs a TransactionGroup.

        This stores all the transaction of a kind in the file, containing only
        transactions of that kind.

        A file can not contain two groups with the same type of transaction.

        The group header should be a GroupHeader, and the trailer a
        GroupTrailer.

        The transactions is a collection of entities representing the
        transactions.

        :param group_header: the group header
        :param group_trailer: the group trailer
        :param transactions: the group transactions
        """
        self._group_header = group_header
        self._group_trailer = group_trailer
        if not transactions:
            self._transactions = []
        else:
            self._transactions = transactions

    def __str__(self):
        return '%s to %s [%s]' % (
            self._group_header, self._group_trailer, self._transactions)

    def __repr__(self):
        return '<class %s>(grh=%r, grt=%r, transactions=%r)' % (
            'TransactionGroup', self._group_header,
            self._group_trailer,
            self._transactions)

    @property
    def group_header(self):
        """
        The group's header. This is a GroupHeader.

        :return: group's header
        """
        return self._group_header

    @group_header.setter
    def group_header(self, value):
        self._group_header = value

    @property
    def group_trailer(self):
        """
        The group's trailer. This is a GroupTrailer.

        :return: group's trailer
        """
        return self._group_trailer

    @group_trailer.setter
    def group_trailer(self, value):
        self._group_trailer = value

    @property
    def transactions(self):
        """
        The group transactions.

        This is a collection of entities representing instances of one type of
        transaction.

        :return: the group transactions
        """
        return self._transactions

    @transactions.setter
    def transactions(self, value):
        self._transactions = value

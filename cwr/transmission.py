# -*- coding: utf-8 -*-

from cwr.record import Record

"""
CWR file transmission model.

This consists on the Transmission Header (HDR) and Transmission Trailer (TRL).

These classes represent a transmission, which is all the contents on a CWR file.
Additionally, the transmission also contains information to check the integrity
of the data.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TransmissionHeader(Record):
    """
    Represents a CWR file Transmission Header (HDR).

    This stores the general information about a transmission (which means, the
    CWR file contents) submitted by a participant, containing the file control
    information as well as the name of the sender.
    """

    def __init__(self,
                 record_type='',
                 sender_id=0,
                 sender_name='',
                 sender_type='',
                 creation_date_time=None,
                 transmission_date=None,
                 edi_standard='01.10',
                 character_set=None
                 ):
        """
        Constructs a TransmissionHeader.

        :param sender_id: the CWR Sender ID or the Society Code
        :param sender_name: name of the sender
        :param sender_type: code identifying the type of sender
        :param creation_date_time: creation date and time for the file
        :param transmission_date: date in which the file was transmitted
        :param record_type: the CWR record type
        :param edi_standard: EDI standard version (01.10 by default)
        :param character_set: file encoding set (ASCII by default)
        """
        super(TransmissionHeader, self).__init__(record_type)

        # Sender info
        self._sender_id = sender_id
        self._sender_name = sender_name
        self._sender_type = sender_type

        # Dates
        self._creation_date_time = creation_date_time
        self._transmission_date = transmission_date

        # Other info
        self._edi_standard = edi_standard
        self._character_set = character_set

    def __str__(self):
        return '%s (%s, %s) on %s' % (
            self._sender_name, self._sender_id, self._sender_type,
            self._transmission_date)

    def __repr__(self):
        return '<class %s>(sender_id=%r, sender_name=%r, sender_type=%r, ' \
               'creation_date=%r, transmission_date=%r)' % (
                   'TransmissionHeader', self._sender_id,
                   self._sender_name, self._sender_type,
                   self._creation_date_time,
                   self._transmission_date)

    @property
    def character_set(self):
        """
        Character Set field. Table lookup (not yet existing).

        By default this is ASCII, and files using any other set are only
        intended to be sent to societies that accept and use such character
        sets (e.g, CASH).

        The table containing the accepted values does not exist at the time of
        this implementation.

        :return: the character set used on the file
        """
        return self._character_set

    @character_set.setter
    def character_set(self, value):
        self._character_set = value

    @property
    def creation_date_time(self):
        """
        Creation Date and Time fields. Date and time.

        The date that this file was created.

        :return: the creation date
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, value):
        self._creation_date_time = value

    @property
    def edi_standard(self):
        """
        EDI Standard Version Number field. Alphanumeric.

        Indicates which version of the header and trailer records was used to
        create the data in this file.

        By default this is '01.10', which is required by the CWR v2.1 standard.

        :return: the EDI standard version number
        """
        return self._edi_standard

    @edi_standard.setter
    def edi_standard(self, value):
        self._edi_standard = value

    @property
    def sender_id(self):
        """
        Sender ID field. Numeric.

        If Sender Type is equal to 'PB' (Publisher), 'AA' (Administrative
        Agency), or 'WR' (Writer), the sender  must enter their assigned CWR
        CAE number in this field.

        If Sender Type is equal to 'SO' (Society), the sending society must
        enter their Society Code.

        The Society codes reside in the Society Code Table. The others on the
        CWR Sender ID and Codes Table.

        :return: the sender ID
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, value):
        self._sender_id = value

    @property
    def sender_name(self):
        """
        Sender Name field. Alphanumeric.

        The name of the sender.

        :return: name of the sender
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, value):
        self._sender_name = value

    @property
    def sender_type(self):
        """
        Sender Type field. Alphanumeric.

        Indicates if the sender of the file is a society or a publisher.

        Possible values are:
        - 'AA': Administrative Agency
        - 'PB': Publisher
        - 'SO': Society
        - 'WR': Writer

        :return: the sender type
        """
        return self._sender_type

    @sender_type.setter
    def sender_type(self, value):
        self._sender_type = value

    @property
    def transmission_date(self):
        """
        Transmission Date field. Date.

        The date that this file was transmitted to all receiving entities.

        :return: the transmission date
        """
        return self._transmission_date

    @transmission_date.setter
    def transmission_date(self, value):
        self._transmission_date = value


class TransmissionTrailer(Record):
    """
    Represents a CWR file Transmission Trailer (TRL).

    The Transmission Trailer record indicates the end of the transmission file.

    Control totals representing the number of groups, transactions, and records
    within the file are included on this record.
    """

    def __init__(self,
                 record_type='',
                 group_count=0,
                 transaction_count=0,
                 record_count=0
                 ):
        """
        Constructs a TransmissionTrailer.

        :param group_count: the total number of groups on the file
        :param transaction_count: the total number of transactions on the file
        :param record_count: the total number of records on the file
        """
        super(TransmissionTrailer, self).__init__(
            record_type
        )

        self._group_count = group_count
        self._transaction_count = transaction_count
        self._record_count = record_count

    def __str__(self):
        return '%s groups, %s transactions, %s records' % (
            self._group_count, self._transaction_count, self._record_count)

    def __repr__(self):
        return '<class %s>(group_count=%r, transaction_count=%r, ' \
               'record_count=%r)' % (
                   'TransmissionTrailer', self._group_count,
                   self._transaction_count, self._record_count)

    @property
    def group_count(self):
        """
        Group Count field. Numeric.

        The number of groups included within this file.

        :return: the total group count
        """
        return self._group_count

    @group_count.setter
    def group_count(self, value):
        self._group_count = value

    @property
    def record_count(self):
        """
        Record Count field. Numeric.

        The number of physical records included in this file including HDR and
        TRL records.

        :return: the total record count
        """
        return self._record_count

    @record_count.setter
    def record_count(self, value):
        self._record_count = value

    @property
    def transaction_count(self):
        """
        Transaction Count field. Numeric.

        The number of transactions included within this file.

        :return: the total transaction count
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, value):
        self._transaction_count = value


class Transmission(object):
    """
    Represents a CWR file Transmission.

    As a Transmission wraps all the file's data, this in practise equals to the
    file content.

    It is composed by a Transmission Header and a Transmission Trailer, and
    in-between a collection of groups, following the structure [HDR, [GRH,GRT]*,
    TRL].
    """

    def __init__(self,
                 header,
                 trailer,
                 groups=None
                 ):
        """
        Constructs a Transmission.

        The transaction groups should be a collection of TransactionGroup
        instances. While the header should be a TransmissionHeader and the
        trailer a TransmissionTrailer.

        :param header: the transmission header
        :param trailer: the transmission trailer
        :param groups: the transaction groups
        """
        self._header = header
        self._trailer = trailer
        if not groups:
            self._groups = []
        else:
            self._groups = groups

    def __str__(self):
        return '%s to %s [%s]' % (
            self._header, self._trailer, self._groups)

    def __repr__(self):
        return '<class %s>(hdr=%r, trl=%r, groups=%r)' % (
            'Transmission', self._header,
            self._trailer,
            self._groups)

    @property
    def groups(self):
        """
        The transmission groups. This is a collection of TransactionGroups.

        :return: a collection with transaction groups
        """
        return self._groups

    @groups.setter
    def groups(self, value):
        self._groups = value

    @property
    def header(self):
        """
        The transmission header. This is a TransmissionHeader.

        :return: the transmission header
        """
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def trailer(self):
        """
        The transmission trailer. This is a TransmissionTrailer.

        :return: the transmission trailer
        """
        return self._trailer

    @trailer.setter
    def trailer(self, value):
        self._trailer = value

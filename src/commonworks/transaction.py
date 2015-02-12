# -*- encoding: utf-8 -*-
from abc import ABCMeta

"""
CWR transaction classes.

These files are not meant to store all the data of the transaction, that is done with the other model files,
but to indicate the relationships contained in these transactions.

For example, an Agreement Transaction would indicate an Agreement, the Territories it applies to and the
Interested Parties for each Territory. While the concrete information of that Agreement, Territories and
Interested Parties are stored in their own model classes.

When representing a full CWR file these transmissions should be stored on the Transmission classes from the file
module. More precisely, they should be contained in a TransactionGroup.

A transaction is a composition of records, the first of which is called the transaction header. This is the record
giving the name for the transaction, so for example an Agreement Transaction means that the header record
is an Agreement Record.

This header will describe the Transaction.

The possible transactions in CWR v2.1 are:
- Acknowledgment of Transaction (ACK)
- Agreement supporting Work Registration (AGR)
- Existing Work which is in conflict with a Work registration (EXC)
- New Works Registration (NWR)
- Notification of ISWC assigned to a Work (ISW)
- Revised Registration (REV)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class AcknowledgementTransaction(object):
    """
    Represents a CWR Acknowledgment Transaction (ACK).
    """

    def __init__(self, agr=None, nwr=None, rev=None, exc=None, messages=None):
        self._agr = agr
        self._nwr = nwr
        self._rev = rev
        self._exc = exc

        if messages is None:
            self._messages = []
        else:
            self._messages = messages

    @property
    def agr(self):
        """
        Agreement supporting Work Registration field.

        :return: the agreement transaction affected by this acknowledgement
        """
        return self._agr

    @property
    def exc(self):
        """
        Existing Work in Conflict field.

        :return: the existing work in conflict transaction affected by this acknowledgement
        """
        return self._exc

    @property
    def messages(self):
        """
        Message field.

        List all messages generated as a result of editing this transaction.

        :return: a list with all the messages
        """
        return self._messages

    @property
    def nwr(self):
        """
        New Works Registration field.

        :return: the new works transaction affected by this acknowledgement
        """
        return self._nwr

    @property
    def rev(self):
        """
        Revised Registration field.

        :return: the revised registration transaction affected by this acknowledgement
        """
        return self._rev


class TransactionInterestedParty(object):
    """
    Represents the relationship between an Interested Party and an Agreement
    """
    __metaclass__ = ABCMeta

    def __init__(self, reversionary=False, first_record_refusal=False, usa_license=False):
        # Flags
        self._first_record_refusal = first_record_refusal
        self._reversionary = reversionary
        self._usa_license = usa_license

    @property
    def first_record_refusal(self):
        """
        First Recording Refusal Indicator field.

        This field indicates that the submitter needs to be asked before the society can authorize a first recording.
        Note that this field is mandatory for registrations with the UK societies.

        It is a Boolean field, and by default is False.

        :return: True if the submitter needs to be asked to authorize first recording, False otherwise
        """
        return self._first_record_refusal

    @property
    def reversionary(self):
        """
        Reversionary Indicator field.

        This indicates that the Interested Party is claiming the work under the reversionary provisions.
        Only some societies recognize reversionary rights.

        It is a Boolean field, and by default is False.

        :return: True if the work is under reversionary provisions, False otherwise
        """
        return self.reversionary

    @property
    def usa_license(self):
        """
        USA License Indicator field.

        This field indicates whether rights for this Interested Party flow through ASCAP, BMI, or SESAC for the U.S.

        It is a Boolean field, and by default is False.

        :return: True if the rights flow to the U.S., False otherwise
        """
        return self._usa_license


class TransactionWriter(TransactionInterestedParty):
    """
    Represents a Writer on a Transaction.
    """

    def __init__(self, writer_id=None, designation=None, writer_unknown=False, work_for_hire=False,
                 reversionary=False, first_record_refusal=False, usa_license=False):
        super(TransactionWriter, self).__init__(reversionary, first_record_refusal, usa_license)
        self._writer_id = writer_id
        self._work_for_hire = work_for_hire
        self._designation = designation
        self._writer_unknown = writer_unknown

    def designation(self):
        """
        Writer Designation Code field.

        Code defining the role the writer played in the composition of the work.  These values reside in the Writer
        Designation Table. This field is required for record type SWR and optional for record type OWR.

        :return: the Writer designation code
        """
        return self._designation

    @property
    def writer_unknown(self):
        """
        Writer Unknown Indicator field.

        Indicates if the name of this writer is unknown. Note that this field must be left blank for SWR records.
        For OWR records, this field must be set to “Y” if the Writer Last Name is blank.

        :return: True if the Writer is unknown, False otherwise
        """
        return self._writer_unknown

    @property
    def work_for_hire(self):
        """
        Work For Hire Indicator field.

        Indicates whether or not this work was written for hire.

        :return: True if thi work was written for hire, False otherwise
        """
        return self._work_for_hire

    @property
    def writer_id(self):
        """
        The Writer's id

        :return: the writer id
        """
        return self._writer_id


class TransactionPublisher(TransactionInterestedParty):
    """
    Represents a Publisher on a Transaction.

    This is for Publisher Controlled By Submitter (SPU) and Other Publisher (OPU) transactions.
    """

    def __init__(self, sequence_n, publisher_id=None, publisher_unknown=False, publisher_type=None,
                 agreement_type=None,
                 submitter_agreement_id=None, society_agreement_id=None, isa_code=None,
                 pr_society=None, pr_owner_share=0, mr_society=None, mr_owner_share=0, sr_society=None,
                 sr_owner_share=0,
                 territories=None,
                 reversionary=False, first_record_refusal=False, usa_license=False):
        super(TransactionPublisher, self).__init__(reversionary, first_record_refusal, usa_license)

        # Interested Parties
        self._publisher_id = publisher_id
        self._publisher_unknown = publisher_unknown
        self._publisher_type = publisher_type
        self._sequence_n = sequence_n

        # Interested Parties Agreement info
        self._submitter_agreement_id = submitter_agreement_id
        self._society_agreement_id = society_agreement_id
        self._agreement_type = agreement_type

        # Shares
        self._pr_society = pr_society
        self._pr_owner_share = pr_owner_share
        self._mr_society = mr_society
        self._mr_owner_share = mr_owner_share
        self._sr_society = sr_society
        self._sr_owner_share = sr_owner_share

        # Other info
        self._isa_code = isa_code

        # Territories and shares
        if territories is None:
            self._territories = []
        else:
            self._territories = territories

    @property
    def agreement_type(self):
        """
        Agreement Type field.

        Code defining the category of agreement.

        The values reside in the Agreement Type Table.

        :return: the Agreement type
        """
        return self._agreement_type

    @property
    def isa_code(self):
        """
        International Standard Agreement Code field.

        A unique number assigned to this agreement. This number is not yet available.

        :return: the ISA code
        """
        return self._isa_code

    @property
    def publisher_id(self):
        """
        Interested Party # field.

        Submitting publisher’s unique identifier for this publisher.  This field is required for record type SPU and
        optional for record type OPU

        :return: the Publisher id
        """
        return self._publisher_id

    @property
    def publisher_type(self):
        """
        Publisher Type field.

        Role played by this publisher in this work. Choose among original publisher, administrator, subpublisher, and
        income participant. In a co-publishing administration situation, the administering publisher may be listed
        twice, as an original publisher and as an administrator.

        :return: the Publisher's role
        """
        return self._publisher_type

    @property
    def publisher_unknown(self):
        """
        Publisher Unknown Indicator.

        Indicates if the name of this publisher is unknown.  Note that this field must be left blank for SPU records.
        For OPU records, this field must be set to True if the Publisher Name is blank

        :return: True if the Publisher is unknown, False otherwise
        """
        return self._publisher_unknown

    @property
    def sequence_n(self):
        """
        Publisher Sequence Number field.

        This enables a rights organization to link subpublishers and administrators to the proper original publisher.
        Each original publisher will start a new chain. An income participant may start a chain, or be included in a
        chain begun by the original publisher which has allocated rights to the income participant.

        :return: the Publisher sequence number in a chain
        """
        return self._sequence_n

    @property
    def society_agreement(self):
        """
        Society-assigned Agreement Number field.

        If you have previously notified the society of this agreement, you may have the number assigned by the society
        to this agreement. You can then provide this number when registering the works.

        :return: the society-assigned Agreement number
        """
        return self._society_agreement_id

    @property
    def mr_owner_share(self):
        """
        MR Ownership Share field.

        Defines the percentage of the publisher’s ownership of the mechanical rights to the work.  This share does not
        define the percentage of the total royalty distributed for sales of CDs, Cassettes, etc. containing the work
        that will be collected by the publisher.  Within an individual SPU record, this value can range from 0 to 100.0

        :return: the mechanical of the performing rights for the Publisher
        """
        return self._mr_owner_share

    @property
    def mr_society(self):
        """
        MR Affiliation Society field.

        Number assigned to the Mechanical Rights Society with which the publisher is affiliated.
        These values reside on the Society Code Table.

        :return: the Publisher's mechanical rights society
        """
        return self._mr_society

    @property
    def pr_owner_share(self):
        """
        PR Ownership Share field.

        Defines the percentage of the publisher’s ownership of the performance rights to the work.  This share does not
        define the percentage of the total royalty distributed for performance of the work that will be collected by the
        publisher.  Within an individual SPU record, this value can range from 0 to 50.0.

        :return: the percentage of the performing rights for the Publisher
        """
        return self._pr_owner_share

    @property
    def pr_society(self):
        """
        PR Affiliation Society field.

        Number assigned to the Performing Rights Society with which the publisher is affiliated.  These values reside on
        the Society Code Table.

        :return: the Publisher's performing rights society
        """
        return self._pr_society

    @property
    def sr_owner_share(self):
        """
        SR Ownershipt Share field.

        Defines the percentage of the publisher’s ownership of the synch rights to the work.  This share does not define
        the percentage of the total money distributed that will be collected by the publisher.  Within an individual SPU
        record, this value can range from 0 to 100.0

        :return: the percentage of the synchronization rights for the Publisher
        """
        return self._sr_owner_share

    @property
    def sr_society(self):
        """
        SR Affiliation Society field.

        Number assigned to the Society with which the publisher is affiliated for administration of synchronization
        rights.

        These values reside on the Society Code Table.

        :return: the Publisher's synchronization rights society
        """
        return self._sr_society

    @property
    def territories(self):
        """
        A collection of TerritoryShare instances.

        This indicates the territories to which the Agreement applies and the share applied to each.

        :return: a collection of TerritoryShare instances applied to the Agreement
        """
        return self._territories

    @property
    def submitter_agreement(self):
        """
        Submitter Agreement Number field.

        This points to an agreement between this publisher and another publisher acting as a domestic or foreign
        administrator and it is your internal number.

        :return: the Submitter Agreement number
        """
        return self._submitter_agreement_id


class PublisherWithTerritories(object):
    """
    Represents a Publisher and his territories.
    """

    def __init__(self, publisher, territories=None):
        self._publisher = publisher

        if territories is None:
            self._territories = []
        else:
            self._territories = territories

    @property
    def publisher(self):
        """
        The Publisher.

        Returns the Publisher which affects the territories.

        :return: the Publisher
        """
        return self._publisher

    @property
    def territories(self):
        """
        The territories.

        Returns the territories to which the Publisher affects.

        :return: the territories of the Publisher
        """
        return self._territories


class WriterWithTerritoryPublisher(object):
    """
    Represents a Writer along his Territories and Publishers.
    """

    def __init__(self, writer, territories=None, publishers=None):
        self._writer = writer

        if territories is None:
            self._territories = []
        else:
            self._territories = territories

        if publishers is None:
            self._publishers = []
        else:
            self._publishers = publishers

    @property
    def publishers(self):
        """
        Publishers representing the Writer.

        :return: all the Publishers representing the Writer
        """
        return self._publishers

    @property
    def territories(self):
        """
        Territories of the Writer.

        :return: the Territories of the Writer
        """
        return self._territories

    @property
    def writer(self):
        """
        The Writer.

        :return: the Writer
        """
        return self._writer
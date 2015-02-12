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
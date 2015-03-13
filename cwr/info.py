# -*- coding: utf-8 -*-
from cwr.record import TransactionRecord

"""
CWR information model.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class AdditionalRelatedInfoRecord(TransactionRecord):
    """
    Represents a CWR Additional Related Info (ARI).

    This record may contain specific information or general information.

    The Work number is used to relate the work being registered to an entry in an unidentified performance/use list, or
    to correct a work referenced in a cue sheet, web site, etc.

    The free-text note contains general information addressed to one or all societies. It may be used for important
    information concerning the work registration.

    Societies are not obliged to process ARI records, even if the note is addressed to them.

    The note field should be used sparingly.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, society_n, type_of_right, work_n='',
                 subject_code=None, note=''):
        super(AdditionalRelatedInfoRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._society_n = society_n
        self._type_of_right = type_of_right
        self._work_n = work_n
        self._subject_code = subject_code
        self._note = note

    @property
    def note(self):
        """
        Note field. Alphanumeric.

        Free text field pertaining to the type of right and subject specified above.

        :return: an informative note
        """
        return self._note

    @property
    def society_n(self):
        """
        Society Number field. Table Lookup (Society Code Table).

        Number assigned to the Society to which the Note is addressed.

        If the note is addressed to all societies that use the ARI record this should be '000'.

        :return: the society number ID
        """
        return self._society_n

    @property
    def subject_code(self):
        """
        Subject Code field. Table Lookup (Subject Code).

        Subject of the ARI.

        :return: the subject code
        """
        return self._subject_code

    @property
    def type_of_right(self):
        """
        Type of Right field. Table Lookup (Type of Right).

        Indicates to which type of right does this information relate.

        :return: the type of right the information is for
        """
        return self._type_of_right

    @property
    def work_n(self):
        """
        Work Number field. Alphanumeric.

        The Society work ID that relates to this registration.

        It may have been found on an unidentified list, or a website, …

        :return: the work id
        """
        return self._work_n
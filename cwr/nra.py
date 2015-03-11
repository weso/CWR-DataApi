# -*- coding: utf-8 -*-

"""
Classes for other Non-Roman Alphabet records.
"""
from abc import ABCMeta

from cwr.record import TransactionRecord


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


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


class NPARecord(NRARecord):
    """
    Represents a CWR Non-Roman Alphabet Agreement Party Name Record (NPA).

    This record identifies names in a non-roman alphabet for the acquiring parties of this agreement. The language code
    is used to identify the alphabet. This record can be used to identify the name of the party in the preceding IPA
    record.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, ip_name, ip_writer_name, ip_id='',
                 language=None):
        super(NPARecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n, language)
        # IP info
        self._ip_name = ip_name
        self._ip_writer_name = ip_writer_name
        self._ip_id = ip_id

        # Language info
        self._language = language

    @property
    def ip_id(self):
        """
        Interested Party # field. Alphanumeric.

        Submitting publisher’s unique identifier for this Writer.

        :return: the Interested Party ID
        """
        return self._ip_id

    @property
    def ip_name(self):
        """
        Interested Party Name field. Alphanumeric.

        The last of a writer or the publisher name.

        :return: the last name of a writer of the publisher name
        """
        return self._ip_name

    @property
    def ip_writer_name(self):
        """
        Interested Party Writer Name field. Alphanumeric.

        The first name of a writer.

        :return: the first name of a writer
        """
        return self._ip_writer_name


class NWNRecord(NRARecord):
    """
    Represents a CWR Non-Roman Alphabet Writer Name Record (NWN).

    This record identifies writer names in non-roman alphabets for this work. The language code is used to identify the
    alphabet. This record can be used to identify the name of the writer in the preceding SWR/OWR record.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, first_name, last_name, ip_id='',
                 language=None):
        super(NWNRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n, language)
        # Writer info
        self._first_name = first_name
        self._last_name = last_name
        self._ip_id = ip_id

    @property
    def ip_id(self):
        """
        Interested Party # field. Alphanumeric.

        Submitting publisher’s unique identifier for this Publisher.

        :return: the Interested Party ID
        """
        return self._ip_id

    @property
    def first_name(self):
        """
        Writer First Name. Alphanumeric.

        The first name of this writer.

        :return: the first name of this writer
        """
        return self._first_name

    @property
    def last_name(self):
        """
        Writer Last Name. Alphanumeric.

        The last or single name of this writer.

        :return: the last or single name of this writer
        """
        return self._last_name


class NATRecord(NRARecord):
    """
    Represents a CWR Non-Roman Alphabet Title (NAT) record.

    This record identifies titles in other alphabets for this work. The language code is used to identify the alphabet.
    This record can be used to describe the original title of a work, and it can also be used to describe alternate
    titles.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, title, title_type, language=None):
        super(NATRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n, language)
        # Title info
        self._title = title
        self._title_type = title_type

    @property
    def title(self):
        """
        Title field. Alphanumeric.

        The work title in non-Roman alphabet.

        :return: the work title in non-Roman alphabet
        """
        return self._title

    @property
    def title_type(self):
        """
        Title Type field. Table Lookup (Title Type Table).

        Indicates the type of title presented on this record (original, alternate etc.).

        :return: the type of the title
        """
        return self._title_type


class NRARecordWork(NRARecord):
    """
    Represents a Non-Roman Alphabet record used for Work details.

    This represents the following records:
    - Non-Roman Alphabet Entire Work Title for Excerpts (NET).
    - Non-Roman Alphabet Title for Components (NCT).
    - Non-Roman Alphabet Original Title for Version (NVT).

    This record identifies titles in other alphabets for this work. The language code is used to identify the alphabet.
    This record can be used to describe the original title of a work, and it can also be used to describe alternate
    titles.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, title, language=None):
        super(NRARecordWork, self).__init__(record_type, transaction_sequence_n, record_sequence_n, language)
        self._title = title

    @property
    def title(self):
        """
        Title field. Alphanumeric.

        The title in non-Roman alphabet.

        :return: the title in non-Roman alphabet
        """
        return self._title


class NOWRecord(NRARecord):
    """
    Represents a CWR Non-Roman Alphabet Other Writer Name (NOW) record.

    This record identifies writer names in non-roman alphabets for the work named in an EWT (entire work for an
    excerpt), VER (original work for a version), or COM (component) record. The language code is used to identify the
    alphabet.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, first_name, name, position=None,
                 language=None):
        super(NOWRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n, language)
        # Writer information
        self._first_name = first_name
        self._name = name
        self._position = position

    @property
    def first_name(self):
        """
        Writer First Name. Alphanumeric.

        The first name of this writer.

        :return: the first name of this writer
        """
        return self._first_name

    @property
    def name(self):
        """
        Writer Name. Alphanumeric.

        The name of this writer.

        :return: the name of this writer
        """
        return self._name

    @property
    def position(self):
        """
        Writer Position field. List lookup (previous record).

        The position of the writer in the corresponding EWT, VER, or COM record.

        :return: the position of the writer in the previous record
        """
        return self._position


class NPRRecord(NRARecord):
    """
    Represents a CWR Performance Data in non-roman alphabet (NPR) record.

    This record contains either the non-roman alphabet name of a person or group performing this work either in public
    or on a recording, or the language/dialect of the performance. This is particularly important for Chinese dialects
    such as Cantonese. Performance Dialect, if entered, must be a valid code from ISO 639-2(T).
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, first_name='', name='', ipi_name=None,
                 ipi_base=None, language=None, performance_language=None, performance_dialect=None):
        super(NPRRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n, language)
        # Artist data
        self._first_name = first_name
        self._name = name
        self._ipi_name = ipi_name
        self._ipi_base = ipi_base

        # Language data
        self._performance_language = performance_language
        self._performance_dialect = performance_dialect

    @property
    def first_name(self):
        """
        Performing Artist First Name field. Alphanumeric.

        First name of a person that has performed the work on a recording or in public.

        :return: the performer's first name
        """
        return self._first_name

    @property
    def ipi_base(self):
        """
        Performing Artist IPI Base Number field. Table lookup (IPI database).

        The IPI base number assigned to this performing artist.

        :return: the performer's IPI base number
        """
        return self._ipi_base

    @property
    def ipi_name(self):
        """
        Performing Artist IPI Name # field. Table Lookup (IPI database).

        The IPI Name # corresponding to this performing artist. Values reside in the IPI database.

        :return: the IPI name number
        """
        return self._ipi_name

    @property
    def name(self):
        """
        Performing Artist Name. Alphanumeric.

        Name of a person or full name of a group that has performed the work on a recording or in public. Note that if
        the performer is known by a single name, it should be entered in this field.

        :return: the performer's name
        """
        return self._name

    @property
    def performance_dialect(self):
        """
        Performance Dialect field. Table Lookup (639-2(T)).

        The dialect used in the performance.

        e.g. if the performance is in Mandarin, YUE Cantonese, MIN NAN or HAKKA, then use: CHN, YUH, CFR or HAK.

        :return: the dialect used in the performance
        """
        return self._performance_dialect

    @property
    def performance_language(self):
        """
        Performance Language field. Table lookup (Language Code Table).

        The language used in the performance.

        :return: the language used in the performance
        """
        return self._performance_language


class NPNRecord(NRARecord):
    """
    Represents a CWR Non-Roman Alphabet Publisher Name Record (NPN).

    This record identifies publisher names in non-roman alphabets for this work. The language code is used to identify
    the alphabet. This record can be used to identify the name of the publisher in the preceding SPU/OPU record.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, sequence_n, ip_id, name, language=None):
        super(NPNRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n, language)
        # Publisher info
        self._sequence_n = sequence_n
        self._ip_id = ip_id
        self._name = name

    @property
    def ip_id(self):
        """
        Interested Party # field. Alphanumeric.

        Submitting publisher’s unique identifier for this Publisher.

        :return: the Interested Party ID
        """
        return self._ip_id

    @property
    def name(self):
        """
        Publisher Name field. Alphanumeric.

        The name of this publishing company in non-roman alphabet.

        :return: the name of this publishing company in non-roman alphabet
        """
        return self._name

    @property
    def sequence_n(self):
        """
        Publisher Sequence # field. Numeric.

        A sequential number assigned to the original publishers on this work.

        :return: the publisher sequential id
        """
        return self._sequence_n
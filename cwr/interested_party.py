# -*- coding: utf-8 -*-
from abc import ABCMeta

from cwr.record import TransactionRecord

"""
Interested party model classes.
"""

__author__ = 'Bernardo Martínez Garrido, Borja Garrido Bear'
__license__ = 'MIT'
__status__ = 'Development'


class InterestedParty(object, metaclass=ABCMeta):
    """
    Represents a CWR interested party.
    """

    def __init__(self,
                 ip_n='',
                 ipi_base_n=None,
                 tax_id='',
                 ipi_name=''
                 ):
        # IP info
        self._ip_n = ip_n

        # IPI info
        self._ipi_name = ipi_name
        self._ipi_base_n = ipi_base_n

        # Other info
        self._tax_id = tax_id

    @property
    def ip_n(self):
        """
        Interested Party Number field. Alphanumeric.

        Unique ID given to the Interested Party by the submitter.

        :return: the Publisher's ID
        """
        return self._ip_n

    @ip_n.setter
    def ip_n(self, value):
        self._ip_n = value

    @property
    def ipi_base_n(self):
        """
        Interested Party IPI Base Number field. Table Lookup (IPI System).

        This number is the unique identifier associated with this IP.

        The IP Base Number is a unique identifier allocated automatically by
        the IPI System to each interested party (IP), being either a natural
        person or legal entity.

        The number consists of 13 characters: letter i (I), hyphen (-), nine
        digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus
        10, I weight = 2, adapted from ISO 7064). You can find more
        information in the CISAC web site.

        :return: the Publisher IPI base number
        """
        return self._ipi_base_n

    @ipi_base_n.setter
    def ipi_base_n(self, value):
        self._ipi_base_n = value

    @property
    def ipi_name_n(self):
        """
        Interested Party IPI Name # field. Table Lookup (IPI).

        The IPI number assigned to this publisher with 2 leading zero’s or the
        IPI Name #.

        :return: the Interested Party IPI name number
        """
        return self._ipi_name

    @ipi_name_n.setter
    def ipi_name_n(self, value):
        self._ipi_name = value

    @property
    def tax_id(self):
        """
        Tax ID number field. Alphanumeric.

        The number used to identify this Interested Party for tax reporting.

        :return: the Interested Party Tax ID
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, value):
        self._tax_id = value


class InterestedPartyRecord(TransactionRecord, metaclass=ABCMeta):
    """
    Represents a CWR Interested Party Record.

    This is meant to be used for Publisher and Writer records.
    """

    def __init__(self,
                 record_type='',
                 transaction_sequence_n=0,
                 record_sequence_n=0,
                 first_recording_refusal='U',
                 usa_license='',
                 pr_society=None,
                 pr_ownership_share=0,
                 mr_society=None,
                 mr_ownership_share=0,
                 sr_society=None,
                 sr_ownership_share=0
                 ):
        """
        Constructs an InterestedPartyRecord.
        """
        super(InterestedPartyRecord, self).__init__(
            record_type,
            transaction_sequence_n,
            record_sequence_n
        )
        # Flags
        self._first_recording_refusal = first_recording_refusal
        self._usa_license = usa_license

        # Societies
        self._pr_society = pr_society
        self._mr_society = mr_society
        self._sr_society = sr_society

        # Shares
        self._pr_ownership_share = pr_ownership_share
        self._mr_ownership_share = mr_ownership_share
        self._sr_ownership_share = sr_ownership_share

    @property
    def first_recording_refusal(self):
        """
        First Recording Refusal Indicator field. Flag (Yes/No/Unknown).

        Indicates whether the submitter has refused to give authority for the
        first recording.

        Note that this field is mandatory for registrations with the UK
        societies.

        :return: 'T' if the submitter needs to authorize first recording, 'F'
        if not, 'U' if unknown
        """
        return self._first_recording_refusal

    @first_recording_refusal.setter
    def first_recording_refusal(self, value):
        self._first_recording_refusal = value

    @property
    def mr_ownership_share(self):
        """
        MR Ownership Share field. Numeric Decimal.

        Defines the percentage of the writer’s ownership of the mechanical
        rights to the work.

        This value can range from 0 (0%) to 1 (100%).

        :return: the MR ownership share
        """
        return self._mr_ownership_share

    @mr_ownership_share.setter
    def mr_ownership_share(self, value):
        self._mr_ownership_share = value

    @property
    def mr_society(self):
        """
        Mechanical Rights Affiliation Society field. Table Lookup (Society
        Code Table).

        Number assigned to the Mechanical Rights Society with which the
        Interested Party is affiliated.

        :return: the Interested Party mechanical rights society
        """
        return self._mr_society

    @mr_society.setter
    def mr_society(self, value):
        self._mr_society = value

    @property
    def pr_ownership_share(self):
        """
        PR Ownership Share field. Numeric Decimal.

        Defines the percentage of the writer’s ownership of the performance
        rights to the work.

        This value can range from 0 (0%) to 1 (100%).

        Note that writers both own and collect the performing right interest.

        :return: the PR ownership share
        """
        return self._pr_ownership_share

    @pr_ownership_share.setter
    def pr_ownership_share(self, value):
        self._pr_ownership_share = value

    @property
    def pr_society(self):
        """
        Performing Rights Affiliation Society field. Table Lookup (Society
        Code Table).

        Number assigned to the Performing Rights Society with which the
        Interested Party is affiliated.

        :return: the Interested Party performing rights society
        """
        return self._pr_society

    @pr_society.setter
    def pr_society(self, value):
        self._pr_society = value

    @property
    def sr_ownership_share(self):
        """
        SR Ownership Share field. Numeric Decimal.

        Defines the percentage of the writer’s ownership of the
        synchronization rights to the work.

        This value can range from 0 (0%) to 1 (100%).

        :return: the SR ownership share
        """
        return self._sr_ownership_share

    @sr_ownership_share.setter
    def sr_ownership_share(self, value):
        self._sr_ownership_share = value

    @property
    def sr_society(self):
        """
        Synchronization Rights Affiliation Society field. Table Lookup
        (Society Code Table).

        Number assigned to the Society with which the publisher is affiliated
        for administration of synchronization rights.

        :return: the Publisher's synchronization rights society
        """
        return self._sr_society

    @sr_society.setter
    def sr_society(self, value):
        self._sr_society = value

    @property
    def usa_license(self):
        """
        USA License Indicator field. Table Lookup ('A','B','S').

        This field indicates whether rights for this Interested Party flow
        through ASCAP, BMI, or SESAC for the U.S.

        :return: the first letter of the society with the USA rights
        """
        return self._usa_license

    @usa_license.setter
    def usa_license(self, value):
        self._usa_license = value


class IPTerritoryOfControlRecord(TransactionRecord):
    """
    Represents a CWR Publisher or Writer Territory of Control (SPT/SWT).

    This indicates if a Publisher or Writer has control or not over a
    Territory, and the shares it has on it.

    The control is indicated with the exclusion marker.

    For example, if the Agreement covers all the world except for Europe, two
    AgreementTerritory entities would be used, one indicating that the world
    is included, and another indicating that Europe is excluded.

    It should be noted that a Territory can only be excluded if it is part of
    another Territory which is already included in the Agreement.
    """

    def __init__(self,
                 record_type='',
                 transaction_sequence_n=0,
                 record_sequence_n=0,
                 ip_n='',
                 inclusion_exclusion_indicator=None,
                 tis_numeric_code=None,
                 sequence_n=0,
                 pr_collection_share=0,
                 mr_collection_share=0,
                 sr_collection_share=0,
                 shares_change=False
                 ):
        super(IPTerritoryOfControlRecord, self).__init__(
            record_type,
            transaction_sequence_n,
            record_sequence_n
        )
        # Territory information
        self._tis_numeric_code = tis_numeric_code

        # IP information
        self._ip_n = ip_n
        self._inclusion_exclusion_indicator = inclusion_exclusion_indicator
        self._sequence_n = sequence_n

        # Shares information
        self._pr_collection_share = pr_collection_share
        self._mr_collection_share = mr_collection_share
        self._sr_collection_share = sr_collection_share
        self._shares_change = shares_change

    @property
    def inclusion_exclusion_indicator(self):
        """
        Inclusion/Exclusion Indicator field. Table Lookup ('E'/'I').

        This indicates if the territory is included or excluded.

        The possible values are:
        - 'E' for excluded
        - 'I' for included

        :return: 'E' if the territory is excluded, 'I' otherwise
        """
        return self._inclusion_exclusion_indicator

    @inclusion_exclusion_indicator.setter
    def inclusion_exclusion_indicator(self, value):
        self._inclusion_exclusion_indicator = value

    @property
    def ip_n(self):
        """
        Interested Party # field. Alphanumeric.

        Submitter ID for the Interested Party.

        :return: the Interested Party ID
        """
        return self._ip_n

    @ip_n.setter
    def ip_n(self, value):
        self._ip_n = value

    @property
    def mr_collection_share(self):
        """
        Mechanical Rights Collection Share field. Numeric decimal.

        Defines the percentage of the total royalty distributed for sales of
        CDs, Cassette Tapes, etc. in which the work is included which will be
        collected by (paid to) the publisher.

        This is a value from 0 (0%) to 1 (100%).

        :return: the Mechanical Rights collection share
        """
        return self._mr_collection_share

    @mr_collection_share.setter
    def mr_collection_share(self, value):
        self._mr_collection_share = value

    @property
    def pr_collection_share(self):
        """
        Performing Rights Collection Share field. Numeric decimal.

        Defines the percentage of the total royalty distributed for
        performance of the work which will be collected by (paid to) the
        publisher within the above Territory.

        This is a value from 0 (0%) to 0.5 (50%).

        :return: the Performing Rights collection share
        """
        return self._pr_collection_share

    @pr_collection_share.setter
    def pr_collection_share(self, value):
        self._pr_collection_share = value

    @property
    def sequence_n(self):
        """
        Sequence Number field.

        A sequential number assigned to each territory following a Publisher
        Record.

        :return: the territory sequence number
        """
        return self._sequence_n

    @sequence_n.setter
    def sequence_n(self, value):
        self._sequence_n = value

    @property
    def shares_change(self):
        """
        Shares Change field. Boolean.

        If the shares for the writer interest change as a result of
        subpublication in this territory or for a similar reason, set this
        field to "Y"

        :return: True if the shares change, False otherwise
        """
        return self._shares_change

    @shares_change.setter
    def shares_change(self, value):
        self._shares_change = value

    @property
    def sr_collection_share(self):
        """
        Synchronization Rights Collection Share field. Numeric decimal.

        Defines the percentage of the total royalty distributed for
        Synchronization rights to the work which will be collected by (paid
        to) the publisher.

        This is a value from 0 (0%) to 1 (100%).

        :return: return Synchronization Rights collection share
        """
        return self._sr_collection_share

    @sr_collection_share.setter
    def sr_collection_share(self, value):
        self._sr_collection_share = value

    @property
    def tis_numeric_code(self):
        """
        TIS Numeric Code field. Table Lookup (TIS Code Table).

        This is the ID for the Territory.

        :return: the Territory TIS code
        """
        return self._tis_numeric_code

    @tis_numeric_code.setter
    def tis_numeric_code(self, value):
        self._tis_numeric_code = value


class Publisher(InterestedParty):
    """
    Represents a CWR Publisher.

    This encompasses several types of interested parties, such as
    sub-publisher, original publisher, acquirer or administrator.
    """

    def __init__(self,
                 ip_n='',
                 publisher_name='',
                 ipi_base_n=None,
                 tax_id=None,
                 ipi_name_n=None
                 ):
        super(Publisher, self).__init__(
            ip_n,
            ipi_base_n,
            tax_id,
            ipi_name_n
        )
        self._publisher_name = publisher_name

    @property
    def publisher_name(self):
        """
        Publisher Name field. Alphanumeric.

        The name of this publishing company.

        :return: the Publisher's name
        """
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, value):
        self._publisher_name = value


class PublisherRecord(InterestedPartyRecord):
    """
    Represents a CWR Publisher Record (SPU/OPU).

    This represents the following records:
    - Publisher Controlled By Submitter (SPU)
    - Other Publisher (OPU)

    This contains information about original publishers, income participants,
    sub-publishers, and/or  administrators who are involved in the ownership
    and collection of a work. May they be under control of the submitter or
    not.
    """

    def __init__(self,
                 record_type='',
                 transaction_sequence_n=0,
                 record_sequence_n=0,
                 publisher=None,
                 publisher_sequence_n=0,
                 submitter_agreement_n='',
                 publisher_type=None,
                 publisher_unknown='N',
                 agreement_type=None,
                 international_standard_code='',
                 society_assigned_agreement_n='',
                 pr_society=None,
                 pr_ownership_share=0,
                 mr_society=None,
                 mr_ownership_share=0,
                 sr_society=None,
                 sr_ownership_share=0,
                 special_agreements=None,
                 first_recording_refusal='U',
                 usa_license=''
                 ):
        """
        Constructs a PublisherRecord.

        :param publisher: the publisher information
        :param publisher_sequence_n: the position in the Publisher Chain
        :param submitter_agreement_n: the submitter's id for the agreement
        :param publisher_type: the publisher role in the agreement
        :param publisher_unknown: publisher unknown flag
        :param agreement_type: the type of agreement
        :param international_standard_code: ISAC for the publisher's agreement
        :param society_assigned_agreement_n: ID for the Agreement given by a
        society
        :param pr_society: Performing Rights society
        :param pr_ownership_share: Performing Rights share
        :param mr_society: Mechanical Rights society
        :param mr_ownership_share: Mechanical Rights share
        :param sr_society: Synchronization Rights society
        :param sr_ownership_share: Synchronization Rights share
        """
        super(PublisherRecord, self).__init__(
            record_type,
            transaction_sequence_n,
            record_sequence_n,
            first_recording_refusal,
            usa_license,
            pr_society,
            pr_ownership_share,
            mr_society,
            mr_ownership_share,
            sr_society,
            sr_ownership_share
        )

        # Publisher info
        self._publisher = publisher
        self._publisher_type = publisher_type
        self._publisher_unknown = publisher_unknown

        # Agreement info
        self._submitter_agreement_n = submitter_agreement_n
        self._society_assigned_agreement_n = society_assigned_agreement_n
        self._agreement_type = agreement_type
        self._international_standard_code = international_standard_code
        self._special_agreements = special_agreements

        # Other info
        self._publisher_sequence_n = publisher_sequence_n

    @property
    def agreement_type(self):
        """
        Agreement Type field. Table Lookup (Agreement Type Table).

        Code defining the category of the agreement.

        :return: the Agreement type
        """
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, value):
        self._agreement_type = value

    @property
    def international_standard_code(self):
        """
        International Standard Agreement Code field.

        A unique number assigned to this agreement under which this publisher
        share is to be administered.

        :return: the agreement ISAC
        """
        return self._international_standard_code

    @international_standard_code.setter
    def international_standard_code(self, value):
        self._international_standard_code = value

    @property
    def publisher(self):
        """
        Publisher.

        Info for the Publisher.

        :return: the publisher
        """
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def publisher_sequence_n(self):
        """
        Publisher Sequence Number field. Numeric.

        Position in the Publisher Chain for this Publisher.

        :return: the Publisher sequence number in the chain
        """
        return self._publisher_sequence_n

    @publisher_sequence_n.setter
    def publisher_sequence_n(self, value):
        self._publisher_sequence_n = value

    @property
    def publisher_type(self):
        """
        Publisher Type field. Table Lookup (Publisher Type Table).

        Role played by this publisher in this work.

        :return: the Publisher's role
        """
        return self._publisher_type

    @publisher_type.setter
    def publisher_type(self, value):
        self._publisher_type = value

    @property
    def publisher_unknown(self):
        """
        Publisher Unknown Indicator. Flag (Yes/No/Unknown).

        Indicates if the name of this publisher is unknown.

        Note that this attribute must be Unknown for SPU records.

        For OPU records, this field must be set to True if the Publisher Name
        is blank.

        :return: True if the Publisher is unknown, False otherwise, Unknown in
        special cases
        """
        return self._publisher_unknown

    @publisher_unknown.setter
    def publisher_unknown(self, value):
        self._publisher_unknown = value

    @property
    def special_agreements(self):
        """
        Special Agreements Indicator. Table Lookup (Special Agreement
        Indicator Table).

        Indicates publisher claiming reversionary rights.

        Note that this flag only applies to societies that recognize
        reversionary rights (for example, SOCAN).

        :return: the Special Agreements indicator
        """
        return self._special_agreements

    @special_agreements.setter
    def special_agreements(self, value):
        self._special_agreements = value

    @property
    def submitter_agreement_n(self):
        """
        Submitter Agreement Number field.

        This points to an agreement between this publisher and another
        publisher acting as a domestic or foreign administrator and it is your
        internal number.

        :return: the Submitter Agreement number
        """
        return self._submitter_agreement_n

    @submitter_agreement_n.setter
    def submitter_agreement_n(self, value):
        self._submitter_agreement_n = value

    @property
    def society_assigned_agreement_n(self):
        """
        Society-assigned Agreement Number field. Alphanumeric.

        The agreement number assigned by the society of the sub-publisher.

        :return: the society-assigned Agreement number
        """
        return self._society_assigned_agreement_n

    @society_assigned_agreement_n.setter
    def society_assigned_agreement_n(self, value):
        self._society_assigned_agreement_n = value


class PublisherChain(object):
    """
    Represents a CWR Publisher Chain.

    This stores the Publishers of a work, along their territories.

    While this is called a chain, due to it being stored in file as a list of
    linked publishers, it is actually
    a tree.

    As a list it can be defined as:
    [SPU, SPT*, [SPU, SPT*]?, [SPU, SPT*, [SPU, SPT*]?]*]

    It should be noted this is recursive, using as base 'SPU, SPT*,
    [SPU, SPT*]?', we have: [BASE, BASE*]

    The first SPU in the chain is original publisher or income participant,
    followed by his territories of shares
    collection.

    Following it there can exist another SPU, and his territories,
    representing the local administrator.

    After this the sub-publishers appear, repeating the same pattern.

    The role of each Publisher is indicated by the Publisher type field.
    """

    def __init__(self,
                 original_publisher
                 ):
        self._original_publisher = original_publisher

    @property
    def original_publisher(self):
        """
        Original publisher.

        This is the original publisher of the work under the agreement.

        In the chain this is the first Publisher, and also the root Publisher
        in the tree.

        :return: the original Publisher
        """
        return self._original_publisher

    @original_publisher.setter
    def original_publisher(self, value):
        self._original_publisher = value


class PublisherChainNode(object):
    """
    Represents a node in the Publisher Chain.

    A Publisher in the chain contains data about itself and the territories
    where it collects shares.
    """

    def __init__(self,
                 publisher,
                 administrator=None,
                 subpublishers=None,
                 territories=None
                 ):
        self._publisher = publisher
        self._administrator = administrator

        if subpublishers is None:
            self._subpublishers = []
        else:
            self._subpublishers = subpublishers

        if territories is None:
            self._territories = []
        else:
            self._territories = territories

    @property
    def administrator(self):
        """
        Regional administrator.

        This is a PublisherChainNode.

        :return: the regional administrator for this Publisher
        """
        return self._administrator

    @administrator.setter
    def administrator(self, value):
        self._administrator = value

    @property
    def publisher(self):
        """
        Publisher Record.

        This is the Publisher Record for this node.

        :return: general information about the Publisher
        """
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def subpublishers(self):
        """
        Sub-publishers list.

        This is a collection of PublisherChainNode instances.

        :return: the collection of sub-publishers
        """
        return self._subpublishers

    @subpublishers.setter
    def subpublishers(self, value):
        self._subpublishers = value

    @property
    def territories(self):
        """
        Publisher territories.

        This is a collection IPTerritory instances.

        :return: territories under control of the Publisher
        """
        return self._territories

    @territories.setter
    def territories(self, value):
        self._territories = value


class Writer(InterestedParty):
    """
    Represents a CWR writer.

    This can be a Writer Controlled by Submitter (SWR) or Other Writer (OWR).
    """

    def __init__(self,
                 ip_n='',
                 personal_number=0,
                 ipi_base_n=None,
                 writer_first_name='',
                 writer_last_name='',
                 tax_id=None,
                 ipi_name_n=None
                 ):
        super(Writer, self).__init__(
            ip_n,
            ipi_base_n,
            tax_id,
            ipi_name_n
        )

        # Writer information
        self._writer_first_name = writer_first_name
        self._writer_last_name = writer_last_name
        self._personal_number = personal_number

    @property
    def personal_number(self):
        """
        Personal Number field. Numeric.

        This field contains the personal number assigned to this individual in
        the country of residence. For Sweden, it has the format YYMMDD9999.

        :return: the Writer country-based personal number
        """
        return self._personal_number

    @personal_number.setter
    def personal_number(self, value):
        self._personal_number = value

    @property
    def writer_first_name(self):
        """
        Writer First Name field. Alphanumeric.

        The first name of the writer.

        :return: the Writer first name
        """
        return self._writer_first_name

    @writer_first_name.setter
    def writer_first_name(self, value):
        self._writer_first_name = value

    @property
    def writer_last_name(self):
        """
        Writer Last Name field. Alphanumeric.

        The last name of the writer. If you do not have the ability to
        separate the last name from the first name, then you may include both
        the last and first name in this field—pr separated by a comma.

        :return: the Writer last name
        """
        return self._writer_last_name

    @writer_last_name.setter
    def writer_last_name(self, value):
        self._writer_last_name = value


class PublisherForWriterRecord(TransactionRecord):
    """
    Represents a CWR Publisher For Writer (PWR) record.

    This record is used to indicate the publisher that represents the writer
    designated on the previous SWR record for writers that are published
    (total writer ownership shares for each right are less than 100%).

    Only Writers under control of the Publisher use these records.

    The record serves in case that two or more writers for a work have an
    agreement with the same original publisher, so it is possible to record
    each Society-Assigned Agreement Number / Submitter Agreement Number in the
    PWR record that links that writer to the original publisher.

    It is the society of the original publisher that assigns the
    society-assigned agreement number to the writer to publisher agreement.
    """

    def __init__(self,
                 record_type='',
                 transaction_sequence_n=0,
                 record_sequence_n=0,
                 publisher_ip_n='',
                 publisher_name='',
                 writer_ip_n='',
                 submitter_agreement_n=None,
                 society_assigned_agreement_n=None
                 ):
        super(PublisherForWriterRecord, self).__init__(
            record_type,
            transaction_sequence_n,
            record_sequence_n
        )
        # Parties IDs
        self._publisher_ip_n = publisher_ip_n
        self._writer_ip_n = writer_ip_n
        self._publisher_name = publisher_name

        # Agreement IDs
        self._submitter_agreement_n = submitter_agreement_n
        self._society_assigned_agreement_n = society_assigned_agreement_n

    @property
    def publisher_ip_n(self):
        """
        Publisher IP Number field. Alphanumeric.

        The publisher interested party number pointing back to the SPU record
        for the original publisher/income participant representing this
        writer.

        :return: the Publisher id
        """
        return self._publisher_ip_n

    @publisher_ip_n.setter
    def publisher_ip_n(self, value):
        self._publisher_ip_n = value

    @property
    def society_assigned_agreement_n(self):
        """
        Society-Assigned Agreement Number field. Alphanumeric.

        The unique number assigned to this agreement by the society.

        :return: the society-given agreement ID
        """
        return self._society_assigned_agreement_n

    @society_assigned_agreement_n.setter
    def society_assigned_agreement_n(self, value):
        self._society_assigned_agreement_n = value

    @property
    def submitter_agreement_n(self):
        """
        Submitter Agreement Number field. Alphanumeric.

        The Agreement's ID.

        :return: the agreement ID
        """
        return self._submitter_agreement_n

    @submitter_agreement_n.setter
    def submitter_agreement_n(self, value):
        self._submitter_agreement_n = value

    @property
    def writer_ip_n(self):
        """
        Writer IP Number field. Alphanumeric.

        The writer interested party number pointing back to the SWR record in
        an explicit link.

        :return: the writer ID
        """
        return self._writer_ip_n

    @writer_ip_n.setter
    def writer_ip_n(self, value):
        self._writer_ip_n = value

    @property
    def publisher_name(self):
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, value):
        self._publisher_name = value


class WriterRecord(InterestedPartyRecord):
    """
    Represents a CWR Writer Record (SWR/OWR)

    This is for Writer Controlled By Submitter (SWR) and Other Writer (OWR)
    records.

    These contain all the information available to the submitter for a Writer.
    """

    def __init__(self,
                 record_type='',
                 transaction_sequence_n=0,
                 record_sequence_n=0,
                 writer=None,
                 writer_designation=None,
                 work_for_hire=False,
                 writer_unknown='F',
                 reversionary='U',
                 first_recording_refusal='U',
                 usa_license='',
                 pr_society=None,
                 pr_ownership_share=0,
                 mr_society=None,
                 mr_ownership_share=0,
                 sr_society=None,
                 sr_ownership_share=0):
        super(WriterRecord, self).__init__(
            record_type,
            transaction_sequence_n,
            record_sequence_n,
            first_recording_refusal,
            usa_license,
            pr_society,
            pr_ownership_share,
            mr_society,
            mr_ownership_share,
            sr_society,
            sr_ownership_share
        )
        # Writer info
        self._writer = writer

        # Writer role
        self._writer_designation = writer_designation
        self._writer_unknown = writer_unknown
        self._work_for_hire = work_for_hire

        # Other info
        self._reversionary = reversionary

    @property
    def reversionary(self):
        """
        Reversionary Indicator field. Flag (Yes/No/Unknown).

        Indicates publisher claiming reversionary rights.

        Note that only some societies, such as SOCAN, recognize reversionary
        rights.

        :return: 'T' if the work is under reversionary provisions, 'F' if not,
        'U' if unknown
        """
        return self._reversionary

    @reversionary.setter
    def reversionary(self, value):
        self._reversionary = value

    @property
    def work_for_hire(self):
        """
        Work For Hire Indicator field. Boolean.

        Indicates whether or not this work was written for hire.

        :return: True if this work was written for hire, False otherwise
        """
        return self._work_for_hire

    @work_for_hire.setter
    def work_for_hire(self, value):
        self._work_for_hire = value

    @property
    def writer(self):
        """
        The Writer information.

        This is a Writer instance.

        :return: the Writer available information
        """
        return self._writer

    @writer.setter
    def writer(self, value):
        self._writer = value

    @property
    def writer_designation(self):
        """
        Writer Designation Code field. Table Lookup (Writer Designation
        Table).

        Code defining the role the writer played in the composition of the
        work.

        This attribute is required for record type SWR and optional for record
        type OWR.

        :return: the Writer designation code
        """
        return self._writer_designation

    @writer_designation.setter
    def writer_designation(self, value):
        self._writer_designation = value

    @property
    def writer_unknown(self):
        """
        Writer Unknown Indicator field. Flag (Yes/No/Unknown).

        Indicates if the name of this writer is unknown. Note that this field
        must be left blank for SWR records.

        For OWR records, this field must be set to 'Y' if the Writer Last Name
        is blank.

        :return: 'Y' if the Writer is unknown, 'F' otherwise, 'U' in special
        cases
        """
        return self._writer_unknown

    @writer_unknown.setter
    def writer_unknown(self, value):
        self._writer_unknown = value

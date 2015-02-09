# -*- encoding: utf-8 -*-
from abc import ABCMeta

"""
Transaction model classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class AgreementTransaction(object):
    """
    Represents a CWR Agreement Transaction (AGR).
    """

    def __init__(self, agreement, territories):
        self._agreement = agreement
        self._territories = territories

    @property
    def agreement(self):
        """
        Agreement Supporting Work Registration field.

        The Agreement record in the transaction.

        :return:
        """
        return self._agreement

    @property
    def territories(self):
        """
        The territories affected by this Agreement and their IPAs.

        This is a collection if TerritoryWithIPAs.

        :return: the territories affected by this Agreement and their IPAs
        """
        return self._territories


class WorkTransaction(object):
    """
    Represents a CWR Work Transaction.

    These can be a New Work Registration (NWR), Revised Registration (REV), Notification of ISWC assign to a work (ISW)
    or Existing work which is in Conflict with a Work Registration (EXC).
    """

    def __init__(self, entire_work_title=None, original_work_title=None, recording=None, alternate_titles=None,
                 publishers_controlled=None, publishers_other=None, writers_controlled=None,
                 writers_other=None, performers=None, origins=None, inst_summaries=None,
                 inst_details=None, components=None, info=None):
        self._entire_work_title = entire_work_title
        self._original_work_title = original_work_title
        self._recording = recording
        self._info = info

        if alternate_titles is None:
            self._alternate_titles = []
        else:
            self._alternate_titles = alternate_titles

        if publishers_controlled is None:
            self._publishers_controlled = []
        else:
            self._publishers_controlled = publishers_controlled

        if publishers_other is None:
            self._publishers_other = []
        else:
            self._publishers_other = publishers_controlled

        if writers_controlled is None:
            self._writers_controlled = []
        else:
            self._writers_controlled = writers_controlled

        if writers_other is None:
            self._writers_other = []
        else:
            self._writers_other = writers_other

        if performers is None:
            self._performers = []
        else:
            self._performers = performers

        if origins is None:
            self._origins = []
        else:
            self._origins = origins

        if inst_summaries is None:
            self._inst_summaries = []
        else:
            self._inst_summaries = inst_summaries

        if inst_details is None:
            self._inst_details = []
        else:
            self._inst_details = inst_details

        if components is None:
            self._components = []
        else:
            self._components = components

    @property
    def alternate_titles(self):
        """
        Alternate Titles field.

        Returns the Alternate Titles for the Work.

        :return: the Alternate Title for the Work
        """
        return self._alternate_titles

    @property
    def components(self):
        """
        Components field.

        Returns the Work Components.

        :return: the Work Components
        """
        return self._components

    @property
    def entire_work_title(self):
        """
        Entire Work Title field.

        Returns an Entire Work Title for the Work.

        :return: an Entire Work Title for the Work
        """
        return self._entire_work_title

    @property
    def info(self):
        """
        Additional Info field.

        Contains information such as comments or the Society number.

        This is a collection of strings.

        :return: additional info for the work
        """
        return self._info

    @property
    def inst_details(self):
        """
        Instrumentation Details field.

        Returns the Work Instrumentation Details.

        :return: the Work Instrumentation Details
        """
        return self._inst_details

    @property
    def inst_summaries(self):
        """
        Instrumentation Summaries field.

        Returns the Work Instrumentation Summaries.

        :return: the Work Instrumentation Summaries
        """
        return self._inst_summaries

    @property
    def original_work_title(self):
        """
        Original Work Title field.

        Returns an Original Work Title for the Work.

        :return: an Original Work Title for the Work
        """
        return self._original_work_title

    @property
    def origins(self):
        """
        Work Origins field.

        Returns the Work Origins.

        :return: the Work Origins
        """
        return self._origins

    @property
    def performers(self):
        """
        Performing Artists field.

        The Performing Artists.

        :return: the Performing Artists
        """
        return self._performers

    @property
    def publishers_controlled(self):
        """
        Publisher Controlled by Submitter field.

        List all publishers controlled by the submitter.  This record is mandatory if writer ownership shares are less
        than 100%.

        This is a collection of PublisherWithTerritories.

        :return: the publishers controlled by the submitter
        """
        return self._publishers_controlled

    @property
    def publishers_other(self):
        """
        Other Publishers field.

        Lists all the publishers not controlled by the submitter.

        This is just a collection of Publishers.

        :return: the Publishers not controlled by the submitter
        """
        return self._publishers_other

    @property
    def recording(self):
        """
        Recording field.

        Recording status.

        :return: the Recording status
        """
        return self._recording

    @property
    def writers_controlled(self):
        """
        Writers Controlled by Submitter field.

        Lists all the Writers controlled by the submitter.

        This is a collection of WriterWithTerritoryPublishers.

        :return: all the Writers controlled by the submitter along his Territories and Publishers
        """
        return self._writers_controlled

    @property
    def writers_other(self):
        """
        Other Writers field.

        List all the Writers not controlled by the submitter.

        This is just a collection of Writers.

        :return: the Writers not controlled by the submitter
        """
        return self._writers_other


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


class IPTerritoryOfControl(object):
    """
    Represents a CWR Interested Party Territory of Control.

    This is for the Publisher Territory of Control (SPT) and Writer Territory of Control (SWT) transactions.

    This indicates the relationship between an Agreement and a Territory. More specifically, it indicates if a territory
    is included or excluded from the Agreement.

    For example, if the Agreement covers all the world except for Europe, two AgreementTerritory entities would be used,
    one indicating that the world is included, and another indicating that Europe is excluded.

    It should be noted that a Territory can only be excluded if it is part of another Territory which is already
    included in the Agreement.

    Territories are identified by a four digit numeric codes. These can be found at http://www.cisac.org/.
    """

    def __init__(self, ip_id, included, tis_numeric_code, pr_col_share=None, mr_col_share=None, sr_col_share=None,
                 shares_change=None):
        self._ip_id = ip_id
        self._included = included
        self._tis_numeric_code = tis_numeric_code
        self._pr_col_share = pr_col_share
        self._mr_col_share = mr_col_share
        self._sr_col_share = sr_col_share
        self._shares_change = shares_change

    @property
    def included(self):
        """
        Inclusion/ Exclusion Indicator field.

        A True value indicates this Territory is included. A False value indicates it is excluded.

        :return: True if the Territory is included, False if it is excluded
        """
        return self._included

    @property
    def ip_id(self):
        """
        Interested Party # field.

        Submitting publisher’s unique identifier for this Interested Party.

        :return: the Interested Party id
        """
        return self._ip_id

    @property
    def mr_col_share(self):
        """
        MR Collection Share field.

        Defines the percentage of the total royalty distributed for sales of CDs, Cassette Tapes, etc. in which the work
        is included which will be collected by (paid to) the publisher. It can be a range from 0 to 100.00

        :return: the MR collection share
        """
        return self._mr_col_share

    @property
    def pr_col_share(self):
        """
        PR Collection Share field.

        Defines the percentage of the total royalty distributed for performance of the work which will be collected by
        (paid to) the publisher within the above Territory.  It can be a range from 0 to 50.00.

        :return: the PR collection share
        """
        return self._pr_col_share

    @property
    def shares_change(self):
        """
        Shares change field.

        If the shares for the writer interest change as a result of subpublication in this territory or for a similar
        reason, set this field to "Y"

        :return: True if the shares change, False otherwise
        """
        return self._shares_change

    @property
    def sr_col_share(self):
        """
        SR Collection Share field.

        Defines the percentage of the total royalty distributed for Synchronization rights to the work which will be
        collected by (paid to) the publisher. It can be a range from 0 to 100.00.

        :return: return SR collection share
        """
        return self._sr_col_share

    @property
    def tis_numeric_code(self):
        """
        TIS Numeric Code field.

        This is the ID for the Territory.

        :return: the Territory TIS code
        """
        return self._tis_numeric_code


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


class TerritoryWithIPAs(object):
    """
    Represents a Territory and its IPAs
    """

    def __init__(self, territory, ipas):
        self._territory = territory
        self._ipas = ipas

    @property
    def ipas(self):
        """
        The Interested Parties of the Agreement which affect this Territory.

        :return: the Territory IPAs
        """
        return self._ipas

    @property
    def territory(self):
        """
        The Territory.

        :return: the Territory
        """
        return self._territory


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
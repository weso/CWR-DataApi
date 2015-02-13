# -*- encoding: utf-8 -*-

from commonworks.file import Record

"""
Agreement model classes.

These classes are used to represent an Agreement Transaction (AGR), which consists on an Agreement Record with the
details of this Agreement, and a collection of Territories and their Interested parties.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class AgreementInterestedParty(Record):
    """
    Represents a CWR Interested Party for the Agreement (IPA).

    This contains information on the interested parties that concluded the agreement and on the shares they have agreed
    to assign through the agreement.
    """

    def __init__(self, prefix, ip_id, last_name, agreement_role_code,
                 writer_name='', ipi=None, cae_ipi_name=None,
                 pr_society=None, pr_share=0, mr_society=None, mr_share=0, sr_society=None, sr_share=0):
        """
        Constructs an AgreementInterestedParty.

        :param prefix: the record prefix
        :param ip_id: the interested party ID
        :param last_name: the writer last name or the publisher name
        :param agreement_role_code: the role in the agreement
        :param writer_name: the writer name
        :param ipi: IPI code
        :param cae_ipi_name: CAE/IPI Name number
        :param pr_society: performing rights society
        :param pr_share: performing rights share
        :param mr_society: mechanization rights society
        :param mr_share: mechanization rights share
        :param sr_society: synchronization rights society
        :param sr_share: synchronization rights share
        """
        super(AgreementInterestedParty, self).__init__(prefix)
        # Agreement and Interested Party relationship
        self._ip_id = ip_id
        self._agreement_role_code = agreement_role_code
        self._cae_ipi_name = cae_ipi_name

        # Interested Party info
        self._ipi = ipi
        self._last_name = last_name
        self._writer_name = writer_name

        # Performing Rights info
        self._pr_society = pr_society
        self._pr_share = pr_share

        # Mechanical Rights info
        self._mr_society = mr_society
        self._mr_share = mr_share

        # Synchronization Rights info
        self._sr_society = sr_society
        self._sr_share = sr_share

    @property
    def agreement_role_code(self):
        """
        Agreement Role Code field. Table Lookup (Agreement Role Code).

        This code is used to indicate the party's role in the Agreement.

        In CWR v2.1 the two available roles are assignor or acquirer.

        :return: the role of the Interested Party on the Agreement
        """
        return self._agreement_role_code

    @property
    def cae_ipi_name(self):
        """
        Interested Party CAE/IPI Name number field. Table Lookup (IPI Database).

        The CAE number (IP name number) assigned to this interested party with 2 leading zero’s or the IPI Name number.

        These values reside in the IPI Database.

        :return: the CAE or IPI name number for this interested party
        """
        return self._cae_ipi_name

    @property
    def ip_id(self):
        """
        Interested Party Number field. Alphanumeric.

        This is the unique ID given by the submitter to the Interested Party.

        :return: ID for the interested party
        """
        return self._ip_id

    @property
    def ipi(self):
        """
        IPI Base Number field. Table Lookup (CISAC CIS).

        The unique identifier associated with this interested party. IPI numbering is a sub-system of the CISAC
        Common Information System.

        :return: IPI base number for the interested party
        """
        return self._ipi

    @property
    def last_name(self):
        """
        Interested Party Last Name field. Alphanumeric.

        The last name of the writer, or the name of the publisher.

        Note that if the submitter does not have the ability to split first and last names of writers, the entire name
        should be entered in this field in the format “Last Name, First Name” including the comma after the last name.

        :return: the writer last name or the publisher name
        """
        return self._last_name

    @property
    def mr_share(self):
        """
        MR Share field. Numeric.

        The percentage of the mechanical rights acquired or retained by this Interested Party under this Agreement.

        This value is a float which can range from 0 (0%) to 1 (100%).

        By default this value is 0.

        :return: the mechanical of the performing rights for the Interested Party
        """
        return self._mr_share

    @property
    def mr_society(self):
        """
        MR Affiliation Society field. Table Lookup (Society Code Table).

        The mechanical rights society to which this Interested Party belongs.

        :return: the Interested Party's mechanical rights society
        """
        return self._mr_society

    @property
    def pr_share(self):
        """
        PR Share field. Numeric.

        The percentage of the performing rights acquired or retained by this Interested Party under this Agreement.

        This value is a float which can range from 0 (0%) to 1 (100%).

        By default this value is 0.

        :return: the percentage of the performing rights for the Interested Party
        """
        return self._pr_share

    @property
    def pr_society(self):
        """
        PR Affiliation Society field. Table Lookup (Society Code Table).

        The performing rights society to which this Interested Party belongs.

        This is only required if the PR Share is greater than zero.

        :return: the Interested Party's performing rights society
        """
        return self._pr_society

    @property
    def sr_share(self):
        """
        SR Share field. Numeric.

        The percentage of the synchronization rights acquired or retained by this Interested Party under this Agreement.

        This value is a float which can range from 0 (0%) to 1 (100%).

        By default this value is 0.

        :return: the percentage of the synchronization rights for the Interested Party
        """
        return self._sr_share

    @property
    def sr_society(self):
        """
        SR Affiliation Society field. Table Lookup (Society Code Table).

        The synchronization rights society to which this Interested Party belongs.

        :return: the Interested Party's synchronization rights society
        """
        return self._sr_society

    @property
    def writer_name(self):
        """
        Interested Party Writer First Name field. Alphanumeric.

        If the interested party is a writer, provide his/her first and middle names.

        :return: the Writer's first and middle names
        """
        return self._writer_name


class AgreementRecord(Record):
    """
    Represents a CWR Agreement Record (AGR).

    This is the header record of an Agreement Transaction, containing the specific information which defines the
    agreement, such as it's unique codes, but missing any information defining relationships, such as the works
    covered, or the interested parties.

    The relationships of the Agreement should be on a Transaction class.

    The Agreement Record contains a Submitter Agreement Number that is used to link the agreement to a work
    registration. If a society has assigned an agreement number, then it too can be used as the link.
    """

    def __init__(self, prefix, agreement_id, agreement_type, start_date, prior_royalty_status,
                 post_term_collection_status, works_number, society_agreement_id='',
                 international_standard_code='', sales_manufacture_clause='S',
                 end_date=None, signature_date=None, retention_end_date=None, prior_royalty_start_date=None,
                 post_term_collection_end_date=None,
                 shares_change=False, advance_given=False):
        """
        Constructs an Agreement Record.

        :param prefix: the record prefix
        :param agreement_id: the submitter's ID for the agreement
        :param agreement_type: the type of agreement
        :param start_date: starting date for the agreement
        :param prior_royalty_status: the status of the royalties before the agreement
        :param post_term_collection_status: if and how the the acquirer can get royalties after the retention end
        :param works_number: number of works in the agreement
        :param society_agreement_id: ID given by a society for the agreement
        :param international_standard_code: ISA ID for the agreement
        :param sales_manufacture_clause: indicates if the rights are for sale or manufacture
        :param end_date: end date for the agreement
        :param signature_date: date of signature of the agreement
        :param retention_end_date: end date of the rights retention
        :param prior_royalty_start_date: royalties acquisition date previous to the start of the agreement
        :param post_term_collection_end_date: end of royalties after the agreement end
        :param shares_change: indicates if the writer's shares can change
        :param advance_given: indicates if an advancement has been paid
        """
        super(AgreementRecord, self).__init__(prefix)
        # Agreement identification data
        self._agreement_id = agreement_id
        self._society_agreement_id = society_agreement_id
        self._international_standard_code = international_standard_code
        self._agreement_type = agreement_type

        # Agreement dates
        self._start_date = start_date
        self._end_date = end_date

        # Royalty info
        self._prior_royalty_status = prior_royalty_status
        self._prior_royalty_start_date = prior_royalty_start_date

        # Post-term collection info
        self._post_term_collection_status = post_term_collection_status
        self._post_term_collection_end_date = post_term_collection_end_date

        # Enumeration fields
        self._sales_manufacture_clause = sales_manufacture_clause

        # Boolean flags
        self._shares_change = shares_change
        self._advance_given = advance_given

        # Other dates
        self._signature_date = signature_date
        self._retention_end_date = retention_end_date

        # Other info
        self._works_number = works_number

    @property
    def advance_given(self):
        """
        Advance Given field. Boolean.

        Indicates if an advance has been paid for this agreement.

        :return: True if an advance has been given, False otherwise
        """
        return self._advance_given

    @property
    def agreement_id(self):
        """
        Submitter Agreement Number field. Alphanumeric.

        This is the unique ID given by the submitter to the Agreement.

        :return: the submitter's ID for this Agreement
        """
        return self._agreement_id

    @property
    def agreement_type(self):
        """
        Agreement Type field. Table lookup (Agreement Type Table).

        Defines the category of the agreement.

        :return: the Agreement's type
        """
        return self._agreement_type

    @property
    def end_date(self):
        """
        Agreement End Date field. Date.

        This is the date when the transfer of rights to the acquiring party ends.

        There may be provisions within the contract (as described in other attributes such as collection end date)
        which have impact on entitlements.

        This attribute is optional, and by default is None.

        :return: the end date for the Agreement
        """
        return self._end_date

    @property
    def international_standard_code(self):
        """
        International Standard Agreement Code field. Alphanumeric.

        If an International Standard Agreement Code exists, it is indicated here.

        As the ISA code may not exist when making the Agreement, this attribute is by default an empty string.

        :return: the ISA code for this Agreement
        """
        return self._international_standard_code

    @property
    def post_term_collection_end_date(self):
        """
        Post-term Collection End Date field. Date.

        Indicates up to which date the acquiring party has right to collect money after the Retention End Date, if it
        exists, or the Agreement End Date, if the first does not exist.

        For this date to be valid, one of those two dates should exist and be previous to this one.

        Also, if the Post-Term Collection Status is not set to 'D' for date this attribute should be ignored.

        :return: the collection ending date after the retention or agreement end
        """
        return self._post_term_collection_end_date

    @property
    def post_term_collection_status(self):
        """
        Post-term Collection Status field. Alphanumeric.

        Indicates if the acquiring party has rights to collect money after the Retention End Date, if it exists, or
        the Agreement End Date, if the first does not exist.

        There are three possible values:
        - 'N' for no, if the acquiring party has no rights.
        - 'O' for open-ended, if the acquiring party can collect until further notification.
        - 'D' for date, if the acquiring party an collect until a specific date. In this case the date should be
        specified in the Post-term Collection End Date attribute.

        :return: if and which type of collection is allowed after the end of the agreement or the retention
        """
        return self._post_term_collection_status

    @property
    def prior_royalty_status(self):
        """
        Prior Royalty Status field. Alphanumeric.

        Indicates if the acquiring party has rights to collection money before the Agreement Start Date.

        There are three possible values:
        - 'N' for none. If the acquiring party has no rights.
        - 'A' for all. If the acquiring party has all the rights.
        - 'D' for date. If the acquiring party can start collection from a specific date. In this case the date
        should be specified in the Prior Royalty Start Date field.

        :return: if and which collection rights has the acquirer before the start of the agreement
        """
        return self._prior_royalty_status

    @property
    def prior_royalty_start_date(self):
        """
        Prior Royalty Start Date field. Date.

        Indicates from which date the acquiring party has right to collect money before the Agreement Start Date.

        This date field indicates from what earning dates the acquiring party can begin collecting monies if the
        acquiring party can begin collecting before the agreement start date of this agreement.

        If the Prior Royalty Status is not set to 'D' this attribute should be ignored.

        return the collection start date before the start of the Agreement
        """
        return self._prior_royalty_start_date

    @property
    def retention_end_date(self):
        """
        Retention End Date field. Date.

        If the agreement specifies that the collection rights for some or all of the works are retained beyond the end
        of the agreement, then the end date of this retention period is indicated here. It is not necessary to specify
        any Retention End Date if it doesn't exist on the Agreement.

        This date supercedes the function of the Agreement End Date when a retention period is part of the agreement.

        For this attribute to be valid the Retention End Date must be equal to or later than the Agreement End Date.

        :return: the collection end date after the end of the Agreement
        """
        return self._retention_end_date

    @property
    def sales_manufacture_clause(self):
        """
        Sales/ Manufacture Clause field. Table Lookup ('S'/'M').

        A marker which shows whether the acquiring party has acquired rights either for products manufactured or for
        products sold in the territories in agreement.

        Only two values are allowed according to BIEM/CISAC-rules:
        - 'S' for Sales Clause. A stipulation which lays down that the acquiring party has acquired rights for products sold
        in the territories in agreement irrespective of the country of manufacture.
        - 'M' for Manufacture Clause. A stipulation which lays down that the acquiring party has acquired rights for products
        manufactured in the territories in agreement irrespective of the country of sale.

        This attribute is by default set to 'S'.

        :return: a marker indicating if the acquiring party has rights for manufacturing or for sales
        """
        return self._sales_manufacture_clause

    @property
    def shares_change(self):
        """
        Shares Change field. Boolean.

        Indicates if the shares assigned to the writers can change as a result of sub-publication or similar.

        :return: True if the writer shares can change, False otherwise
        """
        return self._shares_change

    @property
    def signature_date(self):
        """
        Date of Signature of Agreement field. Date.

        The date when the written form of the agreement (the contract) was signed.

        :return the date when the agreement contract was signed
        """
        return self._signature_date

    @property
    def society_agreement_number(self):
        """
        Society-assigned Agreement Number field. Alphanumeric.

        Identificator given by a Society to the Agreement.

        As this value is generally not known when the agreement is submitted, by default this is an empty string.

        :return: the society given ID
        """
        return self._society_agreement_id

    @property
    def start_date(self):
        """
        Agreement Start Date field. Date.

        The date on which the transfer of rights to the acquiring party becomes effective.

        :return: date on which the Agreement starts
        """
        return self._start_date

    @property
    def works_number(self):
        """
        Number of Works field. Numeric.

        Number of works registered subject to this agreement specific to this file.

        :return: number of works under this Agreement
        """
        return self._works_number


class AgreementTerritoryRecord(Record):
    """
    Represents a CWR Territory in Agreement (TER).

    This record specifies a territory either within the territorial scope of an agreement or excluded from it.

    For example, if  an agreement applied to all of Europe except Switzerland, you can provide a TER record to include
    Europe, and one to exclude Switzerland.

    This is to be used in an Agreement Transaction.
    """

    def __init__(self, prefix, tis_code, ie_indicator):
        """
        Constructs an AgreementTerritory.

        :param prefix: the record prefix
        :param tis_code: the TIS code
        :param ie_indicator: indicates if it is included or not
        """
        super(AgreementTerritoryRecord, self).__init__(prefix)
        self._tis_code = tis_code
        self._ie_indicator = ie_indicator

    @property
    def inclusion_exclusion_indicator(self):
        """
        Inclusion/Exclusion Indicator field. Table Lookup ('E'/'I').

        Indicates if the territory is included or excluded from the Agreement.

        The possible values are:
        - 'E' for excluded.
        - 'I' for included.

        :return: a code indicating if the territory is included or excluded
        """
        return self._ie_indicator

    @property
    def tis_code(self):
        """
        TIS Numeric Code field. Table Lookup (TIS Numeric Code).

        Numeric identifier of a territory according to the new CISAC Territory Standard.

        :return: the TIS code
        """
        return self._tis_code


class AgreementTransaction(object):
    """
    Represents a CWR Agreement Supporting Work Registration Transaction (AGR).

    These transactions document agreements between interested parties, not general agreements, where at least
    two IPAs (one assignor and one acquirer) form an Agreement for at least one Territory.

    The transaction contains only details of the Agreement itself, and the Territories-IPAs relationships, but
    not about the works covered by it, which are stored elsewhere in the same file, and connected to this Agreement
    based on the Submitter Agreement Number that is included in the header record.

    So an Agreement record is composed of three pieces:
    - The Agreement details (AGR)
    - The Territories covered (TER)
    - The IPAs of each territory (IPA)

    Or, in a more visual way an Agreement Transaction is: [AGR, [TER, IPA*]*].

    It must be noted that the total sum of all the shares of the Interested Parties should be 100% for each type of
    share.
    """

    def __init__(self, agreement, territories):
        """
        Constructs an AgreementTransaction.

        :param agreement: the Agreement record
        :param territories: the Territories and their IPAs
        """
        self._agreement = agreement
        self._territories = territories

    @property
    def agreement(self):
        """
        Agreement record field. This is an AgreementRecord.

        The details of the Agreement Transaction.

        :return: the agreement details
        """
        return self._agreement

    @property
    def territories(self):
        """
        The territories affected by this Agreement and their IPAs.

        This is a matrix of two columns, one containing a single Territory and another containing a collection
        with all the Interested Parties affecting this territory.

        Graphically this is: [territory_1, IPA*]*.

        These territories are instances of AgreementTerritory and the Interested Parties are instances of
        AgreementInterestedParty.

        :return: the territories affected by this Agreement and their IPAs as a dictionary
        """
        return self._territories
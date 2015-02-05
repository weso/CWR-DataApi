# -*- encoding: utf-8 -*-

"""
Agreement model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Agreement(object):
    """
    Represents a CWR Agreement entity.

    This is an agreement between two interested parties, affecting any number of works.

    The interested parties may be of any kind, so the agreement may be between a publisher and subpublisher, or between
    a writer and a publisher.

    It is identified by the submitter agreement number, and it is used to link the agreement to a work registration.
    """

    def __init__(self, submitter_agreement_number, society_agreement_number, agreement_type, start_date, end_date,
                 prior_royalty_status, post_term_collection_status, signature_date, works_number,
                 sales_manufacture_clause, international_standard_code=None, retention_end_date=None,
                 prior_royalty_status_date=None, post_term_collection_end_date=None, shares_change=False,
                 advance_given=False, interested_parties=None, territories=None):
        # Agreement identification data
        self._submitter_agreement_number = submitter_agreement_number
        self._society_agreement_number = society_agreement_number
        self._international_standard_code = international_standard_code
        self._agreement_type = agreement_type

        # Agreement dates
        self._start_date = start_date
        self._end_date = end_date

        # Royalty info
        self._prior_royalty_status = prior_royalty_status
        self._prior_royalty_status_date = prior_royalty_status_date

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

        if interested_parties is None:
            self._interested_parties = []
        else:
            self._interested_parties = interested_parties

        # The list of AgreementTerritory entities applied to the Agreement
        if territories is None:
            self._territories = []
        else:
            self._territories = territories

    def add_interested_party(self, ipa):
        self._interested_parties.append(ipa)

    def add_territory(self, territory):
        """
        Adds an AgreementTerritory which is to be applied to this Agreement.

        :param territory: the AgreementTerritory being applied
        """
        self._territories.append(territory)

    def remove_interested_party(self, ipa):
        self._interested_parties.remove(ipa)

    def remove_territory(self, territory):
        """
        Removes an AgreementTerritory which is being applied to this Agreement.

        :param territory: the AgreementTerritory being applied
        """
        self._interested_parties.remove(territory)

    @property
    def advance_given(self):
        """
        Advance Given field.

        Indicates if there is an advance paid for this agreement.

        If that is the case, this field should be True. Otherwise, the default value is False.

        :return: the Advance Given field
        """
        return self._advance_given

    @property
    def agreement_type(self):
        """
        Agreement Type field.

        Specifies the type of agreement.

        The Agreement Types specified by the CWR format are Original (songwriter to publisher) or Sub publisher
        (publisher to publisher), and Specific (defined list of songs) or General (entire catalogue).

        :return: the Agreement Type field
        """
        return self._agreement_type

    @property
    def end_date(self):
        """
        Agreement End Date field.

        This is the date when the transfer of rights to the acquiring party ends.

        There may be provisions within the contract (as described in other fields such as collection end date)
        which have impact on entitlements.

        :return: the Agreement End Date field
        """
        return self._end_date

    @property
    def interested_parties(self):
        return self._interested_parties

    @property
    def international_standard_code(self):
        """
        International Standard Agreement Code field.

        If an International Standard Agreement Code exists, it is indicated here.

        :return: the International Standard Agreement Code
        """
        return self._international_standard_code

    @property
    def post_term_collection_end_date(self):
        """
        Post-term Collection End Date field.

        Indicates up to which date the acquiring party has right to collect money after the Retention End Date, if it
        exists, or the Agreement End Date, if the first does not exist.

        For this date to be valid the the Post-Term Collection Status must then be set to "D" for date.

        :return: the Post-term Collection End Date field
        """
        return self._post_term_collection_end_date

    @property
    def post_term_collection_status(self):
        """
        Post-term Collection Status field.

        Indicates if the acquiring party has right to collect money after the Retention End Date, if it exists, or
        the Agreement End Date, if the first does not exist.

        If the acquiring party has no rights, this field should be "N"o. If the acquiring party can collect until
        further notification, this field should be "O" for open-ended. If they can collect until a specific date,
        this field should be "D" for date, and the date must be specified in Post-term Collection End Date.

        :return: the Post-term Collection Status field
        """
        return self._post_term_collection_status

    @property
    def prior_royalty_status(self):
        """
        Prior Royalty Status field.
        This field indicates whether or not the acquiring party is entitled to collect monies that were accrued before
        the start date of this agreement but not yet distributed by the societies.

        Possible values are: "N"one, or "A"ll , or "D"ate. If the acquiring party is entitled to collect monies as of a
        certain date (as indicated by "D"), then provide the relevant date in Prior Royalty Start Date.

        :return: the Prior Royalty Status field
        """
        return self._prior_royalty_status

    @property
    def prior_royalty_status_date(self):
        """
        Prior Royalty Start Date field.

        This date field indicates from what earning dates the acquiring party can begin collecting monies if the
        acquiring party can begin collecting before the agreement start date of this agreement.

        This date must be entered if and only if the Prior Royalty Status is 'D'ate.

        return the Prior Royalty Start Date field
        """
        return self._prior_royalty_status_date

    @property
    def retention_end_date(self):
        """
        Retention End Date field.

        If the agreement specifies that the collection rights for some or all of the works are retained beyond the end
        of the agreement, then the end date of this retention period is indicated here.

        :return: the Retention End Date field
        """
        return self._retention_end_date

    @property
    def sales_manufacture_clause(self):
        """
        Sales/ Manufacture Clause field.

        A marker which shows whether the acquiring party has acquired rights either for products manufactured or for
        products sold in the territories in agreement.

        Only two values are allowed according to BIEM/CISAC-rules:
        S = Sales Clause: A stipulation which lays down that the acquiring party has acquired rights for products sold
        in the territories in agreement irrespective of the country of manufacture.
        M = Manufacture Clause: A stipulation which lays down that the acquiring party has acquired rights for products
        manufactured in the territories in agreement irrespective of the country of sale.

        :return: the Sales/ Manufacture Clause field
        """
        return self._sales_manufacture_clause

    @property
    def shares_change(self):
        """
        Shares Change field.

        Indicates if the shares assigned to the writers can change when the work(s) covered under this agreement are
        sub published.

        If that is the case, this field should be True. Otherwise, the default value is False.

        :return: the Shares Change field
        """
        return self._shares_change

    @property
    def signature_date(self):
        """
        Date of Signature of Agreement field.

        The date when the written form of the agreement (the contract) was signed.

        :return the Date of Signature of Agreement field
        """
        return self._signature_date

    @property
    def society_agreement_number(self):
        """
        Society-assigned Agreement Number field.

        The agreement number assigned by the society of the subpublisher is generally not known when the agreement is
        submitted but can be supplied by the societies in the acknowledgment transaction.

        :return: the Society-assigned Agreement Number field
        """
        return self._society_agreement_number

    @property
    def start_date(self):
        """
        Agreement Start Date field.

        The transfer of rights to the acquiring party becomes effective on this date.

        :return: the Agreement Start Date field
        """
        return self._start_date

    @property
    def submitter_agreement_number(self):
        """
        Submitter Agreement Number field.

        This is the number that you use to uniquely identify this agreement.

        :return: the Submitter Agreement Number field
        """
        return self._submitter_agreement_number

    @property
    def territories(self):
        """
        Collection of AgreementTerritory entities being applied to this Agreement.

        :return: the AgreementTerritory entities being applied to this Agreement
        """
        return self._territories

    @property
    def works_number(self):
        """
        Number of Works field.

        The number of works for which work registrations are included in the agreement.

        :return: the Number of Works field
        """
        return self._works_number


class AgreementTerritory(object):
    """
    Represents a CWR Territory of Agreement entity.

    This indicates the relationship between an Agreement and a Territory. More specifically, it indicates if a territory
    is included or excluded from the Agreement.

    For example, if the Agreement covers all the world except for Europe, two AgreementTerritory entities would be used,
    one indicating that the world is included, and another indicating that Europe is excluded.

    It should be noted that a Territory can only be excluded if it is part of another Territory which is already
    included in the Agreement.

    Territories are identified by a four digit numeric codes. These can be found at http://www.cisac.org/.
    """

    def __init__(self, included, tis_numeric_code):
        self._included = included
        self._tis_numeric_code = tis_numeric_code

    @property
    def included(self):
        """
        Inclusion/ Exclusion Indicator field.

        A True value indicates this Territory is included. A False value indicates it is excluded.

        :return: True if the Territory is included, False if it is excluded
        """
        return self._included

    @property
    def tis_numeric_code(self):
        """
        TIS Numeric Code field.

        This is the ID for the Territory.

        :return: the Territory TIS code
        """
        return self._tis_numeric_code


class IPA(object):
    """
    Represents a CWR Interested Party for the Agreement (IPA).

    This indicates the relationship between an Interested Party and an Agreement.

    On an Agreement there it at least two Interested Parties: one assignor and one acquirer.
    """

    def __init__(self, agreement_id, interested_party_id, interested_party_name, agreement_role_code,
                 interested_party_writer_name=None, ipi=None,
                 pr_society=None, pr_share=0, mr_society=None, mr_share=0, sr_society=None, sr_share=0):
        # Agreement and Interested Party relationship
        self._agreement_id = agreement_id
        self._interested_party_id = interested_party_id
        self._agreement_role_code = agreement_role_code

        # Interested Party info
        self._ipi = ipi
        self._interested_party_name = interested_party_name
        self._interested_party_writer_name = interested_party_writer_name

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
    def agreement_id(self):
        """
        Agreement to which this Interested Party is related.

        :return: the Agreement ID
        """
        return self._agreement_id

    @property
    def agreement_role_code(self):
        """
        Agreement Role Code field.

        This code is used to indicate whether the interested party is assigning or acquiring the rights.

        :return: the role of the Interested Party on the Agreement
        """
        return self._agreement_role_code

    @property
    def interested_party_id(self):
        """
        Interested Party # field.

        This number is your unique identifier for this Interested Party. The same one which, for example, you would
        use to identify it on your database.

        :return: your Interested Party ID
        """
        return self._interested_party_id

    @property
    def interested_party_name(self):
        """
        Interested Party Name field.

        The last name of the writer, or the name of the publisher.

        Note that if the submitter does not have the ability to split first and last names of writers, the entire name
        should be entered in this field in the format “Last Name, First Name” including the comma after the last name.

        :return: the Interested Party Name
        """
        return self._interested_party_name

    @property
    def interested_party_ipi(self):
        """
        Interested Party Number (IPI) field.

        The unique identifier associated with this interested party. IPI numbering is a sub-system of the CISAC
        Common Information System.

        :return: the Interested Party IPI
        """
        return self._ipi

    @property
    def interested_party_writer_name(self):
        """
        Interested Party Writer First Name field.

        If the interested party is a writer, provide his/her first and middle names.

        :return: the Writer's first and middle names
        """
        return self._interested_party_writer_name

    @property
    def mr_share(self):
        """
        MR Share field.

        The percentage of the mechanical rights acquired or retained by this Interested Party under this Agreement.

        This value is a float which can range from 0 (0%) to 1 (100%).

        :return: the mechanical of the performing rights for the Interested Party
        """
        return self._mr_share

    @property
    def pr_share(self):
        """
        PR Share field.

        The percentage of the performing rights acquired or retained by this Interested Party under this Agreement.

        This value is a float which can range from 0 (0%) to 1 (100%).

        :return: the percentage of the performing rights for the Interested Party
        """
        return self._pr_share

    @property
    def sr_share(self):
        """
        PR Share field.

        The percentage of the synchronization rights acquired or retained by this Interested Party under this Agreement.

        This value is a float which can range from 0 (0%) to 1 (100%).

        :return: the percentage of the synchronization rights for the Interested Party
        """
        return self._sr_share

    @property
    def mr_society(self):
        """
        MR Affiliation Society field.

        The mechanical rights society to which this Interested Party belongs.

        :return: the Interested Party's mechanical rights society
        """
        return self._mr_society

    @property
    def pr_society(self):
        """
        PR Affiliation Society field.

        The performing rights society to which this Interested Party belongs.

        :return: the Interested Party's performing rights society
        """
        return self._pr_society

    @property
    def sr_society(self):
        """
        SR Affiliation Society field.

        The synchronization rights society to which this Interested Party belongs.

        :return: the Interested Party's synchronization rights society
        """
        return self._sr_society
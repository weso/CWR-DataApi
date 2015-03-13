# -*- coding: utf-8 -*-
from abc import ABCMeta
import datetime

from cwr.record import TransactionRecord


"""
Work entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class BaseWorkRecord(TransactionRecord):
    """
    Base class representing a Work's info.
    """
    __metaclass__ = ABCMeta

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, title, language_code=None, iswc=None):
        super(BaseWorkRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._title = title
        self._language_code = language_code
        self._iswc = iswc

    @property
    def iswc(self):
        """
        ISWC field.

        If the International Standard Work Code has been notified to you, you may include it in your registration
        or revision.

        This will return a ISWCCode instance or None.

        :return: the International Standard Work Code
        """
        return self._iswc

    @property
    def language_code(self):
        """
        Language Code field.

        Indicate the language of the Work title.

        If the title crosses languages (e.g., Maria), indicate the language of the lyrics.

        This information will assist societies in identifying the Work.

        :return: the language of the work title or lyrics
        """
        return self._language_code

    @property
    def title(self):
        """
        Work Title field.

        The title by which the work is best known.

        Do not store additional information in the title field e.g. “instrumental” or “background”.
        Such information should be stored in the designated field.

        :return: the title by which the work is best known
        """
        return self._title


class WorkRecord(BaseWorkRecord):
    """
    Represents a CWR Work Title and Core Information Record.

    This can be one of the following CWR v2.1 records:
    - Existing work which is in Conflict with a Work Registration (EXC)
    - New Work Registration (NWR)
    - Notification of ISWC assign to a work (ISW)
    - Revised Registration (REV)

    While the intentions of each type of record differ, these distinctions mean little to the class
    structure, because they are all meant to hold a Work's information for a Work Transaction.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, submitter_work_n, title, version_type,
                 musical_work_distribution_category,
                 date_publication_printed_edition=None, text_music_relationship=None, language_code=None,
                 copyright_number='', copyright_date=None, music_arrangement=None, lyric_adaptation=None,
                 excerpt_type=None, composite_type=None, composite_component_count=1, iswc=None, cwr_work_type=None,
                 duration=None, catalogue_number='', opus_number='', contact_id='', contact_name='',
                 recorded_indicator='U', priority_flag='U', exceptional_clause='U', grand_rights_indicator=False):
        super(WorkRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n, title, language_code,
                                         iswc)
        # Work identifying info
        self._submitter_work_n = submitter_work_n
        self._title = title
        self._date_publication_printed_edition = date_publication_printed_edition

        # Copyright
        self._copyright_date = copyright_date
        self._copyright_number = copyright_number

        # Musical info
        self._text_music_relationship = text_music_relationship
        self._music_arrangement = music_arrangement
        self._lyric_adaptation = lyric_adaptation
        self._composite_type = composite_type
        self._composite_component_count = composite_component_count
        self._duration = duration
        self._version_type = version_type
        self._excerpt_type = excerpt_type
        self._opus_number = opus_number

        # Distribution and publication info
        self._musical_work_distribution_category = musical_work_distribution_category
        self._grand_rights_indicator = grand_rights_indicator
        self._recorded_indicator = recorded_indicator
        self._exceptional_clause = exceptional_clause
        self._catalogue_number = catalogue_number

        # International info
        self._cwr_work_type = cwr_work_type

        # Contact info
        self._contact_id = contact_id
        self._contact_name = contact_name

        # Other info
        self._priority_flag = priority_flag

    @property
    def catalogue_number(self):
        """
        Catalogue Number for serious music field. Alphanumeric.

        The work catalogue number. The abbreviated name of the catalogue is to be added (like BWV, KV), without dots.
        Part numbers are to be added with a # e.g. KV 297#1 (meaning Köchel Verzeichnis Nr.297 part 1).

        :return: the catalogue number for serious music
        """
        return self._catalogue_number

    @property
    def composite_component_count(self):
        """
        Composite Component Count field. Numeric.

        If a type of composition has been indicated on the Work, this returns the number of components contained
        in the composite.

        By default this value is 1.

        :return: the composite count
        """
        return self._composite_component_count

    @property
    def composite_type(self):
        """
        Composite Type field. Table Lookup (Composite Type Table).

        If this is a composite work, this attribute will indicate the type of composite.

        :return: the Work composite type
        """
        return self._composite_type

    @property
    def contact_id(self):
        """
        Contact ID field. Alphanumeric.

        An identifier associated with the contact person at the organization that originated this transaction.

        :return: the ID of a contact persion in the transaction's originator
        """
        return self._contact_id

    @property
    def contact_name(self):
        """
        Contact Name field. Alphanumeric.

        The name of a business contact person at the organization that originated this transaction.

        In the event of the need for a follow-up communication with the submitter on the matter of this registration,
        it is useful to have the name of the person who originated the transaction.

        :return: the name of the transaction's originator
        """
        return self._contact_name

    @property
    def copyright_date(self):
        """
        Copyright Date field. Date.

        Original copyright date of the work.

        This is the date that your national copyright office has registered this Work.

        :return: the date in which the Work was registered
        """
        return self._copyright_date

    @property
    def copyright_number(self):
        """
        Copyright Number field. Alphanumeric.

        Original copyright number of the work.

        This is the number that your national copyright office has assigned to this Work upon registration.

        :return: the Work Copyright number
        """
        return self._copyright_number

    @property
    def cwr_work_type(self):
        """
        CWR Work Type field. Table Lookup (CWR Work Type).

        Indicates a genre found in the CWR Work Type table.

        :return: a CWR work type
        """
        return self._cwr_work_type

    @property
    def date_publication_printed_edition(self):
        """
        Date of Publication of Printed Edition field. Date.

        The date that the printed, new edition published by the submitting Publisher appeared.

        This is meant for registrations with GEMA, and is especially relevant for the notification of sub published
        works.

        :return: the date of the new edition
        """
        return self._date_publication_printed_edition

    @property
    def duration(self):
        """
        Duration field. Time (hours, minute, seconds).

        Duration of the work in hours, minutes, and seconds.

        Duration is required only in the following cases:
        - By all societies if the Musical Work Distribution Category is Serious (SER) (e.g., music intended for
        symphonic, recital and chamber settings)
        - By some societies, such as BMI, if the Musical Work Distribution Category is Jazz

        :return: duration of the work in hours, minutes and seconds
        """
        return self._duration

    @property
    def exceptional_clause(self):
        """
        Exceptional Clause field. Flag (Yes/No/Unknown).

        This is for registrations with GEMA.

        If it is True, the submitting GEMA-sub publisher has declared that the exceptional clause of the GEMA
        distribution rules with regard to printed editions applies (GEMA-Verteilungsplan A Anhang III).

        :return: 'Y' if the exceptional clause of the GEMA distribution rules applies, 'F' otherwise, 'U' if there is
        no information
        """
        return self._exceptional_clause

    @property
    def excerpt_type(self):
        """
        Excerpt Type field. Table Lookup (Excerpt Type Table).

        If this work is part of a larger work, indicates whether this is a movement or another, unspecified type of
        excerpt.

        :return: this Work's type of excerpt
        """
        return self._excerpt_type

    @property
    def grand_rights_indicator(self):
        """
        Grand Rights Indicator field. Boolean.

        Indicates whether this work is originally intended for performance on stage, such as a live theatrical
        performance.

        Note that this field is mandatory for registrations with the UK societies.

        :return: True if this work was originally intended for performance on stage, False otherwise
        """
        return self._grand_rights_indicator

    @property
    def lyric_adaptation(self):
        """
        Lyric Adaptation field. Table Lookup (Lyric Adaptation Table).

        If it is indicated that this is a modified version of another work (Version Type as 'MOD'), this field
        indicates what changes, if any, have occurred to the original lyric.

        :return: the changes to the original lyric
        """
        return self._lyric_adaptation

    @property
    def music_arrangement(self):
        """
        Music Arrangement field. Table Lookup (Music Arrangement Table).

        If it is indicated that this is a modified version of another work (Version Type as 'MOD'), this field
        indicates what changes, if any, have occurred to the original music.

        :return: the changes to the original music
        """
        return self._music_arrangement

    @property
    def musical_work_distribution_category(self):
        """
        Musical Work Distribution Category field. Table Lookup (Musical Work Distribution Category Table).

        Certain rights organizations have special distribution rules that apply to certain very specific genres of
        music. If this Work is in one of them, it should be indicated by this attribute.

        :return: the distribution category for this work
        """
        return self._musical_work_distribution_category

    @property
    def opus_number(self):
        """
        Opus Number for serious music field. Alphanumeric.

        The number assigned to this work, usually by the composer. Part numbers are to be added with a # e.g. 28#3
        (meaning Opus 28 part 3).

        :return: opus number for the work
        """
        return self._opus_number

    @property
    def priority_flag(self):
        """
        Priority Flag field. Flag (Yes/No/Unknown).

        This is meant to be used sparingly, just to speed up the registration of those works that are high on the charts
        or similar.

        :return: 'Y' if this work is prioritary, 'F' otherwise, 'U' if there is no information
        """
        return self._priority_flag

    @property
    def recorded_indicator(self):
        """
        Recorded Indicator field. Flag (Yes/No/Unknown).

        Indicates whether a recording of this work exists that has been made available to the public.

        :return: 'Y' if there is a public recording of this work, 'F' otherwise, 'U' if there is no information
        """
        return self._recorded_indicator

    @property
    def submitter_work_n(self):
        """
        Submitter Work Number field.

        This is the unique ID given by the submitter to the Work.

        :return: the submitter's ID for this Work
        """
        return self._submitter_work_n

    @property
    def text_music_relationship(self):
        """
        Text-Music Relationship field. Table Lookup (Text Music Relationship Table).

        Indicates whether this Work contains text only, music only, or a combination of both. (It is understood that a
        Work with lyrics may be performed instrumentally, and that a work with music may be performed spoken-only.)

        :return: the lyrical and musical composition of the Work
        """
        return self._text_music_relationship

    @property
    def version_type(self):
        """
        Version Type field. Table Lookup (Version Type Table).

        Indicates whether this work is entirely original, or based on another work.

        If the work is based on another work, values must be given for the Music Arrangement and Lyric Adaptation
        fields. If the work is a modified version of a copyrighted work, it is necessary for it to be authorized.

        :return: the Work's version type
        """
        return self._version_type


class WorkTransaction(TransactionRecord):
    """
    Represents a CWR Work Transaction.

    This can be one of the following CWR v2.1 transactions:
    - Existing work which is in Conflict with a Work Registration (EXC)
    - New Work Registration (NWR)
    - Notification of ISWC assign to a work (ISW)
    - Revised Registration (REV)

    While the actual use and intentions of each of these transactions differ, all of them indicate a relationship
    between a Work, Publishers and Writers. Along several details of the work.

    This is a very complex Transaction, composed by more than twenty types of records. Most of them are optional,
    making the possible number of variations huge.

    But all these records can be grouped into four types:
    - Work information record, which is only one, containing the most important information about the record
    - Publishers, divided between those controlled by the submitter and those out of his control
    - Writers, divided between those controlled by the submitter and those out of his control
    - Work details, containing such information as alternate titles or instrument composition

    All, except the first, can appear multiple times in different forms.

    Publishers controlled by the submitter appear along the territories they control, while those out of his
    control appear alone.

    So this section can be described as [[SPU, SPT*]*, OPU*].

    Writers controlled by the submitter appear along their territories and publishers, while those out of his
    control appear alone.

    This section can be described as [[SWR, SWT*, PWR*]*, OWR*].

    The work details are various kinds of data with little relation between them, some of which can appear multiple
    times.

    This section can be described as [ALT*, EWT, VER, PER*, REC, ORN*, INS*, IND*, COM*, ARI*]

    And so, in the end a Work Transaction can be seen as (missing the header record):
    [[SPU, SPT*]*, OPU*, [SWR, SWT*, PWR*]*, OWR*, ALT*, EWT, VER, PER*, REC, ORN*, INS*, IND*, COM*, ARI*]
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, entire_work_title=None,
                 original_work_title=None, recording=None, alternate_titles=None,
                 publishers_controlled=None, publishers_other=None, writers_controlled=None,
                 writers_other=None, performing_artists=None, work_origins=None, instrumentation_summaries=None,
                 instrumentation_details=None, components=None, additional_info=None):
        super(WorkTransaction, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._entire_work_title = entire_work_title
        self._original_work_title = original_work_title
        self._recording = recording
        self._additional_info = additional_info

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

        if performing_artists is None:
            self._performing_artists = []
        else:
            self._performing_artists = performing_artists

        if work_origins is None:
            self._work_origins = []
        else:
            self._work_origins = work_origins

        if instrumentation_summaries is None:
            self._instrumentation_summaries = []
        else:
            self._instrumentation_summaries = instrumentation_summaries

        if instrumentation_details is None:
            self._instrumentation_details = []
        else:
            self._instrumentation_details = instrumentation_details

        if components is None:
            self._components = []
        else:
            self._components = components

    @property
    def additional_info(self):
        """
        Additional Info field.

        Contains information such as comments or the Society number.

        This is a collection of strings.

        :return: additional info for the work
        """
        return self._additional_info

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
    def instrumentation_details(self):
        """
        Instrumentation Details field.

        Returns the Work Instrumentation Details.

        :return: the Work Instrumentation Details
        """
        return self._instrumentation_details

    @property
    def instrumentation_summaries(self):
        """
        Instrumentation Summaries field.

        Returns the Work Instrumentation Summaries.

        :return: the Work Instrumentation Summaries
        """
        return self._instrumentation_summaries

    @property
    def original_work_title(self):
        """
        Original Work Title field.

        Returns an Original Work Title for the Work.

        :return: an Original Work Title for the Work
        """
        return self._original_work_title

    @property
    def performing_artists(self):
        """
        Performing Artists field.

        The Performing Artists.

        :return: the Performing Artists
        """
        return self._performing_artists

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
    def work_origins(self):
        """
        Work Origins field.

        Returns the Work Origins.

        :return: the Work Origins
        """
        return self._work_origins

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


class ComponentRecord(TransactionRecord):
    """
    Represents a CWR Component (COM).

    If the work being registered is a composite work, the COM record will identify an individual component of the
    composite.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, title, writer_1_last_name,
                 submitter_work_n='',
                 writer_1_first_name='', writer_2_first_name='', writer_2_last_name='',
                 writer_1_ipi_base=None, writer_1_ipi_name=None, writer_2_ipi_base=None, writer_2_ipi_name=None,
                 iswc='', duration=None):
        super(ComponentRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        # Work's info
        self._submitter_work_n = submitter_work_n
        self._title = title
        self._iswc = iswc
        self._duration = duration

        # First writer's info
        self._writer_1_first_name = writer_1_first_name
        self._writer_1_last_name = writer_1_last_name
        self._writer_1_ipi_base = writer_1_ipi_base
        self._writer_1_ipi_name = writer_1_ipi_name

        # Second writer's info
        self._writer_2_first_name = writer_2_first_name
        self._writer_2_last_name = writer_2_last_name
        self._writer_2_ipi_base = writer_2_ipi_base
        self._writer_2_ipi_name = writer_2_ipi_name

    @property
    def duration(self):
        """
        Duration Field. Time.

        The duration of this composite component.

        :return: the component's duration
        """
        return self._duration

    @property
    def iswc(self):
        """
        ISWC of Component field. Alphanumeric.

        The International Standard Work Code assigned to the original work from which a portion was taken and included
        in this composite work.

        :return: the International Standard Work Code
        """
        return self._iswc

    @property
    def submitter_work_n(self):
        """
        Submitter Work Number field. Alphanumeric.

        The unique number that you have assigned to the entire work.

        :return: the Work's ID
        """
        return self._submitter_work_n

    @property
    def title(self):
        """
        Title field. Alphanumeric.

        The title of the original work from which a portion was taken and included in the composite work.

        :return: the title of the original work
        """
        return self._title

    @property
    def writer_1_first_name(self):
        """
        Writer 1 First Name field. Alphanumeric.

        The first name of the first writer.

        :return: the first name of the first Writer
        """
        return self._writer_1_first_name

    @property
    def writer_1_ipi_base(self):
        """
        Writer 1 IPI Base Number field. Table Lookup (IPI DB).

        The IP Base Number is a unique identifier allocated automatically by the IPI System to each interested party
        (IP), being either a natural person or legal entity. The number consists of 13 characters: letter i (I),
        hyphen (-), nine digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus 10, I weight = 2,
        adapted from ISO 7064). You can find more information on the CISAC web site.

        :return: the first Writer's IP base number
        """
        return self._writer_1_ipi_base

    @property
    def writer_1_ipi_name(self):
        """
        Writer 1 IPI Name # field.

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the IPI number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the first Writer's IP name field
        """
        return self._writer_1_ipi_name

    @property
    def writer_1_last_name(self):
        """
        Writer 1 Last Name field. Alphanumeric.

        If the ISWC is not known, then the last name of a writer is helpful to identify the work.

        :return: the first Writer's last name
        """
        return self._writer_1_last_name

    @property
    def writer_2_first_name(self):
        """
        Writer 2 First Name field. Alphanumeric.

        The first name of the second writer.

        :return: the first name of the second Writer
        """
        return self._writer_2_first_name

    @property
    def writer_2_ipi_base(self):
        """
        Writer 2 IP Base Number field. Table Lookup (IPI DB).

        The IP Base Number is a unique identifier allocated automatically by the IPI System to each interested party
        (IP), being either a natural person or legal entity. The number consists of 13 characters: letter i (I),
        hyphen (-), nine digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus 10, I weight = 2,
        adapted from ISO 7064). You can find more information on the CISAC web site.

        :return: the second Writer's IP base number
        """
        return self._writer_2_ipi_base

    @property
    def writer_2_ipi_name(self):
        """
        Writer 2 IPI Name # field.

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the IPI number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the second Writer's IP name field
        """
        return self._writer_2_ipi_name

    @property
    def writer_2_last_name(self):
        """
        Writer 2 Last Name field. Alphanumeric.

        If the ISWC is not known, then the last name of a writer is helpful to identify the work.

        :return: the second Writer's last name
        """
        return self._writer_2_last_name


class AuthoredWorkRecord(BaseWorkRecord):
    """
    Represents a Work with authors. This is for the Entire Work (EWT) and Original Work for Versions (VER) entities.

    It also indicates the original source of the work.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, title, submitter_work_n='',
                 writer_1_first_name='', writer_1_last_name='', writer_2_first_name='', writer_2_last_name='',
                 writer_1_ipi_base=None, writer_1_ipi_name=None, writer_2_ipi_base=None, writer_2_ipi_name=None,
                 source=None, language_code=None, iswc=None):
        super(AuthoredWorkRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n, title,
                                                 language_code, iswc)

        # Work's info
        self._submitter_work_n = submitter_work_n
        self._source = source

        # First writer's info
        self._writer_1_first_name = writer_1_first_name
        self._writer_1_last_name = writer_1_last_name
        self._writer_1_ipi_base = writer_1_ipi_base
        self._writer_1_ipi_name = writer_1_ipi_name

        # Second writer's info
        self._writer_2_first_name = writer_2_first_name
        self._writer_2_last_name = writer_2_last_name
        self._writer_2_ipi_base = writer_2_ipi_base
        self._writer_2_ipi_name = writer_2_ipi_name

    @property
    def source(self):
        """
        Source field. Alphanumeric.

        This field contains a free form description of the source of the entire work e.g. symphony.

        :return: the work source
        """
        return self._source

    @property
    def submitter_work_n(self):
        """
        Submitter Work Number field. Alphanumeric.

        The unique number that you have assigned to the entire work.

        :return: the Work ID
        """
        return self._submitter_work_n

    @property
    def writer_1_first_name(self):
        """
        Writer 1 First Name field. Alphanumeric.

        The first name of the first writer.

        :return: the first name of the first Writer
        """
        return self._writer_1_first_name

    @property
    def writer_1_ipi_base(self):
        """
        Writer 1 IPI Base Number field. Table Lookup (CISAC)

        The IP Base Number is a unique identifier allocated automatically by the IPI System to each interested party
        (IP), being either a natural person or legal entity. The number consists of 13 characters: letter i (I),
        hyphen (-), nine digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus 10, I weight = 2,
        adapted from ISO 7064). You can find more information on the CISAC web site.

        :return: the first Writer's IPI base number
        """
        return self._writer_1_ipi_base

    @property
    def writer_1_ipi_name(self):
        """
        Writer 1 IP Name # field. Table Lookup (CISAC)

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the IPI number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the first Writer's IP name field
        """
        return self._writer_1_ipi_name

    @property
    def writer_1_last_name(self):
        """
        Writer 1 Last Name field. Alphanumeric.

        If the ISWC is not known, then the last name of a writer is helpful to identify the work.

        :return: the first Writer's last name
        """
        return self._writer_1_last_name

    @property
    def writer_2_first_name(self):
        """
        Writer 2 First Name field. Alphanumeric.

        The first name of the second writer.

        :return: the first name of the second Writer
        """
        return self._writer_2_first_name

    @property
    def writer_2_ipi_base(self):
        """
        Writer 2 IPI Base Number field. Table Lookup (CISAC)

        The IP Base Number is a unique identifier allocated automatically by the IPI System to each interested party
        (IP), being either a natural person or legal entity. The number consists of 13 characters: letter i (I),
        hyphen (-), nine digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus 10, I weight = 2,
        adapted from ISO 7064). You can find more information on the CISAC web site.

        :return: the second Writer's IPI base number
        """
        return self._writer_2_ipi_base

    @property
    def writer_2_ipi_name(self):
        """
        Writer 2 IP Name # field. Table Lookup (CISAC)

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the IPI number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the second Writer's IP name field
        """
        return self._writer_2_ipi_name

    @property
    def writer_2_last_name(self):
        """
        Writer 2 Last Name field. Alphanumeric.

        If the ISWC is not known, then the last name of a writer is helpful to identify the work.

        :return: the second Writer's last name
        """
        return self._writer_2_last_name


class AlternateTitleRecord(TransactionRecord):
    """
    Represents a CWR Alternate Title (ALT) record.

    This identifies alternate titles for this work.

    The language code is used to identify titles that have been translated into a language other than the original.

    Note that this applies to translation of the title only - not a  translation of the work. Including record type VER
    would indicate a work translation.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, alternate_title, title_type,
                 language_code=None):
        super(AlternateTitleRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._alternate_title = alternate_title
        self._title_type = title_type
        self._language_code = language_code

    @property
    def alternate_title(self):
        """
        Alternate Title field. Alphanumeric.

        AKA or pseudonym of the work title.

        :return: the alternate title
        """
        return self._alternate_title

    @property
    def language_code(self):
        """
        Language Code field. Table Lookup (Language Code Table).

        This field contains the code used to describe the language of the Alternate Title, if it is known.

        :return: the Alternate Title language
        """
        return self._language_code

    @property
    def title_type(self):
        """
        Title Type field. Table Lookup (Title Type Table).

        Indicates the type of alternate title presented on this record.

        :return: the type of alternate title
        """
        return self._title_type


class RecordingDetailRecord(TransactionRecord):
    """
    Represents a CWR Recording Detail (REC).

    This record contains information on the first commercial release of the work.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, first_release_date=None,
                 first_release_duration=None, first_album_title='',
                 first_album_label='', first_release_catalog_n='', ean=None,
                 isrc=None, recording_format=None, recording_technique=None, media_type=None):
        super(RecordingDetailRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._first_release_date = first_release_date

        if first_release_duration is None:
            self._first_release_duration = datetime.timedelta(seconds=0)
        else:
            self._first_release_duration = first_release_duration

        self._first_album_title = first_album_title
        self._first_album_label = first_album_label
        self._first_release_catalog_n = first_release_catalog_n
        self._ean = ean
        self._isrc = isrc
        self._recording_format = recording_format
        self._recording_technique = recording_technique
        self._media_type = media_type

    @property
    def ean(self):
        """
        EAN field. Table Lookup (EAN).

        European Article Number of release (EAN-13).

        :return: the EAN
        """
        return self._ean

    @property
    def first_album_label(self):
        """
        First Album Label field. Alphanumeric.

        Name of the organization that produced and released the album in which the first release of the work was
        included.

        :return: the label of the first album
        """
        return self._first_album_label

    @property
    def first_album_title(self):
        """
        First Album Title field. Alphanumeric.

        The name of the album in which the work was included if the work was first released as part of an album.

        :return: the title of the first album
        """
        return self._first_album_title

    @property
    def first_release_catalog_n(self):
        """
        First Release Catalog Number field. Alphanumeric.

        Number assigned by the organization releasing the album for internal purposes such as sales and distribution
        tracking.

        :return: the first release catalog id
        """
        return self._first_release_catalog_n

    @property
    def first_release_date(self):
        """
        First Release Date field. Date.

        Date the work was or will be first released for public consumption.

        This date can be a past, present, or future date.

        :return: the date of the first release
        """
        return self._first_release_date

    @property
    def first_release_duration(self):
        """
        First Release Duration field. Time (Hours, minutes, seconds).

        Duration of the first release of the work.

        :return: the duration of the first release of the work
        """
        return self._first_release_duration

    @property
    def isrc(self):
        """
        ISRC field. Table Lookup (ISRC).

        International Standard Recording Code of the recording of the work on the release (according to ISO 3901).

        :return: the ISRC
        """
        return self._isrc

    @property
    def media_type(self):
        """
        Media Type field. Table Lookup (BIEM/CISAC Media Type table).

        BIEM/CISAC code for media type.

        :return: the media type
        """
        return self._media_type

    @property
    def recording_format(self):
        """
        Recording Format field. Table Lookup (?).

        Code that identifies the content of the recording: “A” (audio), “V” (video)..

        :return: the recording format
        """
        return self._recording_format

    @property
    def recording_technique(self):
        """
        Recording Technique field. Table Lookup (Recording Technique table).

        Identifies the recording procedure: “A” (Analogue), “D” (Digital), “U” (Unknown).

        :return: the recording technique
        """
        return self._recording_technique


class InstrumentationDetailRecord(TransactionRecord):
    """
    Represents a CWR Instrumentation Detail (IND) record.

    The IND record provides information on standard instruments or voices for serious works.

    If the Musical Work  Distribution Category is SER then instrumentation detail is required using one or more INS
    records as well as IND records to describe the individual instruments (if any).
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, instrument_code, number_players=0):
        super(InstrumentationDetailRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._instrument_code = instrument_code
        self._number_players = number_players

    @property
    def instrument_code(self):
        """
        Instrument Code field. Table Lookup (Instrument table).

        Indicates the use of a specific instrument in this version of instrumentation.

        :return: the instrument code
        """
        return self._instrument_code

    @property
    def number_players(self):
        """
        Number of Players field. Numeric.

        Indicates the number of players for the above instrument.

        :return: the number of players
        """
        return self._number_players


class WorkOriginRecord(TransactionRecord):
    """
    Represents a CWR Work Origin (ORN) record.

    This record serves to describe the origin of the work.

    The origin may be a library, or an audio-visual production or both. If the work originated in an AV production,
    additional information regarding the usage of the work within the production can be helpful.

    Note that the cue sheet is always the final authority for usage data.

    Many identifiers for the audio-visual production have been added with version 2.1 including the reference as used in
    the CIS tool, AV Index.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, intended_purpose, production_title='',
                 cd_identifier='', cut_number=0, library='', bltvr='', visan=None, production_n='', episode_title='',
                 episode_n='', year_production=0, audio_visual_key=None):
        super(WorkOriginRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._intended_purpose = intended_purpose
        self._production_title = production_title
        self._cd_identifier = cd_identifier
        self._cut_number = cut_number
        self._library = library
        self._bltvr = bltvr
        self._visan = visan
        self._production_n = production_n
        self._episode_title = episode_title
        self._episode_n = episode_n
        self._year_production = year_production
        self._audio_visual_key = audio_visual_key

    @property
    def audio_visual_key(self):
        """
        Audio-Visual Key.

        :return: the audio-visual key
        """
        return self._audio_visual_key

    @property
    def bltvr(self):
        """
        BLTVR field. Alphanumeric.

        An indication of the primary use of the work within the AV production.

        The definitive source for cue usage is the cue sheet.

        :return: the BLTVR
        """
        return self._bltvr

    @property
    def cd_identifier(self):
        """
        CD Identifier field. Alphanumeric.

        If Intended Purpose is equal to LIB (Library Work), enter the identifier associated with the CD upon which
        the work appears.

        :return: CD identifier
        """
        return self._cd_identifier

    @property
    def cut_number(self):
        """
        Cut Number field. Numeric.

        If Intended Purpose is equal to LIB (Library Work), enter the track number on the CD Identifier where the work
        appears.  This field is required when CD Identifier is entered.

        :return: the cut number
        """
        return self._cut_number

    @property
    def episode_n(self):
        """
        Episode Number field. Alphanumeric.

        Number assigned to the episode by the producer.

        :return: the episode number
        """
        return self._episode_n

    @property
    def episode_title(self):
        """
        Episode Title field. Alphanumeric.

        Title of the episode from which this work originated.

        :return: the episode title
        """
        return self._episode_title

    @property
    def intended_purpose(self):
        """
        Intended Purpose field. Table Lookup (Intended Purpose Table).

        Indicates the type of production from which this work originated.

        :return: the inteded purpose
        """
        return self._intended_purpose

    @property
    def library(self):
        """
        Library field. Alphanumeric.

        The library from which this work originated.

        :return: the library
        """
        return self._library

    @property
    def production_n(self):
        """
        Production Number field. Alphanumeric.

        The number generated by the production company to identify the work.

        :return: the production number field
        """
        return self._production_n

    @property
    def production_title(self):
        """
        Production Title field. Alphanumeric.

        Name of the production from which this work originated.

        :return: the production title
        """
        return self._production_title

    @property
    def visan(self):
        """
        V-ISAN.

        This is expected to be a VISAN object instance.

        :return: the V-ISAN
        """
        return self._visan

    @property
    def year_production(self):
        """
        Year of Production field. Numeric.

        The year in which the production of the film or episode was completed.

        :return: the year of production
        """
        return self._year_production


class InstrumentationSummaryRecord(TransactionRecord):
    """
    Represents a CWR Instrumentation Summary (INS) record.

    This record provides information on standard and non-standard instrumentation for serious works. If the Musical Work
    Distribution Category is SER then instrumentation detail is required using one or more Standard Instrumentation
    Type, one or more IND records, or one Instrumentation Description.

    The Instrumentation Description is the least desirable, and should be used only if the other fields are not
    available.

    It is possible to use both a Standard Instrumentation Type and one or more IND records to describe, for example, a
    wind quintet and a piano.

    It is also possible to use both one or more Standard Instrumentation Type and one or more IND records to describe,
    for example, a work written for two wind quintets and two pianos.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, number_voices=0,
                 standard_instrumentation_type=None,
                 description=''):
        super(InstrumentationSummaryRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._number_voices = number_voices
        self._standard_instrumentation_type = standard_instrumentation_type
        self._instrumentation_description = description

    @property
    def instrumentation_description(self):
        """
        Instrumentation Description field. Alphanumeric.

        Describes instrumentation if non-standard instrumentation is used on this work. Note that this field is required
         if IND records are not entered and if Standard Instrumentation Type is blank.

        :return: the instrumentation description
        """
        return self._instrumentation_description

    @property
    def number_voices(self):
        """
        Number of Voices field. Numeric.

        Indicates the number of independent parts included in this work.

        :return: the number of voices
        """
        return self._number_voices

    @property
    def standard_instrumentation_type(self):
        """
        Standard Instrumentation Type field. Table Lookup (Standard Instrumentation table).

        Describes instrumentation if standard instrumentation is used on this work. Note that this field is required if
        IND records are not entered and if Instrumentation Description is blank.

        :return: the Standard Instrumentation Type
        """
        return self._standard_instrumentation_type


class PerformingArtistRecord(TransactionRecord):
    """
    Represents a CWR Performing Artist (PER).

    Contains the info of a person or group performing this work either in public or on a recording.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n, performing_artist_last_name,
                 performing_artist_first_name='', performing_artist_ipi_name=None,
                 performing_artist_ipi_base_number=None):
        super(PerformingArtistRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
        self._performing_artist_first_name = performing_artist_first_name
        self._performing_artist_last_name = performing_artist_last_name
        self._performing_artist_ipi_name = performing_artist_ipi_name
        self._performing_artist_ipi_base_number = performing_artist_ipi_base_number

    @property
    def performing_artist_first_name(self):
        """
        Performing Artist First Name field. Alphanumeric.

        First name associated with the performing artist identified in the previous field.

        :return: the Performing Artist first name
        """
        return self._performing_artist_first_name

    @property
    def performing_artist_ipi_base_n(self):
        """
        Performing Artist IPI Base Number field. Table Lookup (IPI DB).

        The IPI base number assigned to this performing artist.

        :return: the IPI base number
        """
        return self._performing_artist_ipi_base_number

    @property
    def performing_artist_ipi_name_n(self):
        """
        Performing Artist IPI Name Number field. Table Lookup (IPI).

        The IPI # corresponding to this performing artist with 2 leading zero’s or the IPI Name #.

        Values reside in the IPI database.

        :return: the Performing Artist IPI name number
        """
        return self._performing_artist_ipi_name

    @property
    def performing_artist_last_name(self):
        """
        Performing Artist Last Name field. Alphanumeric.

        Last name of a person or full name of a group that has performed the work on a recording or in public.

        Note that if the performer is known by a single name, it should be entered in this field.

        :return: the Performing Artist last name
        """
        return self._performing_artist_last_name



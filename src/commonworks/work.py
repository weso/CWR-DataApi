# -*- encoding: utf-8 -*-
from abc import ABCMeta

from commonworks.file import Record


"""
Work entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class BaseWork(Record):
    """
    Base class representing a Work's info.
    """
    __metaclass__ = ABCMeta

    def __init__(self, prefix, title, language_code=None, iswc=None):
        super(BaseWork, self).__init__(prefix)
        self._title = title
        self._language_code = language_code
        self._iswc = iswc

    @property
    def iswc(self):
        """
        ISWC field.

        If the International Standard Work Code has been notified to you, you may include it in your registration
        or revision.

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


class WorkRecord(BaseWork):
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

    def __init__(self, prefix, work_id, title, version_type, musical_distribution_category,
                 printed_edition_publication_date=None, text_music_relationship=None, language_code=None,
                 copyright_number='', copyright_date=None, music_arrangement=None, lyric_adaptation=None,
                 excerpt_type=None, composite_type=None, composite_component_count=1, iswc='', cwr_work_type=None,
                 duration=None, catalogue_number='', opus_number='', contact_id='', contact_name='',
                 recorded_indicator=False, priority_flag=False, exceptional_clause=False, grand_rights_indicator=False):
        super(WorkRecord, self).__init__(prefix, title, language_code, iswc)
        # Work identifying info
        self._work_id = work_id
        self._title = title
        self._printed_edition_publication_date = printed_edition_publication_date

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
        self._musical_distribution_category = musical_distribution_category
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
    def musical_distribution_category(self):
        """
        Musical Work Distribution Category field. Table Lookup (Musical Work Distribution Category Table).

        Certain rights organizations have special distribution rules that apply to certain very specific genres of
        music. If this Work is in one of them, it should be indicated by this attribute.

        :return: the distribution category for this work
        """
        return self._musical_distribution_category

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
    def printed_edition_publication_date(self):
        """
        Date of Publication of Printed Edition field. Date.

        The date that the printed, new edition published by the submitting Publisher appeared.

        This is meant for registrations with GEMA, and is especially relevant for the notification of sub published
        works.

        :return: the date of the new edition
        """
        return self._printed_edition_publication_date

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

    @property
    def work_id(self):
        """
        Submitter Work Number field.

        This is the unique ID given by the submitter to the Work.

        :return: the submitter's ID for this Work
        """
        return self._work_id


class WorkTransaction(object):
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


class Component(object):
    """
    Represents a CWR Component (COM).
    """

    def __init__(self, title, first_name_1, submitter_id=None,
                 last_name_1=None, first_name_2=None, last_name_2=None,
                 ip_base_1=None, ip_name_1=None, ip_base_2=None, ip_name_2=None,
                 iswc=None):
        # Work's info
        self._submitter_id = submitter_id
        self._title = title
        self._iswc = iswc

        # First writer's info
        self._first_name_1 = first_name_1
        self._last_name_1 = last_name_1
        self._ip_base_1 = ip_base_1
        self._ip_name_1 = ip_name_1

        # Second writer's info
        self._first_name_2 = first_name_2
        self._last_name_2 = last_name_2
        self._ip_base_2 = ip_base_2
        self._ip_name_2 = ip_name_2

    @property
    def first_name_1(self):
        """
        Writer 1 First Name field.

        The first name of the first writer.

        :return: the first name of the first Writer
        """
        return self._first_name_1

    @property
    def first_name_2(self):
        """
        Writer 2 First Name field.

        The first name of the second writer.

        :return: the first name of the second Writer
        """
        return self._first_name_2

    @property
    def ip_base_1(self):
        """
        Writer 1 IP Base Number field.

        The IP Base Number is a unique identifier allocated automatically by the IPI System to each interested party
        (IP), being either a natural person or legal entity. The number consists of 13 characters: letter i (I),
        hyphen (-), nine digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus 10, I weight = 2,
        adapted from ISO 7064). You can find more information on the CISAC web site.

        :return: the first Writer's IP base number
        """
        return self._ip_base_1

    @property
    def ip_base_2(self):
        """
        Writer 2 IP Base Number field.

        The IP Base Number is a unique identifier allocated automatically by the IPI System to each interested party
        (IP), being either a natural person or legal entity. The number consists of 13 characters: letter i (I),
        hyphen (-), nine digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus 10, I weight = 2,
        adapted from ISO 7064). You can find more information on the CISAC web site.

        :return: the second Writer's IP base number
        """
        return self._ip_base_2

    @property
    def ip_name_1(self):
        """
        Writer 1 IP Name # field.

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the CAE number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the first Writer's IP name field
        """
        return self._ip_name_1

    @property
    def ip_name_2(self):
        """
        Writer 2 IP Name # field.

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the CAE number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the second Writer's IP name field
        """
        return self._ip_name_2

    @property
    def iswc(self):
        """
        ISWC field.

        If the International Standard Work Code has been notified to you, you may include it in your registration
        or revision.

        :return: the International Standard Work Code
        """
        return self._iswc

    @property
    def last_name_1(self):
        """
        Writer 1 Last Name field.

        If the ISWC is not known, then the last name of a writer is helpful to identify the work.

        :return: the first Writer's last name
        """
        return self._last_name_1

    @property
    def last_name_2(self):
        """
        Writer 2 Last Name field.

        If the ISWC is not known, then the last name of a writer is helpful to identify the work.

        :return: the second Writer's last name
        """
        return self._last_name_2

    @property
    def submitter_id(self):
        """
        Submitter entity # field.

        The unique number that you have assigned to the entire work.

        :return: the entity's ID
        """
        return self._submitter_id

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


class AuthoredWork(BaseWork):
    """
    Represents a Work with authors. This is for the Entire Work and Original Work entities.
    """

    def __init__(self, prefix, title, work_id=None,
                 first_name_1=None, last_name_1=None, first_name_2=None, last_name_2=None,
                 ip_base_1=None, ip_name_1=None, ip_base_2=None, ip_name_2=None,
                 source=None, language_code=None, iswc=None):
        super(AuthoredWork, self).__init__(prefix, title, language_code, iswc)

        # Work's info
        self._work_id = work_id
        self._source = source

        # First writer's info
        self._first_name_1 = first_name_1
        self._last_name_1 = last_name_1
        self._ip_base_1 = ip_base_1
        self._ip_name_1 = ip_name_1

        # Second writer's info
        self._first_name_2 = first_name_2
        self._last_name_2 = last_name_2
        self._ip_base_2 = ip_base_2
        self._ip_name_2 = ip_name_2

    @property
    def first_name_1(self):
        """
        Writer 1 First Name field.

        The first name of the first writer.

        :return: the first name of the first Writer
        """
        return self._first_name_1

    @property
    def first_name_2(self):
        """
        Writer 2 First Name field.

        The first name of the second writer.

        :return: the first name of the second Writer
        """
        return self._first_name_2

    @property
    def ip_base_1(self):
        """
        Writer 1 IP Base Number field.

        The IP Base Number is a unique identifier allocated automatically by the IPI System to each interested party
        (IP), being either a natural person or legal entity. The number consists of 13 characters: letter i (I),
        hyphen (-), nine digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus 10, I weight = 2,
        adapted from ISO 7064). You can find more information on the CISAC web site.

        :return: the first Writer's IP base number
        """
        return self._ip_base_1

    @property
    def ip_base_2(self):
        """
        Writer 2 IP Base Number field.

        The IP Base Number is a unique identifier allocated automatically by the IPI System to each interested party
        (IP), being either a natural person or legal entity. The number consists of 13 characters: letter i (I),
        hyphen (-), nine digits, hyphen (-), one check-digit. I-999999999-9. (weighted modulus 10, I weight = 2,
        adapted from ISO 7064). You can find more information on the CISAC web site.

        :return: the second Writer's IP base number
        """
        return self._ip_base_2

    @property
    def ip_name_1(self):
        """
        Writer 1 IP Name # field.

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the CAE number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the first Writer's IP name field
        """
        return self._ip_name_1

    @property
    def ip_name_2(self):
        """
        Writer 2 IP Name # field.

        The IP Name Number is a unique identifier allocated automatically by the IPI System to each name. It is based on
        the CAE number and consists of 11 digits 99999999999 (modulus 101). The last two digits are check-digits. An IP
        may have more than one IP name. New IP names will get new IP Name Numbers. A name of an IP name number may only
        be changed in case of spelling corrections.

        :return: the second Writer's IP name field
        """
        return self._ip_name_2

    @property
    def last_name_1(self):
        """
        Writer 1 Last Name field.

        If the ISWC is not known, then the last name of a writer is helpful to identify the work.

        :return: the first Writer's last name
        """
        return self._last_name_1

    @property
    def last_name_2(self):
        """
        Writer 2 Last Name field.

        If the ISWC is not known, then the last name of a writer is helpful to identify the work.

        :return: the second Writer's last name
        """
        return self._last_name_2

    @property
    def source(self):
        """
        Source field.

        This field contains a free form description of the source of the entire work e.g. symphony.

        :return: the source
        """
        return self._source

    @property
    def work_id(self):
        """
        Submitter Work # field.

        The unique number that you have assigned to the entire work.

        :return: the Work's ID
        """
        return self._work_id


class AlternateTitle(object):
    """
    Represents a CWR Alternate Title.
    """

    def __init__(self, alternate_title, title_type, language=None):
        self._alternate_title = alternate_title
        self._title_type = title_type
        self._language = language

    @property
    def alternate_title(self):
        """
        Alternate Title field.

        :return: the alternate title
        """
        return self._alternate_title

    @property
    def language(self):
        """
        Language Code field.

        This field contains the code used to describe the language of the Alternate Title, if it is known.

        :return: the Alternate Title language
        """
        return self._language

    @property
    def title_type(self):
        """
        Title Type field.

        This field describes the type of title.

        :return:
        """
        return self._title_type


class RecordingDetail(object):
    """
    Represents a CWR recording details.
    """

    def __init__(self, first_release_date=None, first_release_duration=None, first_album_title=None,
                 first_album_label=None, first_release_catalog_id=None, ean=None,
                 isrc=None, recording_format=None, recording_technique=None, media_type=None):
        self._first_release_date = first_release_date
        self._first_release_duration = first_release_duration
        self._first_album_title = first_album_title
        self._first_album_label = first_album_label
        self._first_release_catalog_id = first_release_catalog_id
        self._ean = ean
        self._isrc = isrc
        self._recording_format = recording_format
        self._recording_technique = recording_technique
        self._media_type = media_type

    @property
    def ean(self):
        """
        EAN field.

        European Article Number of release (EAN-13).

        :return: the EAN
        """
        return self._ean

    @property
    def first_album_label(self):
        """
        First Album Label field.

        Name of the organization that produced and released the album in which the first release of the work was
        included.

        :return: the label of the first album
        """
        return self._first_album_label

    @property
    def first_album_title(self):
        """
        First Album Title field.

        The name of the album in which the work was included if the work was first released as part of an album.

        :return: the title of the first album
        """
        return self._first_album_title

    @property
    def first_release_catalog_id(self):
        """
        First Release Catalog # field.

        Number assigned by the organization releasing the album for internal purposes such as sales and distribution
        tracking.

        :return: the first release catalog id
        """
        return self._first_release_catalog_id

    @property
    def first_release_date(self):
        """
        First Release Date field.

        Date the work was or will be first released for public consumption.

        This date can be a past, present, or future date.

        :return: the date of the first release
        """
        return self._first_release_date

    @property
    def first_release_duration(self):
        """
        First Release Duration field.

        Duration of the first release of the work.

        :return: the duration of the first release of the work
        """
        return self._first_release_duration

    @property
    def isrc(self):
        """
        ISRC field.

        International Standard Recording Code of the recording of the work on the release (according to ISO 3901).

        :return: the ISRC
        """
        return self._isrc

    @property
    def media_type(self):
        """
        Media Type field.

        BIEM/CISAC code for media type.

        :return: the media type
        """
        return self._media_type

    @property
    def recording_format(self):
        """
        Recording Format field.

        Code that identifies the content of the recording: “A” (audio), “V” (video)..

        :return: the recording format
        """
        return self._recording_format

    @property
    def recording_technique(self):
        """
        Recording Technique field.

        Identifies the recording procedure: “A” (Analogue), “D” (Digital), “U” (Unknown).

        :return: the recording technique
        """
        return self._recording_technique


class Instrumentation(object):
    """
    Represents a CWR Instrumentation (INS).
    """

    def __init__(self, number_voices=None, instr_type=None, description=None):
        self._number_voices = number_voices
        self._instr_type = instr_type
        self._description = description

    @property
    def description(self):
        """
        Instrumentation Description field.

        Describes instrumentation if non-standard instrumentation is used on this work. Note that this field is required
        if IND records are not entered and if Standard Instrumentation Type is blank.

        :return: the description
        """
        return self._description

    @property
    def instr_type(self):
        """
        Standard Instrumentation Type field.

        Describes instrumentation if standard instrumentation is used on this work.  Note that this field is required if
        IND records are not entered and if Instrumentation Description is blank.  These values reside in the Standard
        Instrumentation Table.

        :return: the standard instrumentation type
        """
        return self._instr_type

    @property
    def number_voices(self):
        """
        Number of Voices field.

        Indicates the number of independent parts included in this work.

        :return: the number of voices
        """
        return self._number_voices


class InstrumentationDetail(object):
    """
    Represents a CWR Instrumentation Detail (IND)
    """

    def __init__(self, code, players):
        self._code = code
        self._players = players

    @property
    def code(self):
        """
        Instrument Code field.

        Indicates the use of a specific instrument in this version of instrumentation.  These values reside in the
        Instrument Table.

        :return: the instrument code
        """
        return self._code

    @property
    def players(self):
        """
        Number of Players field.

        Indicates the number of players for the above instrument.

        :return: the number of players
        """
        return self._players


class WorkOrigin(object):
    """
    Represents a CWR work origin.
    """

    def __init__(self, intended_purpose, production_title=None, cd_identifier=None, cut_number=None,
                 library=None, blt=None, visan_version=None, visan_isan=None, visan_episode=None,
                 visan_check_digit=None, production_id=None, episode_title=None,
                 episode_id=None, production_year=None, avi_key_society=None,
                 avi_key_number=None):
        self._intended_purpose = intended_purpose
        self._production_title = production_title
        self._cd_identifier = cd_identifier
        self._cut_number = cut_number
        self._library = library
        self._blt = blt
        self._visan_version = visan_version
        self._visan_isan = visan_isan
        self._visan_episode = visan_episode
        self._visan_check_digit = visan_check_digit
        self._production_id = production_id
        self._episode_title = episode_title
        self._episode_id = episode_id
        self._production_year = production_year
        self._avi_key_society = avi_key_society
        self._avi_key_number = avi_key_number

    @property
    def avi_key_number(self):
        """
        Audio-Visual Number field.

        Unique number  used internally by the ‘owning’ society  to identify the audio-visual work as referenced in the
        AV Index.

        :return: the audio-visual number field
        """
        return self._avi_key_number

    @property
    def avi_key_society(self):
        """
        AVI Society Code field.

        The CAE code of the society whose audio visual work detail entry is referenced in the AV Index.

        :return: the AVI society code
        """
        return self._avi_key_society

    @property
    def blt(self):
        """
        BLT field.

        An indication of the primary use of the work within the AV production.

        The definitive source for cue usage is the cue sheet.

        :return: the BLT
        """
        return self._blt

    @property
    def cd_identifier(self):
        """
        CD Identifier field.

        If Intended Purpose is equal to LIB (Library Work), enter the identifier associated with the CD upon which
        the work appears.

        :return: CD identifier
        """
        return self._cd_identifier

    @property
    def cut_number(self):
        """
        Cut Number field.

        If Intended Purpose is equal to LIB (Library Work), enter the track number on the CD Identifier where the work
        appears.  This field is required when CD Identifier is entered.

        :return: the cut number
        """
        return self._cut_number

    @property
    def episode_id(self):
        """
        Episode # field.

        Number assigned to the episode by the producer.

        :return: the episode number
        """
        return self._episode_id

    @property
    def episode_title(self):
        """
        Episode Title field.

        Title of the episode from which this work originated.

        :return: the episode title
        """
        return self._episode_title

    @property
    def intended_purpose(self):
        """
        Intended Purpose field.

        Indicates the type of production from which this work originated.

        These values reside in the Intended Purpose Table.

        :return: the inteded purpose
        """
        return self._intended_purpose

    @property
    def library(self):
        """
        Library field.

        The library from which this work originated.

        :return: the library
        """
        return self._library

    @property
    def production_id(self):
        """
        Production # field.

        The number generated by the production company to identify the work.

        :return: the production number field
        """
        return self._production_id

    @property
    def production_title(self):
        """
        Production Title field.

        Name of the production from which this work originated.

        :return: the production title
        """
        return self._production_title

    @property
    def production_year(self):
        """
        Year of Production field.

        The year in which the production of the film or episode was completed.

        :return: the year of production
        """
        return self._production_year

    @property
    def visan_check_digit(self):
        """
        V-ISAN Check Digit field.

        Unique identifier for audio-visual production in which this work is first used.

        Check digit to verify accuracy of ISAN.

        :return: the check digit
        """
        return self._visan_check_digit

    @property
    def visan_episode(self):
        """
        V-ISAN Episode field.

        Unique identifier for audio-visual production in which this work is first used.

        Unique identifier for episode.

        :return: the episode id
        """
        return self._visan_episode

    @property
    def visan_isan(self):
        """
        V-ISAN ISAN field.

        Unique identifier for audio-visual production in which this work is first used.

        ISAN portion of the V-ISAN.

        :return: the V-ISAN ISAN
        """
        return self._visan_isan

    @property
    def visan_version(self):
        """
        V-ISAN Version field.

        Unique identifier for audio-visual production in which this work is first used.

        Version portion of the V-ISAN.

        :return: the V-ISAN version
        """
        return self._visan_version


class PerformingArtist(object):
    """
    Represents a CWR Performing Artist (PER).
    """

    def __init__(self, last_name, first_name=None, cae_ipi_name=None, ipi_base_number=None):
        self._first_name = first_name
        self._last_name = last_name
        self._cae_ipi_name = cae_ipi_name
        self._ipi_base_number = ipi_base_number

    @property
    def cae_ipi_name(self):
        """
        Performing Artist CAE /IPI Name # field.

        The CAE # corresponding to this performing artist with 2 leading zero’s or the IPI Name #.

        Values reside in the IPI database.

        :return: the Performing Artist CAE/IPI name number
        """
        return self._cae_ipi_name

    @property
    def first_name(self):
        """
        Performing Artist First Name field.

        First name associated with the performing artist identified in the previous field.

        :return: the Performing Artist first name
        """
        return self._first_name

    @property
    def ipi_base_number(self):
        """
        Performing Artist IPI Base Number field.

        The IPI base number assigned to this performing artist.

        :return: the IPI base number
        """
        return self._ipi_base_number

    @property
    def last_name(self):
        """
        Performing Artist Last Name field.

        Last name of a person or full name of a group that has performed the work on a recording or in public.

        Note that if the performer is known by a single name, it should be entered in this field.

        :return: the Performing Artist last name
        """
        return self._last_name
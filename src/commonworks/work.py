# -*- encoding: utf-8 -*-


"""
Work entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Work(object):
    """
    Represents a CWR Work Title and Core Information.

    This record contains core information about the work itself, such as title and the unique codes that have been
    assigned to it.
    """

    def __init__(self, work_id, title, language_code, printed_edition_publication_date, copyright_number,
                 copyright_date, text_music_relationship, version_type,
                 music_arrangement=None, lyric_adaptation=None, excerpt_type=None, composite_type=None,
                 composite_component_count=1, iswc=None, cwr_work_type=None, musical_distribution_category=None,
                 duration=None, catalogue_number=None, opus_number=None, contact_id=None, contact_name=None,
                 recorded_indicator=False, priority_flag=False, exceptional_clause=False, grand_rights_indicator=False):
        # Work identifying info
        self._work_id = work_id
        self._title = title
        self._printed_edition_publication_date = printed_edition_publication_date
        self._language_code = language_code

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
        self._iswc = iswc
        self._cwr_work_type = cwr_work_type

        # Contact info
        self._contact_id = contact_id
        self._contact_name = contact_name

        # Other info
        self._priority_flag = priority_flag

    @property
    def catalogue_number(self):
        """
        Catalogue Number for serious music field.

        The work catalogue number. The abbreviated name of the catalogue is to be added (like BWV, KV), without dots.
        Part numbers are to be added with a # e.g. KV 297#1 (meaning Köchel Verzeichnis Nr.297 part 1).

        :return: the catalogue number for serious music
        """
        return self._catalogue_number

    @property
    def composite_component_count(self):
        """
        Composite Component Count field.

        If a Work consists of one original work and one sample, then the component count is two.

        :return: the composite count
        """
        return self._composite_component_count

    @property
    def composite_type(self):
        """
        Composite Type field.

        Certain works incorporate other works. If this work is such a case, choose the type of composite from the CWR
        values.

        :return: the Work composite type
        """
        return self._composite_type

    @property
    def contact_id(self):
        """
        Contact ID field.

        This is an identifier associated with the contact person.

        :return: the ID of the transaction's originator
        """
        return self._contact_id

    @property
    def contact_name(self):
        """
        Contact Name field.

        In the event of the need for a follow-up communication to you on the matter of this registration, it is useful
        to have the name of the person who originated the transaction.

        :return: the name of the transaction's originator
        """
        return self._contact_name

    @property
    def copyright_date(self):
        """
        Copyright Date field.

        This is the date that your national copyright office has registered this Work.

        :return: the date in which the Work was registered
        """
        return self._copyright_date

    @property
    def copyright_number(self):
        """
        Copyright Number field.

        This is the number that your national copyright office has assigned to this Work upon registration.

        :return: the Work Copyright number
        """
        return self._copyright_number

    @property
    def cwr_work_type(self):
        """
        CWR Work Type field.

        Indicates a genre found in the CWR Work Type table.

        :return: a genre found in the CWR Work Type table
        """
        return self._cwr_work_type

    @property
    def duration(self):
        """
        Duration field.

        Duration of the work.

        Duration is required only in the following cases:
        - By all societies if the Musical Work Distribution Category is Serious (e.g., music intended for symphonic,
        recital and chamber settings);
        - if there is a BMI interested party in this work and the Musical Work Distribution Category is Jazz.

        :return: duration of the work
        """
        return self._duration

    @property
    def exceptional_clause(self):
        """
        Exceptional Clause field.

        This is for registrations with GEMA.

        If it is True, the submitting GEMA-sub publisher has declared that the exceptional clause of the GEMA
        distribution rules with regard to printed editions applies (GEMA-Verteilungsplan A Anhang III).

        :return: True if GEMA-Verteilungsplan A Anhang III applies, False otherwise
        """
        return self._exceptional_clause

    @property
    def grand_rights_indicator(self):
        """
        Grand Rights Indicator field.

        Indicates whether or not this work is originally intended for live theatrical performance.

        :return: True if this work was originally intended for live theatrical performance, False otherwise
        """
        return self._grand_rights_indicator

    @property
    def excerpt_type(self):
        """
        Excerpt Type field.

        If this work is part of a larger work, indicates whether this is a movement or another, unspecified type of
        excerpt.

        :return: this Work's type of excerpt
        """
        return self._excerpt_type

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
    def lyric_adaptation(self):
        """
        Lyric Adaptation field.

        If it is indicated that this is a modified version of another work, this field indicates what changes,
        if any, have occurred to the original lyric.

        :return: the changes to the original lyric
        """
        return self._lyric_adaptation

    @property
    def music_arrangement(self):
        """
        Music Arrangement field.

        If it is indicated that this is a modified version of another work, this field indicates what changes,
        if any, have occurred to the original music.

        :return: the changes to the original music
        """
        return self._music_arrangement

    @property
    def musical_distribution_category(self):
        """
        Musical Work Distribution Category field.

        Certain rights organizations have special distribution rules that apply to certain genres of music.

        All such genres for participating societies can be found in the Musical Work Distribution Category Table in
        the layout document.

        :return:
        """
        return self._musical_distribution_category

    @property
    def opus_number(self):
        """
        Opus Number for serious music field.

        The number assigned to this work, usually by the composer. Part numbers are to be added with a # e.g. 28#3
        (meaning Opus 28 part 3).

        :return: opus number for the work
        """
        return self._opus_number

    @property
    def printed_edition_publication_date(self):
        """
        Date of Publication of Printed Edition field.

        The date that the printed, new edition published by the submitting Publisher appeared.

        This information is especially relevant for the notification of sub published works by GEMA-sub publishers.

        :return: the date of the new edition
        """
        return self._printed_edition_publication_date

    @property
    def priority_flag(self):
        """
        Priority Flag field.

        Use this flag to indicate that the registration of this work should be expedited. This flag should be used
        sparingly – only when the work is high on the charts, etc.

        :return:
        """
        return self._priority_flag

    @property
    def recorded_indicator(self):
        """
        Recorded Indicator field.

        Indicates whether a recording of this work exists that has been made available to the public.

        :return: True if there is a public recording of this work, False otherwise
        """
        return self._recorded_indicator

    @property
    def text_music_relationship(self):
        """
        Text-Music Relationship field.

        Indicates whether this Work contains text only, music only, or a combination of both. (It is understood that a
        Work with lyrics may be performed instrumentally, and that a work with music may be performed spoken-only.)

        :return: the lyrical and musical composition of the Work
        """
        return self._text_music_relationship

    @property
    def title(self):
        """
        Work Title field.

        The title by which the work is best known.

        Alternative titles should be indicated using the AlternativeWorkTitle class.

        Do not store additional information in the title field e.g. “instrumental” or “background”.
        Such information should be stored in the designated field.

        :return: the title by which the work is best known
        """
        return self._title

    @property
    def version_type(self):
        """
        Version Type field.

        Indicate whether this work is entirely original, or based on another work. If the work is based on another work,
        values must be given for the Music Arrangement and Lyric Adaptation fields. If the work is a modified version of
        a copyrighted work, it is necessary for it to be authorized.

        :return: the Work's version type
        """
        return self._version_type

    @property
    def work_id(self):
        """
        Submitter Work Number field.

        This is your unique numerical code for this work.

        It is important that this number refer only to the work named on the registration, since further electronic
        communication (ACK, ISW, EXC) that includes this number will point to this work and its interested parties.

        :return: your unique numerical code for this work
        """
        return self._work_id


class AlternateTitle(object):
    """
    Represents a CWR Alternate Title.
    """

    def __init__(self, alternate_title, title_type, language = None):
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


class EntireWorkTitle(object):
    """
    Represents a CWR entire work title.

    If the work is an excerpt this object reflects the entire work from where it comes.
    """

    def __init__(self, entire_title, entire_work_iswc, language_code
                 , writer_one_first_name, writer_one_last_name,
                 writer_one_ipi_cae, writer_one_ipi_base_number,
                 writer_two_first_name, writer_two_last_name, writer_two_ipi_cae, writer_two_ipi_base_number,
                 work_number):
        self._entire_title = entire_title
        self._entire_work_iswc = entire_work_iswc
        self._language_code = language_code
        self._writer_one_first_name = writer_one_first_name
        self._writer_one_last_name = writer_one_last_name
        self._writer_one_ipi_cae = writer_one_ipi_cae
        self._writer_one_ipi_base_number = writer_one_ipi_base_number
        self._writer_two_first_name = writer_two_first_name
        self._writer_two_last_name = writer_two_last_name
        self._writer_two_ipi_cae = writer_two_ipi_cae
        self._writer_two_ipi_base_number = writer_two_ipi_base_number
        self._work_number = work_number

    @property
    def entire_title(self):
        return self._entire_title

    @property
    def entire_work_iswc(self):
        return self._entire_work_iswc

    @property
    def language_code(self):
        return self._language_code

    @property
    def work_number(self):
        return self._work_number

    @property
    def writer_one_first_name(self):
        return self._writer_one_first_name

    @property
    def writer_one_ipi_base_number(self):
        return self._writer_one_ipi_base_number

    @property
    def writer_one_ipi_cae(self):
        return self._writer_one_ipi_cae

    @property
    def writer_one_last_name(self):
        return self._writer_one_last_name

    @property
    def writer_two_first_name(self):
        return self._writer_two_first_name

    @property
    def writer_two_ipi_base_number(self):
        return self._writer_two_ipi_base_number

    @property
    def writer_two_ipi_cae(self):
        return self._writer_two_ipi_cae

    @property
    def writer_two_last_name(self):
        return self._writer_two_last_name


class OriginalWorkTitle(object):
    """
    Represents a CWR original work title.

    If the work is a version this reflect the original one which is versioned.
    """

    def __init__(self, entire_title, entire_work_iswc, language_code, writer_one_first_name, writer_one_last_name,
                 writer_one_ipi_cae, writer_one_ipi_base_number, writer_two_first_name,
                 writer_two_last_name, writer_two_ipi_cae,
                 writer_two_ipi_base_number, work_number):
        self._entire_title = entire_title
        self._entire_work_iswc = entire_work_iswc
        self._language_code = language_code
        self._writer_one_first_name = writer_one_first_name
        self._writer_one_last_name = writer_one_last_name
        self._writer_one_ipi_cae = writer_one_ipi_cae
        self._writer_one_ipi_base_number = writer_one_ipi_base_number
        self._writer_two_first_name = writer_two_first_name
        self._writer_two_last_name = writer_two_last_name
        self._writer_two_ipi_cae = writer_two_ipi_cae
        self._writer_two_ipi_base_number = writer_two_ipi_base_number
        self._work_number = work_number

    @property
    def entire_title(self):
        return self._entire_title

    @property
    def entire_work_iswc(self):
        return self._entire_work_iswc

    @property
    def language_code(self):
        return self._language_code

    @property
    def work_number(self):
        return self._work_number

    @property
    def writer_one_first_name(self):
        return self._writer_one_first_name

    @property
    def writer_one_ipi_base_number(self):
        return self._writer_one_ipi_base_number

    @property
    def writer_one_ipi_cae(self):
        return self._writer_one_ipi_cae

    @property
    def writer_one_last_name(self):
        return self._writer_one_last_name

    @property
    def writer_two_first_name(self):
        return self._writer_two_first_name

    @property
    def writer_two_ipi_base_number(self):
        return self._writer_two_ipi_base_number

    @property
    def writer_two_ipi_cae(self):
        return self._writer_two_ipi_cae

    @property
    def writer_two_last_name(self):
        return self._writer_two_last_name


class RecordingDetails(object):
    """
    Represents a CWR recording details.
    """

    def __init__(self, first_release_date, first_release_duration, first_album_title,
                 first_album_label, first_release_catalog_id, ean,
                 isrc, recording_format, recording_technique, media_type):
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
        return self._ean

    @property
    def first_album_label(self):
        return self._first_album_label

    @property
    def first_album_title(self):
        return self._first_album_title

    @property
    def first_release_catalog_id(self):
        return self._first_release_catalog_id

    @property
    def first_release_date(self):
        return self._first_release_date

    @property
    def first_release_duration(self):
        return self._first_release_duration

    @property
    def isrc(self):
        return self._isrc

    @property
    def media_type(self):
        return self._media_type

    @property
    def recording_format(self):
        return self._recording_format

    @property
    def recording_technique(self):
        return self._recording_technique


class WorkOrigin(object):
    """
    Represents a CWR work origin.
    """

    def __init__(self, intended_purpose, production_title, cd_identifier, cut_number,
                 library, blt, visan_version, visan_isan, visan_episode,
                 visan_check_digit, production_id, episode_title,
                 episode_id, production_year, avi_key_society,
                 avi_key_number):
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
        return self._avi_key_number

    @property
    def avi_key_society(self):
        return self._avi_key_society

    @property
    def blt(self):
        return self._blt

    @property
    def cd_identifier(self):
        return self._cd_identifier

    @property
    def cut_number(self):
        return self._cut_number

    @property
    def episode_id(self):
        return self._episode_id

    @property
    def episode_title(self):
        return self._episode_title

    @property
    def intended_purpose(self):
        return self._intended_purpose

    @property
    def library(self):
        return self._library

    @property
    def production_id(self):
        return self._production_id

    @property
    def production_title(self):
        return self._production_title

    @property
    def production_year(self):
        return self._production_year

    @property
    def visan_check_digit(self):
        return self._visan_check_digit

    @property
    def visan_episode(self):
        return self._visan_episode

    @property
    def visan_isan(self):
        return self._visan_isan

    @property
    def visan_version(self):
        return self._visan_version


class PerformingArtist(object):
    """
    Represents a CWR performing artist.
    """

    def __init__(self, first_name, last_name, cae_ipi_name, ipi_base_number):
        self._first_name = first_name
        self._last_name = last_name
        self._cae_ipi_name = cae_ipi_name
        self._ipi_base_number = ipi_base_number

    @property
    def cae_ipi_name(self):
        return self._cae_ipi_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def ipi_base_number(self):
        return self._ipi_base_number

    @property
    def last_name(self):
        return self._last_name
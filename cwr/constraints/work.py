# -*- encoding: utf-8 -*-

import pyparsing as pp


"""
CWR Work constraints.

These are for validating works.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def ser_has_duration(work):
    """
    Ensures that serious music works have a duration set.

    The validation fails if:
    - The Musical Work Distribution Category is set to 'SER' and no duration has been set

    :param work: the work to validate
    """

    if work.musical_distribution_category == 'SER':
        # Musical Distribution Category is 'serious'
        if not work.duration or (work.duration.hour == 0 and work.duration.minute == 0 and work.duration.second == 0):
            # No duration has been set
            # Or
            # Duration is zero
            message = 'When the Musical Distribution Category is set to %s the duration should be higher than 0' % \
                      work.musical_distribution_category
            raise pp.ParseException('', msg=message)


def mod_has_music_arrangement(work):
    """
    Ensures that modified music works have a musical arrangement.

    The validation fails if:
    - The Version Type is set to 'MOD' and no Music Arrangement is set

    :param work: the work to validate
    """

    if work.version_type == 'MOD':
        if not work.music_arrangement or len(work.music_arrangement) == 0:
            message = 'When the Version Type is set to %s the Music Arrangement must be set' % \
                      work.version_type
            raise pp.ParseException('', msg=message)


def mod_has_lyric_adaptation(work):
    """
    Ensures that modified music works have a lyrical adaptation.

    The validation fails if:
    - The Version Type is set to 'MOD' and no Lyric Adaptation is set

    :param work: the work to validate
    """

    if work.version_type == 'MOD':
        # Version type is 'MOD'
        if not work.lyric_adaptation or len(work.lyric_adaptation) == 0:
            # No Lyric Adaptation set
            # Or
            # Lyric Adaptation is empty
            message = 'When the Version Type is set to %s the Lyric Adaptation must be set' % \
                      work.version_type
            raise pp.ParseException('', msg=message)


def composite_has_count(work):
    """
    Ensures that composite works have a composite count.

    The validation fails if:
    - The Composite Type is set and the Composite Component Count is 0

    :param work: the work to validate
    """

    if work.composite_type and work.composite_component_count == 0:
        raise pp.ParseException('',
                                msg='When the Composite Type is set the Composite Component Count should be greater than 0')


def count_when_composite(work):
    """
    Ensures that if the composite count is set then the work is set as a composite work.

    The validation fails if:
    - The Composite Component Count is greater than 0 and the Composite Type is not set

    :param work: the work to validate
    """

    if work.composite_component_count > 0 and not work.composite_type:
        raise pp.ParseException('',
                                msg='When the Composite Component Count is greater than 0 the Composite Type should be set')

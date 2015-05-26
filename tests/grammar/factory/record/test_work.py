# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Work grammar tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWorkValid(unittest.TestCase):
    """
    Tests that the Work grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('work')

    def test_valid_common(self):
        record = 'NWR0000019900000000WORK NAME                                                     1450455                  00000000            UNC000000YMTX   ORI   ORIORI                                          N00000000000U                                                  Y'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NWR', result.record_type)
        self.assertEqual(199, result.transaction_sequence_n)
        self.assertEqual(0, result.record_sequence_n)
        self.assertEqual('WORK NAME', result.title)
        self.assertEqual(None, result.language_code)
        self.assertEqual('1450455', result.submitter_work_n)
        self.assertEqual(None, result.iswc)
        self.assertEqual(None, result.copyright_date)
        self.assertEqual(None, result.copyright_number)
        self.assertEqual('UNC', result.musical_work_distribution_category)
        self.assertEqual(0, result.duration.hour)
        self.assertEqual(0, result.duration.minute)
        self.assertEqual(0, result.duration.second)
        self.assertEqual('Y', result.recorded_indicator)
        self.assertEqual('MTX', result.text_music_relationship)
        self.assertEqual(None, result.composite_type)
        self.assertEqual('ORI', result.version_type)
        self.assertEqual(None, result.excerpt_type)
        self.assertEqual('ORI', result.music_arrangement)
        self.assertEqual('ORI', result.lyric_adaptation)
        self.assertEqual(None, result.contact_name)
        self.assertEqual(None, result.contact_id)
        self.assertEqual(None, result.work_type)
        self.assertEqual(False, result.grand_rights_indicator)
        self.assertEqual(0, result.composite_component_count)
        self.assertEqual(None, result.date_publication_printed_edition)
        self.assertEqual('U', result.exceptional_clause)
        self.assertEqual(None, result.opus_number)
        self.assertEqual(None, result.catalogue_number)
        self.assertEqual('Y', result.priority_flag)

    def test_valid_common_b(self):
        record = 'NWR0000000000000000MUSIC WORK                                                  ES000000199     T035117711120391002            POP000300U      ORI                                                    00000000000                                                    '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NWR', result.record_type)
        self.assertEqual(0, result.transaction_sequence_n)
        self.assertEqual(0, result.record_sequence_n)
        self.assertEqual('MUSIC WORK', result.title)
        self.assertEqual('ES', result.language_code)
        self.assertEqual('000000199', result.submitter_work_n)
        self.assertEqual(35117711, result.iswc.id_code)
        self.assertEqual(1, result.iswc.check_digit)
        self.assertEqual(2039, result.copyright_date.year)
        self.assertEqual(10, result.copyright_date.month)
        self.assertEqual(2, result.copyright_date.day)
        self.assertEqual(None, result.copyright_number)
        self.assertEqual('POP', result.musical_work_distribution_category)
        self.assertEqual(0, result.duration.hour)
        self.assertEqual(3, result.duration.minute)
        self.assertEqual(0, result.duration.second)
        self.assertEqual('U', result.recorded_indicator)
        self.assertEqual(None, result.text_music_relationship)
        self.assertEqual(None, result.composite_type)
        self.assertEqual('ORI', result.version_type)
        self.assertEqual(None, result.excerpt_type)
        self.assertEqual(None, result.music_arrangement)
        self.assertEqual(None, result.lyric_adaptation)
        self.assertEqual(None, result.contact_name)
        self.assertEqual(None, result.contact_id)
        self.assertEqual(None, result.work_type)
        self.assertEqual(None, result.grand_rights_indicator)
        self.assertEqual(0, result.composite_component_count)
        self.assertEqual(None, result.date_publication_printed_edition)
        self.assertEqual(None, result.exceptional_clause)
        self.assertEqual(None, result.opus_number)
        self.assertEqual(None, result.catalogue_number)
        self.assertEqual(None, result.priority_flag)

    def test_valid_full(self):
        """
        Tests that the Work grammar decodes correctly formatted Work record.

        This test contains all the optional fields.
        """
        record = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NWR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('TITLE OF THE WORK', result.title)
        self.assertEqual('EN', result.language_code)
        self.assertEqual('ABCD0123456789', result.submitter_work_n)
        self.assertEqual(12345678, result.iswc.id_code)
        self.assertEqual(9, result.iswc.check_digit)
        self.assertEqual(1, result.copyright_date.month)
        self.assertEqual(2, result.copyright_date.day)
        self.assertEqual(2013, result.copyright_date.year)
        self.assertEqual('AB0123456789', result.copyright_number)
        self.assertEqual('POP', result.musical_work_distribution_category)
        self.assertEqual(3, result.duration.hour)
        self.assertEqual(2, result.duration.minute)
        self.assertEqual(1, result.duration.second)
        self.assertEqual('Y', result.recorded_indicator)
        self.assertEqual('MUS', result.text_music_relationship)
        self.assertEqual('POT', result.composite_type)
        self.assertEqual('MOD', result.version_type)
        self.assertEqual('MOV', result.excerpt_type)
        self.assertEqual('ORI', result.music_arrangement)
        self.assertEqual('ORI', result.lyric_adaptation)
        self.assertEqual('THE CONTACT', result.contact_name)
        self.assertEqual('A123456789', result.contact_id)
        self.assertEqual('AR', result.work_type)
        self.assertEqual(True, result.grand_rights_indicator)
        self.assertEqual(12, result.composite_component_count)
        self.assertEqual(2, result.date_publication_printed_edition.day)
        self.assertEqual(3, result.date_publication_printed_edition.month)
        self.assertEqual(2014, result.date_publication_printed_edition.year)
        self.assertEqual('Y', result.exceptional_clause)
        self.assertEqual('28#3', result.opus_number)
        self.assertEqual('KV 297#1', result.catalogue_number)
        self.assertEqual('Y', result.priority_flag)

    def test_valid_minimum(self):
        """
        Tests that the Work grammar decodes correctly formatted Work record.

        This test contains no optional fields.
        """
        record = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUS   ORIMOV      THE CONTACT                   A123456789   00020140302Y28#3                     KV 297#1                 Y'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NWR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('TITLE OF THE WORK', result.title)
        self.assertEqual('EN', result.language_code)
        self.assertEqual('ABCD0123456789', result.submitter_work_n)
        self.assertEqual(12345678, result.iswc.id_code)
        self.assertEqual(9, result.iswc.check_digit)
        self.assertEqual(1, result.copyright_date.month)
        self.assertEqual(2, result.copyright_date.day)
        self.assertEqual(2013, result.copyright_date.year)
        self.assertEqual('AB0123456789', result.copyright_number)
        self.assertEqual('POP', result.musical_work_distribution_category)
        self.assertEqual(3, result.duration.hour)
        self.assertEqual(2, result.duration.minute)
        self.assertEqual(1, result.duration.second)
        self.assertEqual('Y', result.recorded_indicator)
        self.assertEqual('MUS', result.text_music_relationship)
        self.assertEqual(None, result.composite_type)
        self.assertEqual('ORI', result.version_type)
        self.assertEqual('MOV', result.excerpt_type)
        self.assertEqual(None, result.music_arrangement)
        self.assertEqual(None, result.lyric_adaptation)
        self.assertEqual('THE CONTACT', result.contact_name)
        self.assertEqual('A123456789', result.contact_id)
        self.assertEqual(None, result.work_type)
        self.assertEqual(None, result.grand_rights_indicator)
        self.assertEqual(0, result.composite_component_count)
        self.assertEqual(2, result.date_publication_printed_edition.day)
        self.assertEqual(3, result.date_publication_printed_edition.month)
        self.assertEqual(2014, result.date_publication_printed_edition.year)
        self.assertEqual('Y', result.exceptional_clause)
        self.assertEqual('28#3', result.opus_number)
        self.assertEqual('KV 297#1', result.catalogue_number)
        self.assertEqual('Y', result.priority_flag)


class TestIPAGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('work')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)

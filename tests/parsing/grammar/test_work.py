# -*- encoding: utf-8 -*-
import unittest
from cwr.parsing.grammar import work

from pyparsing import ParseException

from cwr.parsing.grammar import transmission


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
        self.grammar = work.work_record

    def test_valid_full(self):
        """
        Tests that the Work grammar decodes correctly formatted Work record.

        This test contains all the optional fields.
        """
        record = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789A012345678920130102AB0123456789POP030201YMUSPOTMODMOVNEWNONTHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        result = self.grammar.parseString(record)[0]
        print self.grammar.parseString(record)
"""
        self.assertEqual('NWR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('TITLE OF THE WORK', result.title)
        self.assertEqual('EN', result.language_code)
        self.assertEqual('ABCD0123456789', result.work_id)
        self.assertEqual('A0123456789', result.iswc)
        self.assertEqual(1, result.copyright_date.month)
        self.assertEqual(2, result.copyright_date.day)
        self.assertEqual(2013, result.copyright_date.year)
        self.assertEqual('AB0123456789', result.copyright_number)
        self.assertEqual('POP', result.musical_distribution_category)
        self.assertEqual(3, result.duration.hour)
        self.assertEqual(2, result.duration.minute)
        self.assertEqual(1, result.duration.second)
        self.assertEqual('Y', result.recorded_indicator)
        self.assertEqual('MUS', result.text_music_relationship)
        self.assertEqual('POT', result.composite_type)
        self.assertEqual('MOD', result.version_type)
        self.assertEqual('MOV', result.excerpt_type)
        self.assertEqual('NEW', result.music_arrangement)
        self.assertEqual('NON', result.lyric_adaptation)
        self.assertEqual('THE CONTACT', result.contact_name)
        self.assertEqual('A123456789', result.contact_id)
        self.assertEqual('AR', result.cwr_work_type)
        self.assertEqual(True, result.grand_rights_indicator)
        self.assertEqual(12, result.composite_component_count)
        self.assertEqual(2, result.printed_edition_publication_date.month)
        self.assertEqual(3, result.printed_edition_publication_date.day)
        self.assertEqual(2014, result.printed_edition_publication_date.year)
        self.assertEqual('Y', result.exceptional_clause)
        self.assertEqual('28#3', result.opus_number)
        self.assertEqual('KV 297#1', result.catalogue_number)
        self.assertEqual('Y', result.priority_flag)"""

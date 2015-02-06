# -*- encoding: utf-8 -*-

import unittest
import datetime

from commonworks.agreement import AgreementTerritory, Agreement, IPA
from commonworks.work import AlternateTitle, EntireWorkTitle, OriginalWorkTitle, \
    PerformingArtist, WorkOrigin, RecordingDetails, Work
from commonworks.interested_party import Publisher
from commonworks.society import Society
from commonworks.territory import Territory
from commonworks.value_entity import ValueEntity
from commonworks.interested_party import Writer
from commonworks.utils.dict_encoder import CWRDictionaryEncoder


"""
Unit tests to check if the CWRDictionaryEncoder class encodes the objects into dictionaries correctly.

Only valid cases are tested here. The used objects should have no errors.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreementTerritory(unittest.TestCase):
    """
    Tests the AgreementTerritory to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = AgreementTerritory(True, 2)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['included'], True)
        self.assertEqual(self.dict['tis_numeric_code'], 2)


class TestAgreement(unittest.TestCase):
    """
    Tests the Agreement to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Agreement(1, 2, 'Original', datetime.date(2015, 1, 11), datetime.date(2015, 2, 11),
                           'D', 'D', datetime.date(2015, 6, 11), 122, 'S',
                           international_standard_code=3, retention_end_date=datetime.date(2015, 3, 11),
                           prior_royalty_status_date=datetime.date(2015, 4, 11),
                           post_term_collection_end_date=datetime.date(2015, 5, 11),
                           shares_change=True, advance_given=True)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['submitter_agreement_number'], 1)
        self.assertEqual(self.dict['society_agreement_number'], 2)
        self.assertEqual(self.dict['international_standard_number'], 3)
        self.assertEqual(self.dict['agreement_type'], 'Original')

        self.assertEqual(self.dict['start_date'], datetime.date(2015, 1, 11).isoformat())
        self.assertEqual(self.dict['end_date'], datetime.date(2015, 2, 11).isoformat())

        self.assertEqual(self.dict['prior_royalty_status'], 'D')
        self.assertEqual(self.dict['prior_royalty_status_date'], datetime.date(2015, 4, 11).isoformat())

        self.assertEqual(self.dict['post_term_collection_status'], 'D')
        self.assertEqual(self.dict['post_term_collection_end_date'], datetime.date(2015, 5, 11).isoformat())

        self.assertEqual(self.dict['retention_end_date'], datetime.date(2015, 3, 11).isoformat())
        self.assertEqual(self.dict['signature_date'], datetime.date(2015, 6, 11).isoformat())
        self.assertEqual(self.dict['works_number'], 122)
        self.assertEqual(self.dict['sales_manufacture_clause'], 'S')
        self.assertEqual(self.dict['shares_change'], True)
        self.assertEqual(self.dict['advance_given'], True)


class TestAlternativeWorkTitle(unittest.TestCase):
    """
    Tests the AlternativeWorkTitle to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = AlternateTitle('title', 1, 'ES')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['alternate_title'], 'title')
        self.assertEqual(self.dict['title_type'], 1)
        self.assertEqual(self.dict['language'], 'ES')


class TestEntireWorkTitle(unittest.TestCase):
    """
    Tests the EntireWorkTitle to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = EntireWorkTitle('title', 1, 'ES',
                                 'name1', 'surname1', 2, 3,
                                 'name2', 'surname2', 4, 5,
                                 6)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['entire_title'], 'title')
        self.assertEqual(self.dict['entire_work_iswc'], 1)
        self.assertEqual(self.dict['language_code'], 'ES')
        self.assertEqual(self.dict['writer_one_first_name'], 'name1')
        self.assertEqual(self.dict['writer_one_last_name'], 'surname1')
        self.assertEqual(self.dict['writer_one_ipi_cae'], 2)
        self.assertEqual(self.dict['writer_one_ipi_base_number'], 3)
        self.assertEqual(self.dict['writer_two_first_name'], 'name2')
        self.assertEqual(self.dict['writer_two_last_name'], 'surname2')
        self.assertEqual(self.dict['writer_two_ipi_cae'], 4)
        self.assertEqual(self.dict['writer_two_ipi_base_number'], 5)


class TestIPAAgreement(unittest.TestCase):
    """
    Tests the IPAAgreement to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = IPA(1, 2, 'party', 'assign', 'writer', 3, 4, 0.1, 5, 0.2, 6, 0.3)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(1, self.dict['agreement_id'])
        self.assertEqual(2, self.dict['interested_party_id'])
        self.assertEqual('party', self.dict['interested_party_name'])
        self.assertEqual('assign', self.dict['agreement_role_code'])
        self.assertEqual('writer', self.dict['interested_party_writer_name'])
        self.assertEqual(3, self.dict['interested_party_ipi'])
        self.assertEqual(4, self.dict['pr_society'])
        self.assertEqual(0.1, self.dict['pr_share'])
        self.assertEqual(5, self.dict['mr_society'])
        self.assertEqual(0.2, self.dict['mr_share'])
        self.assertEqual(6, self.dict['sr_society'])
        self.assertEqual(0.3, self.dict['sr_share'])


class TestOriginalWorkTitle(unittest.TestCase):
    """
    Tests the OriginalWorkTitle to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = OriginalWorkTitle('title', 2, 'ES',
                                   'name1', 'surname1', 3, 4,
                                   'name2', 'surname2', 5, 6, 7)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['entire_title'], 'title')
        self.assertEqual(self.dict['entire_work_iswc'], 2)
        self.assertEqual(self.dict['language_code'], 'ES')
        self.assertEqual(self.dict['writer_one_first_name'], 'name1')
        self.assertEqual(self.dict['writer_one_last_name'], 'surname1')
        self.assertEqual(self.dict['writer_one_ipi_cae'], 3)
        self.assertEqual(self.dict['writer_one_ipi_base_number'], 4)
        self.assertEqual(self.dict['writer_two_first_name'], 'name2')
        self.assertEqual(self.dict['writer_two_last_name'], 'surname2')
        self.assertEqual(self.dict['writer_two_ipi_cae'], 5)
        self.assertEqual(self.dict['writer_two_ipi_base_number'], 6)


class TestPerformingArtist(unittest.TestCase):
    """
    Tests the PerformingArtist to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = PerformingArtist('name', 'surname', 1, 2)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['first_name'], 'name')
        self.assertEqual(self.dict['last_name'], 'surname')
        self.assertEqual(self.dict['cae_ipi_name'], 1)
        self.assertEqual(self.dict['ipi_base_number'], 2)


class TestPublisher(unittest.TestCase):
    """
    Tests the Publisher to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Publisher('publisher1', 1, 'name_ip', 2, 3)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['name'], 'publisher1')
        self.assertEqual(self.dict['ip_id'], 1)
        self.assertEqual(self.dict['ip_name'], 'name_ip')
        self.assertEqual(self.dict['ip_base_id'], 2)
        self.assertEqual(self.dict['tax_id'], 3)


class TestRecordingDetails(unittest.TestCase):
    """
    Tests the RecordingDetails to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = RecordingDetails(datetime.date(2015, 1, 11), 1, 'title', 'label', 2,
                                  3, 4, 5, 6, 7)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['first_release_date'], datetime.date(2015, 1, 11).isoformat())
        self.assertEqual(self.dict['first_release_duration'], 1)
        self.assertEqual(self.dict['first_album_title'], 'title')
        self.assertEqual(self.dict['first_album_label'], 'label')
        self.assertEqual(self.dict['first_release_catalog_id'], 2)
        self.assertEqual(self.dict['ean'], 3)
        self.assertEqual(self.dict['isrc'], 4)
        self.assertEqual(self.dict['recording_format'], 5)
        self.assertEqual(self.dict['recording_technique'], 6)
        self.assertEqual(self.dict['media_type'], 7)


class TestSociety(unittest.TestCase):
    """
    Tests the Society to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Society(1, 'name', 'formerly')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['name'], 'name')
        self.assertEqual(self.dict['former_name'], 'formerly')


class TestTerritory(unittest.TestCase):
    """
    Tests the Territory to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Territory(1, 2, 3, 'name', 'official')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['tis'], 1)
        self.assertEqual(self.dict['iso2'], 2)
        self.assertEqual(self.dict['type'], 3)
        self.assertEqual(self.dict['name'], 'name')
        self.assertEqual(self.dict['official_name'], 'official')


class TestValueEntity(unittest.TestCase):
    """
    Tests the ValueEntity to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = ValueEntity(1, 'name', 'desc')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['id'], 1)
        self.assertEqual(self.dict['name'], 'name')
        self.assertEqual(self.dict['description'], 'desc')


class TestWork(unittest.TestCase):
    """
    Tests the Work to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Work(1, 'The Title', 'ES', datetime.date(2015, 1, 11), 2, datetime.date(2015, 1, 12),
                      'text_only', 'original', 'none', 'none', 'movement', 'composite', 3, 4, 'jazz',
                      'category', 60, 5, '28#3', 'name_id', 'Person', True, True, True, True)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(1, self.dict['work_id'])
        self.assertEqual('The Title', self.dict['title'])
        self.assertEqual('ES', self.dict['language_code'])
        self.assertEqual(datetime.date(2015, 1, 11).isoformat(), self.dict['printed_edition_publication_date'])
        self.assertEqual(2, self.dict['copyright_number'])
        self.assertEqual(datetime.date(2015, 1, 12).isoformat(), self.dict['copyright_date'])
        self.assertEqual('text_only', self.dict['text_music_relationship'])
        self.assertEqual('original', self.dict['version_type'])
        self.assertEqual('none', self.dict['music_arrangement'])
        self.assertEqual('none', self.dict['lyric_adaptation'])
        self.assertEqual('movement', self.dict['excerpt_type'])
        self.assertEqual('composite', self.dict['composite_type'])
        self.assertEqual(3, self.dict['composite_component_count'])
        self.assertEqual(4, self.dict['iswc'])
        self.assertEqual('jazz', self.dict['cwr_work_type'])
        self.assertEqual('category', self.dict['musical_distribution_category'])
        self.assertEqual(60, self.dict['duration'])
        self.assertEqual(5, self.dict['catalogue_number'])
        self.assertEqual('28#3', self.dict['opus_number'])
        self.assertEqual('name_id', self.dict['contact_id'])
        self.assertEqual('Person', self.dict['contact_name'])
        self.assertEqual(True, self.dict['recorded_indicator'])
        self.assertEqual(True, self.dict['priority_flag'])
        self.assertEqual(True, self.dict['exceptional_clause'])
        self.assertEqual(True, self.dict['grand_rights_indicator'])


class TestWorkOrigin(unittest.TestCase):
    """
    Tests the WorkOrigin to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = WorkOrigin(1, 'title', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'episode', 11, 1995, 12, 13)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['intended_purpose'], 1)
        self.assertEqual(self.dict['production_title'], 'title')
        self.assertEqual(self.dict['cd_identifier'], 2)
        self.assertEqual(self.dict['cut_number'], 3)
        self.assertEqual(self.dict['library'], 4)
        self.assertEqual(self.dict['blt'], 5)
        self.assertEqual(self.dict['visan_version'], 6)
        self.assertEqual(self.dict['visan_isan'], 7)
        self.assertEqual(self.dict['visan_episode'], 8)
        self.assertEqual(self.dict['visan_check_digit'], 9)
        self.assertEqual(self.dict['production_id'], 10)
        self.assertEqual(self.dict['episode_title'], 'episode')
        self.assertEqual(self.dict['episode_id'], 11)
        self.assertEqual(self.dict['production_year'], 1995)
        self.assertEqual(self.dict['avi_key_society'], 12)
        self.assertEqual(self.dict['avi_key_number'], 13)


class TestWriter(unittest.TestCase):
    """
    Tests the Writer to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Writer('name', 1, 2, 'ip', 3, 'surname')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['first_name'], 'name')
        self.assertEqual(self.dict['personal_number'], 1)
        self.assertEqual(self.dict['ip_id'], 2)
        self.assertEqual(self.dict['ip_name'], 'ip')
        self.assertEqual(self.dict['ip_base_id'], 3)
        self.assertEqual(self.dict['last_name'], 'surname')


if __name__ == '__main__':
    unittest.main()
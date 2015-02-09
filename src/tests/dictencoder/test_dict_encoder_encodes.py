# -*- encoding: utf-8 -*-

import unittest
import datetime

from commonworks.agreement import AgreementTerritory, Agreement, IPA
from commonworks.interested_party import Publisher, Writer
from commonworks.society import Society
from commonworks.territory import Territory
from commonworks.value_entity import ValueEntity
from commonworks.work import AlternateTitle, AuthoredWork, \
    PerformingArtist, WorkOrigin, RecordingDetails, Work
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
        self.assertEqual(True, self.dict['included'])
        self.assertEqual(2, self.dict['tis_numeric_code'])


class TestAgreement(unittest.TestCase):
    """
    Tests the Agreement to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Agreement(1, 'Original', datetime.date(2015, 1, 11), 'D', 'D', datetime.date(2015, 6, 11),
                           122, society_agreement_number=2, international_standard_code=3,
                           sales_manufacture_clause='S',
                           end_date=datetime.date(2015, 2, 11),
                           retention_end_date=datetime.date(2015, 3, 11),
                           prior_royalty_status_date=datetime.date(2015, 4, 11),
                           post_term_collection_end_date=datetime.date(2015, 5, 11),
                           shares_change=True, advance_given=True)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(1, self.dict['submitter_agreement_number'])
        self.assertEqual(2, self.dict['society_agreement_number'])
        self.assertEqual(3, self.dict['international_standard_number'])
        self.assertEqual('Original', self.dict['agreement_type'])

        self.assertEqual(datetime.date(2015, 1, 11).isoformat(), self.dict['start_date'])
        self.assertEqual(datetime.date(2015, 2, 11).isoformat(), self.dict['end_date'])

        self.assertEqual('D', self.dict['prior_royalty_status'])
        self.assertEqual(datetime.date(2015, 4, 11).isoformat(), self.dict['prior_royalty_status_date'])

        self.assertEqual('D', self.dict['post_term_collection_status'])
        self.assertEqual(datetime.date(2015, 5, 11).isoformat(), self.dict['post_term_collection_end_date'])

        self.assertEqual(datetime.date(2015, 3, 11).isoformat(), self.dict['retention_end_date'])
        self.assertEqual(datetime.date(2015, 6, 11).isoformat(), self.dict['signature_date'])
        self.assertEqual(122, self.dict['works_number'])
        self.assertEqual('S', self.dict['sales_manufacture_clause'])
        self.assertEqual(True, self.dict['shares_change'])
        self.assertEqual(True, self.dict['advance_given'])


class TestAlternativeWorkTitle(unittest.TestCase):
    """
    Tests the AlternativeWorkTitle to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = AlternateTitle('title', 1, 'ES')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual('title', self.dict['alternate_title'])
        self.assertEqual(1, self.dict['title_type'])
        self.assertEqual('ES', self.dict['language'])


class TestAuthoredWork(unittest.TestCase):
    """
    Tests the EntireWorkTitle to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = AuthoredWork(1, 'title', 'ES', 'Broadway show',
                              'name1', 1, 'ip_1',
                              'name2', 2, 'ip_2', 'surname1', 'surname2',
                              3)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(1, self.dict['work_id'])
        self.assertEqual('title', self.dict['title'])
        self.assertEqual('ES', self.dict['language_code'])
        self.assertEqual('Broadway show', self.dict['source'])
        self.assertEqual('name1', self.dict['first_name_1'])
        self.assertEqual(1, self.dict['ip_base_1'])
        self.assertEqual('ip_1', self.dict['ip_name_1'])
        self.assertEqual('name2', self.dict['first_name_2'])
        self.assertEqual(2, self.dict['ip_base_2'])
        self.assertEqual('ip_2', self.dict['ip_name_2'])
        self.assertEqual('surname1', self.dict['last_name_1'])
        self.assertEqual('surname2', self.dict['last_name_2'])
        self.assertEqual(3, self.dict['iswc'])


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


class TestPerformingArtist(unittest.TestCase):
    """
    Tests the PerformingArtist to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = PerformingArtist('name', 'surname', 1, 2)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual('name', self.dict['first_name'])
        self.assertEqual('surname', self.dict['last_name'])
        self.assertEqual(1, self.dict['cae_ipi_name'])
        self.assertEqual(2, self.dict['ipi_base_number'])


class TestPublisher(unittest.TestCase):
    """
    Tests the Publisher to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Publisher('publisher1', 1, 'name_ip', 2, 3)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual('publisher1', self.dict['name'])
        self.assertEqual(1, self.dict['ip_id'])
        self.assertEqual('name_ip', self.dict['ip_name'])
        self.assertEqual(2, self.dict['ip_base_id'])
        self.assertEqual(3, self.dict['tax_id'])


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
        self.assertEqual(datetime.date(2015, 1, 11).isoformat(), self.dict['first_release_date'])
        self.assertEqual(1, self.dict['first_release_duration'])
        self.assertEqual('title', self.dict['first_album_title'])
        self.assertEqual('label', self.dict['first_album_label'])
        self.assertEqual(2, self.dict['first_release_catalog_id'])
        self.assertEqual(3, self.dict['ean'])
        self.assertEqual(4, self.dict['isrc'])
        self.assertEqual(5, self.dict['recording_format'])
        self.assertEqual(6, self.dict['recording_technique'])
        self.assertEqual(7, self.dict['media_type'])


class TestSociety(unittest.TestCase):
    """
    Tests the Society to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Society(1, 'name', 'formerly')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual('name', self.dict['name'])
        self.assertEqual('formerly', self.dict['former_name'])


class TestTerritory(unittest.TestCase):
    """
    Tests the Territory to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Territory(1, 2, 3, 'name', 'official')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(1, self.dict['tis'])
        self.assertEqual(2, self.dict['iso2'])
        self.assertEqual(3, self.dict['type'])
        self.assertEqual('name', self.dict['name'])
        self.assertEqual('official', self.dict['official_name'])


class TestValueEntity(unittest.TestCase):
    """
    Tests the ValueEntity to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = ValueEntity(1, 'name', 'desc')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(1, self.dict['id'])
        self.assertEqual('name', self.dict['name'])
        self.assertEqual('desc', self.dict['description'])


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
        self.assertEqual(1, self.dict['intended_purpose'])
        self.assertEqual('title', self.dict['production_title'])
        self.assertEqual(2, self.dict['cd_identifier'])
        self.assertEqual(3, self.dict['cut_number'])
        self.assertEqual(4, self.dict['library'])
        self.assertEqual(5, self.dict['blt'])
        self.assertEqual(6, self.dict['visan_version'])
        self.assertEqual(7, self.dict['visan_isan'])
        self.assertEqual(8, self.dict['visan_episode'])
        self.assertEqual(9, self.dict['visan_check_digit'])
        self.assertEqual(10, self.dict['production_id'])
        self.assertEqual('episode', self.dict['episode_title'])
        self.assertEqual(11, self.dict['episode_id'])
        self.assertEqual(1995, self.dict['production_year'])
        self.assertEqual(12, self.dict['avi_key_society'])
        self.assertEqual(13, self.dict['avi_key_number'])


class TestWriter(unittest.TestCase):
    """
    Tests the Writer to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = Writer('name', 1, 2, 'ip', 3, 'surname')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual('name', self.dict['first_name'])
        self.assertEqual(1, self.dict['personal_number'])
        self.assertEqual(2, self.dict['ip_id'])
        self.assertEqual('ip', self.dict['ip_name'])
        self.assertEqual(3, self.dict['ip_base_id'])
        self.assertEqual('surname', self.dict['last_name'])


if __name__ == '__main__':
    unittest.main()
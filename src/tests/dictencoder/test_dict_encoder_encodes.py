# -*- encoding: utf-8 -*-

import unittest
import datetime

from commonworks.model.agreement import AgreementTerritory, Agreement
from commonworks.model.work import AlternativeWorkTitle, EntireWorkTitle, OriginalWorkTitle, \
    PerformingArtist, WorkOrigin, RecordingDetails, Work
from commonworks.model.interested_party import InterestedParty, IPAAgreement
from commonworks.model.publisher import Publisher
from commonworks.model.society import Society
from commonworks.model.territory import Territory
from commonworks.model.value_entity import ValueEntity
from commonworks.model.writer import Writer
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
        entity = AgreementTerritory(1, 2)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['inclusion_exclusion_indicator'], 1)
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
        entity = AlternativeWorkTitle('title', 1)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['alternative_title'], 'title')
        self.assertEqual(self.dict['alternative_title_type'], 1)


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
        self.assertEqual(self.dict['work_number'], 6)


class TestInterestedParty(unittest.TestCase):
    """
    Tests the InterestedParty to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = InterestedParty(1, 2, 3, 4, 'surname')

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['submitter_id'], 1)
        self.assertEqual(self.dict['cae_ipi_id'], 2)
        self.assertEqual(self.dict['ipi_base_number'], 3)
        self.assertEqual(self.dict['ipa_number'], 4)
        self.assertEqual(self.dict['last_name'], 'surname')


class TestIPAAgreement(unittest.TestCase):
    """
    Tests the IPAAgreement to dictionary encoding.
    """

    def setUp(self):
        encoder = CWRDictionaryEncoder()
        entity = IPAAgreement(1, 2, 3, 4, 5, 6, 7, 8)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['agreement_id'], 1)
        self.assertEqual(self.dict['agreement_role_code'], 2)
        self.assertEqual(self.dict['pr_society'], 3)
        self.assertEqual(self.dict['pr_share'], 4)
        self.assertEqual(self.dict['mr_society'], 5)
        self.assertEqual(self.dict['mr_share'], 6)
        self.assertEqual(self.dict['sr_society'], 7)
        self.assertEqual(self.dict['sr_share'], 8)


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
        self.assertEqual(self.dict['work_number'], 7)


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
        entity = Publisher(1, 2, 3)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['agreement_id'], 2)
        self.assertEqual(self.dict['interested_party'], 3)


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
        entity = Work(1, 'title', 'ES', 3, 4, datetime.date(2015, 1, 11),
                      5, 6, 7, 8, 9, 10, 11, 12, 13, 22, 'name', 14, 15, 16, 17,
                      datetime.date(2015, 2, 11), 18, 19, 20, 21)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['submitter_id'], 1)
        self.assertEqual(self.dict['title'], 'title')
        self.assertEqual(self.dict['language_code'], 'ES')
        self.assertEqual(self.dict['work_number'], 3)
        self.assertEqual(self.dict['iswc'], 4)
        self.assertEqual(self.dict['copyright_date'], datetime.date(2015, 1, 11).isoformat())
        self.assertEqual(self.dict['copyright_number'], 5)
        self.assertEqual(self.dict['musical_distribution_category'], 6)
        self.assertEqual(self.dict['duration'], 7)
        self.assertEqual(self.dict['recorded_indicator'], 8)
        self.assertEqual(self.dict['text_music_relationship'], 9)
        self.assertEqual(self.dict['composite_type'], 10)
        self.assertEqual(self.dict['version_type'], 11)
        self.assertEqual(self.dict['excerpt_type'], 12)
        self.assertEqual(self.dict['music_arrangement'], 13)
        self.assertEqual(self.dict['lyric_adaptation'], 22)
        self.assertEqual(self.dict['contact_name'], 'name')
        self.assertEqual(self.dict['contact_id'], 14)
        self.assertEqual(self.dict['cwr_work_type'], 15)
        self.assertEqual(self.dict['grand_rights_indicator'], 16)
        self.assertEqual(self.dict['composite_component_count'], 17)
        self.assertEqual(self.dict['printed_edition_publication_date'], datetime.date(2015, 2, 11).isoformat())
        self.assertEqual(self.dict['exceptional_clause'], 18)
        self.assertEqual(self.dict['opus_number'], 19)
        self.assertEqual(self.dict['catalogue_number'], 20)
        self.assertEqual(self.dict['priority_flag'], 21)


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
        entity = Writer(1, 2, 'name', 'surname', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

        self.dict = encoder.encode(entity)

    def test_dictionary(self):
        self.assertEqual(self.dict['interested_party'], 2)
        self.assertEqual(self.dict['first_name'], 'name')
        self.assertEqual(self.dict['last_name'], 'surname')
        self.assertEqual(self.dict['designation_code'], 3)
        self.assertEqual(self.dict['tax_id_number'], 4)
        self.assertEqual(self.dict['cae_ipi_name_id'], 5)
        self.assertEqual(self.dict['pr_society'], 6)
        self.assertEqual(self.dict['pr_share'], 7)
        self.assertEqual(self.dict['mr_society'], 8)
        self.assertEqual(self.dict['mr_share'], 9)
        self.assertEqual(self.dict['sr_society'], 10)
        self.assertEqual(self.dict['sr_share'], 11)
        self.assertEqual(self.dict['reversionary_indicator'], 12)
        self.assertEqual(self.dict['first_recording_refusal_indicator'], 13)
        self.assertEqual(self.dict['work_for_hire_indicator'], 14)
        self.assertEqual(self.dict['ipi_base_number'], 15)
        self.assertEqual(self.dict['personal_number'], 16)
        self.assertEqual(self.dict['usa_license_indicator'], 17)


if __name__ == '__main__':
    unittest.main()
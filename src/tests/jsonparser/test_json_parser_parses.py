# -*- encoding: utf-8 -*-
import unittest
import json
import datetime

from commonworks.utils import jsonparser


"""
Unit tests to check if the methods of jsonparser create the model objects correctly.

Only valid cases are tested here. The used JSON objects should have no errors.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreement(unittest.TestCase):
    """
    Tests the JSON to Agreement parsing.
    """

    def setUp(self):
        data = {}
        data['submitter_agreement_number'] = 1
        data['society_agreement_number'] = 2
        data['international_standard_code'] = 3
        data['agreement_type'] = 'Original'

        data['start_date'] = datetime.date(2015, 1, 11).isoformat()
        data['end_date'] = datetime.date(2015, 12, 11).isoformat()

        data['prior_royalty_status'] = 'D'
        data['prior_royalty_start_date'] = datetime.date(2013, 12, 11).isoformat()

        data['post_term_collection_status'] = 'D'
        data['post_term_collection_end_date'] = datetime.date(2014, 1, 20).isoformat()

        data['signature_date'] = datetime.date(2014, 12, 20).isoformat()
        data['retention_end_date'] = datetime.date(2015, 12, 20).isoformat()
        data['works_number'] = 123
        data['sales_manufacture_clause'] = 'S'
        data['shares_change'] = True
        data['advance_given'] = True

        self.agreement = jsonparser.parse_agreement(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.agreement.agreement_id, 1)
        self.assertEqual(self.agreement.society_agreement_number, 2)
        self.assertEqual(self.agreement.international_standard_code, 3)
        self.assertEqual(self.agreement.agreement_type, 'Original')
        self.assertEqual(self.agreement.start_date, datetime.date(2015, 1, 11).isoformat())
        self.assertEqual(self.agreement.end_date, datetime.date(2015, 12, 11).isoformat())
        self.assertEqual(self.agreement.retention_end_date, datetime.date(2015, 12, 20).isoformat())
        self.assertEqual(self.agreement.prior_royalty_status, 'D')
        self.assertEqual(self.agreement.prior_royalty_start_date, datetime.date(2013, 12, 11).isoformat())
        self.assertEqual(self.agreement.post_term_collection_status, 'D')
        self.assertEqual(self.agreement.post_term_collection_end_date, datetime.date(2014, 1, 20).isoformat())
        self.assertEqual(self.agreement.signature_date, datetime.date(2014, 12, 20).isoformat())
        self.assertEqual(self.agreement.works_number, 123)
        self.assertEqual(self.agreement.sales_manufacture_clause, 'S')
        self.assertEqual(self.agreement.shares_change, True)
        self.assertEqual(self.agreement.advance_given, True)


class TestAlternativeWorkTitle(unittest.TestCase):
    """
    Tests the JSON to AlternativeWorkTitle parsing.
    """

    def setUp(self):
        data = {}
        data['alternate_title'] = 'title'
        data['title_type'] = 'type'
        data['language'] = 'ES'

        self.title = jsonparser.parse_alternative_work_title(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.title.alternate_title, 'title')
        self.assertEqual(self.title.title_type, 'type')
        self.assertEqual(self.title.language, 'ES')


class TestAuthoredWork(unittest.TestCase):
    """
    Tests the JSON to AuthoredWork parsing.
    """

    def setUp(self):
        data = {}
        data['work_id'] = 1
        data['title'] = 'Title'
        data['language_code'] = 'ES'
        data['source'] = 'Broadway show'
        data['first_name_1'] = 'first_1'
        data['ip_base_1'] = 1
        data['ip_name_1'] = 'ip_1'
        data['first_name_2'] = 'first_2'
        data['ip_base_2'] = 2
        data['ip_name_2'] = 'ip_2'
        data['last_name_1'] = 'last_1'
        data['last_name_2'] = 'last_2'
        data['iswc'] = 3

        self.title = jsonparser.parse_authored_work(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.title.work_id, 1)
        self.assertEqual(self.title.title, 'Title')
        self.assertEqual(self.title.language_code, 'ES')
        self.assertEqual(self.title.source, 'Broadway show')
        self.assertEqual(self.title.first_name_1, 'first_1')
        self.assertEqual(self.title.ip_base_1, 1)
        self.assertEqual(self.title.ip_name_1, 'ip_1')
        self.assertEqual(self.title.first_name_2, 'first_2')
        self.assertEqual(self.title.ip_base_2, 2)
        self.assertEqual(self.title.ip_name_2, 'ip_2')
        self.assertEqual(self.title.last_name_1, 'last_1')
        self.assertEqual(self.title.last_name_2, 'last_2')
        self.assertEqual(self.title.iswc, 3)


class TestIPA(unittest.TestCase):
    """
    Tests the JSON to IPA parsing.
    """

    def setUp(self):
        data = {}
        data['ip_id'] = 1
        data['ip_last_name'] = 'surname'
        data['agreement_role_code'] = 'assign'
        data['ip_ipi'] = 3
        data['cae_ipi_name'] = 'cae_name'
        data['ip_writer_name'] = 'writer'
        data['mr_share'] = 0.1
        data['pr_share'] = 0.2
        data['sr_share'] = 0.3
        data['mr_society'] = 4
        data['pr_society'] = 5
        data['sr_society'] = 6

        self.agreement = jsonparser.parse_ipa(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(1, self.agreement.ip_id)
        self.assertEqual('surname', self.agreement.last_name)
        self.assertEqual('assign', self.agreement.agreement_role_code)
        self.assertEqual('writer', self.agreement.writer_name)
        self.assertEqual(3, self.agreement.ipi)
        self.assertEqual('cae_name', self.agreement.cae_ipi_name)
        self.assertEqual('writer', self.agreement.writer_name)
        self.assertEqual(0.1, self.agreement.mr_share)
        self.assertEqual(0.2, self.agreement.pr_share)
        self.assertEqual(0.3, self.agreement.sr_share)
        self.assertEqual(4, self.agreement.mr_society)
        self.assertEqual(5, self.agreement.pr_society)
        self.assertEqual(6, self.agreement.sr_society)


class TestPerformingArtist(unittest.TestCase):
    """
    Tests the JSON to PerformingArtist parsing.
    """

    def setUp(self):
        data = {}
        data['first_name'] = 'name'
        data['last_name'] = 'surname'
        data['cae_ipi_name'] = 'ipi'
        data['ipi_base_number'] = 11

        self.artist = jsonparser.parse_performing_artist(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.artist.first_name, 'name')
        self.assertEqual(self.artist.last_name, 'surname')
        self.assertEqual(self.artist.cae_ipi_name, 'ipi')
        self.assertEqual(self.artist.ipi_base_number, 11)


class TestPublisher(unittest.TestCase):
    """
    Tests the JSON to Publisher parsing.
    """

    def setUp(self):
        data = {}
        data['name'] = 'Publisher'
        data['ip_id'] = 1
        data['ip_name'] = 'name_ip'
        data['ip_base_id'] = 2
        data['tax_id'] = 3

        self.publisher = jsonparser.parse_publisher(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.publisher.name, 'Publisher')
        self.assertEqual(self.publisher.ip_id, 1)
        self.assertEqual(self.publisher.ip_name, 'name_ip')
        self.assertEqual(self.publisher.ip_base_id, 2)
        self.assertEqual(self.publisher.tax_id, 3)


class TestRecordingDetails(unittest.TestCase):
    """
    Tests the JSON to RecordingDetails parsing.
    """

    def setUp(self):
        data = {}
        data['first_release_date'] = datetime.date(2014, 1, 20).isoformat()
        data['first_release_duration'] = 120
        data['first_album_title'] = 'title'
        data['first_album_label'] = 'label'
        data['first_release_catalog_id'] = 12345
        data['ean'] = 1122
        data['isrc'] = 3344
        data['recording_format'] = 4455
        data['recording_technique'] = 6677
        data['media_type'] = 8899

        self.details = jsonparser.parse_recording_details(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.details.first_release_date, datetime.date(2014, 1, 20).isoformat())
        self.assertEqual(self.details.first_release_duration, 120)
        self.assertEqual(self.details.first_album_title, 'title')
        self.assertEqual(self.details.first_album_label, 'label')
        self.assertEqual(self.details.first_release_catalog_id, 12345)
        self.assertEqual(self.details.ean, 1122)
        self.assertEqual(self.details.isrc, 3344)
        self.assertEqual(self.details.recording_format, 4455)
        self.assertEqual(self.details.recording_technique, 6677)
        self.assertEqual(self.details.media_type, 8899)


class TestWork(unittest.TestCase):
    """
    Tests the JSON to Work parsing.
    """

    def setUp(self):
        data = {}
        data['work_id'] = 1
        data['title'] = 'The Title'
        data['language_code'] = 'ES'
        data['printed_edition_publication_date'] = datetime.date(2015, 1, 11).isoformat()
        data['copyright_number'] = 2
        data['copyright_date'] = datetime.date(2015, 1, 12).isoformat()
        data['text_music_relationship'] = 'text_only'
        data['version_type'] = 'original'
        data['music_arrangement'] = 'none'
        data['lyric_adaptation'] = 'none'
        data['excerpt_type'] = 'movement'
        data['composite_type'] = 'composite'
        data['composite_component_count'] = 12
        data['iswc'] = 3
        data['cwr_work_type'] = 'jazz'
        data['musical_distribution_category'] = 'category'
        data['duration'] = 60
        data['catalogue_number'] = 4
        data['opus_number'] = '28#3'
        data['contact_id'] = 'name_id'
        data['contact_name'] = 'Person'
        data['recorded_indicator'] = True
        data['priority_flag'] = True
        data['exceptional_clause'] = True
        data['grand_rights_indicator'] = True

        self.work = jsonparser.parse_work(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.work.work_id, 1)
        self.assertEqual(self.work.title, 'The Title')
        self.assertEqual(self.work.language_code, 'ES')
        self.assertEqual(self.work.printed_edition_publication_date, datetime.date(2015, 1, 11).isoformat())
        self.assertEqual(self.work.copyright_number, 2)
        self.assertEqual(self.work.copyright_date, datetime.date(2015, 1, 12).isoformat())
        self.assertEqual(self.work.text_music_relationship, 'text_only')
        self.assertEqual(self.work.version_type, 'original')
        self.assertEqual(self.work.music_arrangement, 'none')
        self.assertEqual(self.work.lyric_adaptation, 'none')
        self.assertEqual(self.work.excerpt_type, 'movement')
        self.assertEqual(self.work.composite_type, 'composite')
        self.assertEqual(self.work.composite_component_count, 12)
        self.assertEqual(self.work.iswc, 3)
        self.assertEqual(self.work.cwr_work_type, 'jazz')
        self.assertEqual(self.work.musical_distribution_category, 'category')
        self.assertEqual(self.work.duration, 60)
        self.assertEqual(self.work.catalogue_number, 4)
        self.assertEqual(self.work.opus_number, '28#3')
        self.assertEqual(self.work.contact_id, 'name_id')
        self.assertEqual(self.work.contact_name, 'Person')
        self.assertEqual(self.work.recorded_indicator, True)
        self.assertEqual(self.work.priority_flag, True)
        self.assertEqual(self.work.exceptional_clause, True)
        self.assertEqual(self.work.grand_rights_indicator, True)


class TestWorkOrigin(unittest.TestCase):
    """
    Tests the JSON to WorkOrigin parsing.
    """

    def setUp(self):
        data = {}
        data['intended_purpose'] = 'purpose'
        data['production_title'] = 'title'
        data['cd_identifier'] = 1234
        data['cut_number'] = 5678
        data['library'] = 11122
        data['blt'] = 3344
        data['visan_version'] = 5566
        data['visan_isan'] = 7788
        data['visan_episode'] = 9900
        data['visan_check_digit'] = 2211
        data['production_id'] = 3322
        data['episode_title'] = 'episode'
        data['episode_id'] = 4433
        data['production_year'] = 1995
        data['avi_key_society'] = 5544
        data['avi_key_number'] = 6655

        self.origin = jsonparser.parse_work_origin(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.origin.intended_purpose, 'purpose')
        self.assertEqual(self.origin.production_title, 'title')
        self.assertEqual(self.origin.cd_identifier, 1234)
        self.assertEqual(self.origin.cut_number, 5678)
        self.assertEqual(self.origin.library, 11122)
        self.assertEqual(self.origin.blt, 3344)
        self.assertEqual(self.origin.visan_version, 5566)
        self.assertEqual(self.origin.visan_isan, 7788)
        self.assertEqual(self.origin.visan_episode, 9900)
        self.assertEqual(self.origin.visan_check_digit, 2211)
        self.assertEqual(self.origin.production_id, 3322)
        self.assertEqual(self.origin.episode_title, 'episode')
        self.assertEqual(self.origin.episode_id, 4433)
        self.assertEqual(self.origin.production_year, 1995)
        self.assertEqual(self.origin.avi_key_society, 5544)
        self.assertEqual(self.origin.avi_key_number, 6655)


if __name__ == '__main__':
    unittest.main()
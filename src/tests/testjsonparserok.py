# -*- encoding: utf-8 -*-
import unittest
import json
import datetime

from commonworks.util import jsonparser


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
        data['submitter_number'] = 12345
        data['international_standard_number'] = 67890
        data['type'] = 't12'
        data['start_date'] = datetime.date(2015, 1, 11).isoformat()
        data['end_date'] = datetime.date(2015, 12, 11).isoformat()
        data['retention_end_date'] = datetime.date(2015, 12, 20).isoformat()
        data['prior_royalty_status'] = 's34'
        data['prior_royalty_status_date'] = datetime.date(2013, 12, 11).isoformat()
        data['post_term_collection_status'] = 's56'
        data['post_term_collection_end_date'] = datetime.date(2014, 1, 20).isoformat()
        data['signature_date'] = datetime.date(2014, 12, 20).isoformat()
        data['works_number'] = 123
        data['sales_manufacture_clause'] = 'c23'
        data['shares_change'] = 56
        data['advance_given'] = 78
        data['society_assigned_number'] = 135

        self.agreement = jsonparser.parse_agreement(189, json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.agreement.submitter_id, 189)
        self.assertEqual(self.agreement.submitter_number, 12345)
        self.assertEqual(self.agreement.international_standard_number, 67890)
        self.assertEqual(self.agreement.type, 't12')
        self.assertEqual(self.agreement.start_date, datetime.date(2015, 1, 11).isoformat())
        self.assertEqual(self.agreement.end_date, datetime.date(2015, 12, 11).isoformat())
        self.assertEqual(self.agreement.retention_end_date, datetime.date(2015, 12, 20).isoformat())
        self.assertEqual(self.agreement.prior_royalty_status, 's34')
        self.assertEqual(self.agreement.prior_royalty_status_date, datetime.date(2013, 12, 11).isoformat())
        self.assertEqual(self.agreement.post_term_collection_status, 's56')
        self.assertEqual(self.agreement.post_term_collection_end_date, datetime.date(2014, 1, 20).isoformat())
        self.assertEqual(self.agreement.signature_date, datetime.date(2014, 12, 20).isoformat())
        self.assertEqual(self.agreement.works_number, 123)
        self.assertEqual(self.agreement.sales_manufacture_clause, 'c23')
        self.assertEqual(self.agreement.shares_change, 56)
        self.assertEqual(self.agreement.advance_given, 78)
        self.assertEqual(self.agreement.society_assigned_number, 135)


class TestAgreementTerritory(unittest.TestCase):
    """
    Tests the JSON to Agreement Territory parsing.
    """

    def setUp(self):
        data = {}
        data['inclusion_exclusion_indicator'] = 12345
        data['tis_numeric_code'] = 6789

        self.territory = jsonparser.parse_agreement_territory(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.territory.inclusion_exclusion_indicator, 12345)
        self.assertEqual(self.territory.tis_numeric_code, 6789)


class TestAlternativeWorkTitle(unittest.TestCase):
    """
    Tests the JSON to AlternativeWorkTitle parsing.
    """

    def setUp(self):
        data = {}
        data['alternate_title'] = 'title'
        data['title_type'] = 'type'

        self.title = jsonparser.parse_alternative_work_title(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.title.alternate_title, 'title')
        self.assertEqual(self.title.title_type, 'type')


class TestEntireWorkTitle(unittest.TestCase):
    """
    Tests the JSON to EntireWorkTitle parsing.
    """

    def setUp(self):
        data = {}
        data['entire_title'] = 'title'
        data['entire_work_iswc'] = 123456
        data['language_code'] = 'ES'
        data['writer_one_last_name'] = 'last_1'
        data['writer_one_first_name'] = 'first_1'
        data['writer_one_ipi_cae'] = 'ipi_cae_1'
        data['writer_one_ipi_base_number'] = 'ipi_base_number_1'
        data['writer_two_last_name'] = 'last_2'
        data['writer_two_first_name'] = 'first_2'
        data['writer_two_ipi_cae'] = 'ipi_cae_2'
        data['writer_two_ipi_base_number'] = 'ipi_base_number_2'
        data['submitter_id'] = 1122

        self.title = jsonparser.parse_entire_work_title(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.title.entire_title, 'title')
        self.assertEqual(self.title.entire_work_iswc, 123456)
        self.assertEqual(self.title.language_code, 'ES')
        self.assertEqual(self.title.writer_one_last_name, 'last_1')
        self.assertEqual(self.title.writer_one_first_name, 'first_1')
        self.assertEqual(self.title.writer_one_ipi_cae, 'ipi_cae_1')
        self.assertEqual(self.title.writer_one_ipi_base_number, 'ipi_base_number_1')
        self.assertEqual(self.title.writer_two_last_name, 'last_2')
        self.assertEqual(self.title.writer_two_first_name, 'first_2')
        self.assertEqual(self.title.writer_two_ipi_cae, 'ipi_cae_2')
        self.assertEqual(self.title.writer_two_ipi_base_number, 'ipi_base_number_2')
        self.assertEqual(self.title.work_number, 1122)


class TestInterestedParty(unittest.TestCase):
    """
    Tests the JSON to InterestedParty parsing.
    """

    def setUp(self):
        data = {}
        data['cae_ipi_id'] = 12345
        data['ipi_base_number'] = 6789
        data['id'] = 'abc'
        data['last_name'] = 'surname'

        self.party = jsonparser.parse_interested_party(189, json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.party.submitter_id, 189)
        self.assertEqual(self.party.cae_ipi_id, 12345)
        self.assertEqual(self.party.ipi_base_number, 6789)
        self.assertEqual(self.party.id, 'abc')
        self.assertEqual(self.party.last_name, 'surname')


class TestIPAAgreement(unittest.TestCase):
    """
    Tests the JSON to IPAAgreement parsing.
    """

    def setUp(self):
        data = {}
        data['agreement_role_code'] = 1234
        data['pr_society'] = 5678
        data['pr_share'] = 905
        data['mr_society'] = 111
        data['mr_share'] = 222
        data['sr_society'] = 333
        data['sr_share'] = 444

        self.agreement = jsonparser.parse_ipa_agreement(189, json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.agreement.agreement_id, 189)
        self.assertEqual(self.agreement.agreement_role_code, 1234)
        self.assertEqual(self.agreement.pr_society, 5678)
        self.assertEqual(self.agreement.pr_share, 905)
        self.assertEqual(self.agreement.mr_society, 111)
        self.assertEqual(self.agreement.mr_share, 222)
        self.assertEqual(self.agreement.sr_society, 333)
        self.assertEqual(self.agreement.sr_share, 444)


class TestOriginalWorkTitle(unittest.TestCase):
    """
    Tests the JSON to OriginalWorkTitle parsing.
    """

    def setUp(self):
        data = {}
        data['entire_title'] = 'title'
        data['entire_work_iswc'] = 12345
        data['language_code'] = 'ES'
        data['writer_one_last_name'] = 'last_1'
        data['writer_one_first_name'] = 'first_1'
        data['writer_one_ipi_cae'] = 'ipi_cae_1'
        data['writer_one_ipi_base_number'] = 'ipi_base_number_1'
        data['writer_two_last_name'] = 'last_2'
        data['writer_two_first_name'] = 'first_2'
        data['writer_two_ipi_cae'] = 'ipi_cae_2'
        data['writer_two_ipi_base_number'] = 'ipi_base_number_2'
        data['submitter_id'] = 1122

        self.title = jsonparser.parse_original_work_title(json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.title.original_title, 'title')
        self.assertEqual(self.title.original_work_iswc, 12345)
        self.assertEqual(self.title.language_code, 'ES')
        self.assertEqual(self.title.writer_one_last_name, 'last_1')
        self.assertEqual(self.title.writer_one_first_name, 'first_1')
        self.assertEqual(self.title.writer_one_ipi_cae, 'ipi_cae_1')
        self.assertEqual(self.title.writer_one_ipi_base_number, 'ipi_base_number_1')
        self.assertEqual(self.title.writer_two_last_name, 'last_2')
        self.assertEqual(self.title.writer_two_first_name, 'first_2')
        self.assertEqual(self.title.writer_two_ipi_cae, 'ipi_cae_2')
        self.assertEqual(self.title.writer_two_ipi_base_number, 'ipi_base_number_2')


class TestPublisher(unittest.TestCase):
    """
    Tests the JSON to IPAAgreement parsing.
    """

    def setUp(self):
        data = {}
        data['agreement_number'] = 1234
        data['interested_party_id'] = 5678

        self.publisher = jsonparser.parse_publisher(189, json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.publisher.submitter_id, 189)
        self.assertEqual(self.publisher.agreement_number, 1234)
        self.assertEqual(self.publisher.interested_party_id, 5678)


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
        data['title'] = 'The Title'
        data['language_code'] = 'ES'
        data['submitter_id'] = 189
        data['iswc'] = 12345
        data['copyright_date'] = datetime.date(2015, 1, 11).isoformat()
        data['copyright_number'] = 6789
        data['musical_distribution_category'] = 'c123'
        data['duration'] = 120
        data['recorded_indicator'] = 111
        data['text_music_relationship'] = 222
        data['composite_type'] = 333
        data['version_type'] = 444
        data['excerpt_type'] = 555
        data['music_arrangement'] = 666
        data['lyric_adaptation'] = 777
        data['contact_name'] = 'name'
        data['contact_id'] = 888
        data['cwr_work_type'] = 999
        data['grand_rights_indicator'] = 000
        data['composite_component_count'] = 1122
        data['printed_edition_publication_date'] = datetime.date(2012, 1, 11).isoformat()
        data['exceptional_clause'] = 'c333'
        data['opus_number'] = 3344
        data['catalogue_number'] = 5566
        data['priority_flag'] = 7788

        self.work = jsonparser.parse_work(189, json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.work.submitter_id, 189)
        self.assertEqual(self.work.title, 'The Title')
        self.assertEqual(self.work.language_code, 'ES')
        self.assertEqual(self.work.submitter_id, 189)
        self.assertEqual(self.work.iswc, 12345)
        self.assertEqual(self.work.copyright_date, datetime.date(2015, 1, 11).isoformat())
        self.assertEqual(self.work.copyright_number, 6789)
        self.assertEqual(self.work.musical_distribution_category, 'c123')
        self.assertEqual(self.work.duration, 120)
        self.assertEqual(self.work.recorded_indicator, 111)
        self.assertEqual(self.work.text_music_relationship, 222)
        self.assertEqual(self.work.composite_type, 333)
        self.assertEqual(self.work.version_type, 444)
        self.assertEqual(self.work.excerpt_type, 555)
        self.assertEqual(self.work.music_arrangement, 666)
        self.assertEqual(self.work.lyric_adaptation, 777)
        self.assertEqual(self.work.contact_name, 'name')
        self.assertEqual(self.work.contact_id, 888)
        self.assertEqual(self.work.cwr_work_type, 999)
        self.assertEqual(self.work.grand_rights_indicator, 000)
        self.assertEqual(self.work.composite_component_count, 1122)
        self.assertEqual(self.work.printed_edition_publication_date, datetime.date(2012, 1, 11).isoformat())
        self.assertEqual(self.work.exceptional_clause, 'c333')
        self.assertEqual(self.work.opus_number, 3344)
        self.assertEqual(self.work.catalogue_number, 5566)
        self.assertEqual(self.work.priority_flag, 7788)


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


class TestWriter(unittest.TestCase):
    """
    Tests the JSON to Writer parsing.
    """

    def setUp(self):
        data = {}
        data['interested_party_id'] = 1234
        data['first_name'] = 'first'
        data['last_name'] = 'last'
        data['designation_code'] = 5678
        data['tax_id_number'] = 1122
        data['cae_ipi_name_id'] = 3344
        data['pr_society'] = 5566
        data['pr_share'] = 7788
        data['mr_society'] = 9900
        data['mr_share'] = 12
        data['sr_society'] = 23
        data['sr_share'] = 34
        data['reversionary_indicator'] = 56
        data['first_recording_refusal_indicator'] = 78
        data['work_for_hire_indicator'] = 90
        data['ipi_base_number'] = 9988
        data['personal_number'] = 8877
        data['usa_license_indicator'] = 7766

        self.writer = jsonparser.parse_writer(189, json.loads(json.dumps(data)))

    def test_data(self):
        # Makes sure the data was parsed correctly
        self.assertEqual(self.writer.submitter_id, 189)
        self.assertEqual(self.writer.interested_party_id, 1234)
        self.assertEqual(self.writer.first_name, 'first')
        self.assertEqual(self.writer.last_name, 'last')
        self.assertEqual(self.writer.designation_code, 5678)
        self.assertEqual(self.writer.tax_id_number, 1122)
        self.assertEqual(self.writer.cae_ipi_name_id, 3344)
        self.assertEqual(self.writer.pr_society, 5566)
        self.assertEqual(self.writer.pr_share, 7788)
        self.assertEqual(self.writer.mr_society, 9900)
        self.assertEqual(self.writer.mr_share, 12)
        self.assertEqual(self.writer.sr_society, 23)
        self.assertEqual(self.writer.sr_share, 34)
        self.assertEqual(self.writer.reversionary_indicator, 56)
        self.assertEqual(self.writer.first_recording_refusal_indicator, 78)
        self.assertEqual(self.writer.work_for_hire_indicator, 90)
        self.assertEqual(self.writer.ipi_base_number, 9988)
        self.assertEqual(self.writer.personal_number, 8877)
        self.assertEqual(self.writer.usa_license_indicator, 7766)


if __name__ == '__main__':
    unittest.main()
# -*- encoding: utf-8 -*-
import unittest
import datetime

from commonworks.agreement import AgreementTerritory, Agreement, IPA
from commonworks.interested_party import Publisher
from commonworks.society import Society
from commonworks.territory import Territory
from commonworks.value_entity import ValueEntity
from commonworks.work import AlternateTitle, AuthoredWork, \
    PerformingArtist, WorkOrigin, Work, RecordingDetails
from tests.mongo.mongo_test_conf import host, port, db_name, MongoGenericRepository


"""
Integration tests to check that it is possible to store the model classes in a Mongo database.

Requires a Mongo database running, and set up as mongo_test_conf indicates.

Right now these are just placeholders to create real tests.
"""

__author__ = 'Borja Garrido Bear,Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreement(unittest.TestCase):
    """
    Tests the Agreement API against a Mongo database.
    """

    def setUp(self):
        self.entity = Agreement(1, 'Original', datetime.date(2015, 1, 11), 'D', 'D', datetime.date(2015, 6, 11),
                                122, society_agreement_number=2, international_standard_code=3,
                                sales_manufacture_clause='S',
                                end_date=datetime.date(2015, 2, 11),
                                retention_end_date=datetime.date(2015, 3, 11),
                                prior_royalty_status_date=datetime.date(2015, 4, 11),
                                post_term_collection_end_date=datetime.date(2015, 5, 11),
                                shares_change=True, advance_given=True)
        self.repo = MongoGenericRepository(host, port, db_name, 'agreements')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestAgreementTerritory(unittest.TestCase):
    """
    Tests the AgreementTerritory API against a Mongo database.
    """

    def setUp(self):
        self.entity = AgreementTerritory(1, 2)
        self.repo = MongoGenericRepository(host, port, db_name, 'agreement_territories')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestAlternativeWorkTitle(unittest.TestCase):
    """
    Tests the AlternativeWorkTitle API against a Mongo database.
    """

    def setUp(self):
        self.entity = AlternateTitle('title', 1, 'ES')
        self.repo = MongoGenericRepository(host, port, db_name, 'alternate_titles')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestAuthoredWork(unittest.TestCase):
    """
    Tests the EntireWorkTitle API against a Mongo database.
    """

    def setUp(self):
        self.entity = AuthoredWork(1, 'title', 'ES', 'Broadway show',
                                   'name1', 1, 'ip_1',
                                   'name2', 2, 'ip_2', 'surname1', 'surname2',
                                   3)
        self.repo = MongoGenericRepository(host, port, db_name, 'authored_works')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestIPA(unittest.TestCase):
    """
    Tests the IPA API against a Mongo database.
    """

    def setUp(self):
        self.entity = IPA(2, 'party', 'assign', 'writer', 3, 'cae_name', 4, 0.1, 5, 0.2, 6, 0.3)
        self.repo = MongoGenericRepository(host, port, db_name, 'ipas')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestPerformingArtist(unittest.TestCase):
    """
    Tests the PerformingArtist API against a Mongo database.
    """

    def setUp(self):
        self.entity = PerformingArtist('name', 'surname', 1, 2)
        self.repo = MongoGenericRepository(host, port, db_name, 'performing_artists')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestPublisher(unittest.TestCase):
    """
    Tests the Publisher API against a Mongo database.
    """

    def setUp(self):
        self.entity = Publisher('publisher1', 1, 'name_ip', 2, 3)
        self.repo = MongoGenericRepository(host, port, db_name, 'publishers')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestRecordingDetails(unittest.TestCase):
    """
    Tests the RecordingDetails API against a Mongo database.
    """

    def setUp(self):
        self.entity = RecordingDetails(datetime.date(2015, 1, 11), 1, 'title', 'label', 2,
                                       3, 4, 5, 6, 7)
        self.repo = MongoGenericRepository(host, port, db_name, 'recording_details')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestSociety(unittest.TestCase):
    """
    Tests the Society API against a Mongo database.
    """

    def setUp(self):
        self.entity = Society(1, 'name', 'formerly')
        self.repo = MongoGenericRepository(host, port, db_name, 'societies')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestTerritory(unittest.TestCase):
    """
    Tests the Territory API against a Mongo database.
    """

    def setUp(self):
        self.entity = Territory(1, 2, 3, 'name', 'official')
        self.repo = MongoGenericRepository(host, port, db_name, 'territories')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestValueEntity(unittest.TestCase):
    """
    Tests the ValueEntity API against a Mongo database.
    """

    def setUp(self):
        self.entity = ValueEntity(1, 'name', 'desc')
        self.repo = MongoGenericRepository(host, port, db_name, 'value_entities')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestWork(unittest.TestCase):
    """
    Tests the Work API against a Mongo database.
    """

    def setUp(self):
        self.entity = Work(1, 'The Title', 'original', 'category',
                           language_code='ES', printed_edition_publication_date=datetime.date(2015, 1, 11),
                           copyright_number=2, copyright_date=datetime.date(2015, 1, 12),
                           text_music_relationship='text_only',
                           music_arrangement='none', lyric_adaptation='none', excerpt_type='movement',
                           composite_type='composite', composite_component_count=3,
                           iswc=4, cwr_work_type='jazz',
                           duration=60, catalogue_number=5, opus_number='28#3',
                           contact_id='name_id', contact_name='Person',
                           recorded_indicator=True, priority_flag=True, exceptional_clause=True,
                           grand_rights_indicator=True)
        self.repo = MongoGenericRepository(host, port, db_name, 'works')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestWorkOrigin(unittest.TestCase):
    """
    Tests the WorkOrigin API against a Mongo database.
    """

    def setUp(self):
        self.entity = WorkOrigin(1, 'title', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'episode', 11, 1995, 12, 13)
        self.repo = MongoGenericRepository(host, port, db_name, 'work_origins')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


if __name__ == '__main__':
    unittest.main()
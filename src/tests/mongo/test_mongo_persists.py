# -*- encoding: utf-8 -*-
import unittest
import datetime

from commonworks.model.agreement import AgreementTerritory, Agreement
from commonworks.model.work import AlternativeWorkTitle, EntireWorkTitle, OriginalWorkTitle, \
    PerformingArtist, WorkOrigin, Work
from commonworks.model.interested_party import InterestedParty, IPAAgreement
from commonworks.model.publisher import Publisher
from commonworks.model.society import Society
from commonworks.model.territory import Territory
from commonworks.model.value_entity import ValueEntity
from commonworks.model.writer import Writer
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
        self.entity = Agreement(1, 2, 'Original', datetime.date(2015, 1, 11), datetime.date(2015, 2, 11),
                                'D', 'D', datetime.date(2015, 6, 11), 122, 'S',
                                international_standard_code=3, retention_end_date=datetime.date(2015, 3, 11),
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
        self.entity = AlternativeWorkTitle('title', 2)
        self.repo = MongoGenericRepository(host, port, db_name, 'alternative_work_titles')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestEntireWorkTitle(unittest.TestCase):
    """
    Tests the EntireWorkTitle API against a Mongo database.
    """

    def setUp(self):
        self.entity = EntireWorkTitle('title', 1, 'ES',
                                      'name1', 'surname1', 2, 3,
                                      'name2', 'surname2', 4, 5,
                                      6)
        self.repo = MongoGenericRepository(host, port, db_name, 'entire_work_titles')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestInterestedParty(unittest.TestCase):
    """
    Tests the InterestedParty API against a Mongo database.
    """

    def setUp(self):
        self.entity = InterestedParty(1, 2, 3, 4, 'surname')
        self.repo = MongoGenericRepository(host, port, db_name, 'interested_parties')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestIPAAgreement(unittest.TestCase):
    """
    Tests the IPAAgreement API against a Mongo database.
    """

    def setUp(self):
        self.entity = IPAAgreement(1, 2, 3, 4, 5, 6, 7, 8)
        self.repo = MongoGenericRepository(host, port, db_name, 'ipa_agreements')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


class TestOriginalWorkTitle(unittest.TestCase):
    """
    Tests the OriginalWorkTitle API against a Mongo database.
    """

    def setUp(self):
        self.entity = OriginalWorkTitle('title', 2, 'ES',
                                        'name1', 'surname1', 3, 4,
                                        'name2', 'surname2', 5, 6, 7)
        self.repo = MongoGenericRepository(host, port, db_name, 'original_work_titles')

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
        self.entity = Publisher(1, 2, 3)
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
        self.entity = Publisher(1, 2, 3)
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
        self.entity = Work(1, 'title', 'ES', 3, 4, datetime.date(2015, 1, 11),
                           5, 6, 7, 8, 9, 10, 11, 12, 13, 22, 'name', 14, 15, 16, 17,
                           datetime.date(2015, 2, 11), 18, 19, 20, 21)
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


class TestWriter(unittest.TestCase):
    """
    Tests the Writer API against a Mongo database.
    """

    def setUp(self):
        self.entity = Writer(1, 2, 'name', 'surname', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
        self.repo = MongoGenericRepository(host, port, db_name, 'writers')

    def tearDown(self):
        self.repo.clear()

    def test_add(self):
        self.assertEqual(len(self.repo.get(lambda e: True)), 0)
        self.repo.add(self.entity)
        self.assertEqual(len(self.repo.get(lambda e: True)), 1)


if __name__ == '__main__':
    unittest.main()
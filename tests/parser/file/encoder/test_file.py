# -*- coding: utf-8 -*-
import codecs
import os

import unittest
import datetime
import json
import sys
from cwr.parser.decoder.file import default_file_decoder

from cwr.parser.encoder.file import CwrFileEncoder, default_file_encoder
from cwr.file import FileTag, CWRFile
from cwr.group import GroupHeader, GroupTrailer, Group
from cwr.work import WorkRecord
from cwr.agreement import AgreementRecord
from cwr.transmission import TransmissionTrailer, TransmissionHeader, \
    Transmission

"""
Group from cwr encoding tests.

The following cases are tested:
"""

__author__ = 'Yaroslav O. Holub'
__license__ = 'MIT'
__status__ = 'Development'


class TestCwrEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = default_file_encoder()
        self._decoder = default_file_decoder()

    def get_data(self):
        current_dir = os.path.dirname(__file__)
        example_path = os.path.join(current_dir, '..', '..', '..', 'examples', 'ackexample.V21')
        data = {}
        data['filename'] = os.path.basename(example_path)
        data['contents'] = codecs.open(example_path, 'r', 'latin-1').read()
        return data

    def test_file_encoding(self):
        decoder = default_file_decoder()
        data = self.get_data()

        original_lines = data['contents'].splitlines()
        for i in range(len(original_lines)):
            print(original_lines[i])

        entities = decoder.decode(data)
        file_encoder = default_file_encoder()
        result = file_encoder.encode(entities.transmission)
        original_lines = data['contents'].split("\n")
        encoded_lines = result.split("\n")

        self.assertEqual(len(original_lines), len(encoded_lines))
        for i in range(1, len(original_lines)):
            self.assertEquals(original_lines[i].strip(), encoded_lines[i].strip())






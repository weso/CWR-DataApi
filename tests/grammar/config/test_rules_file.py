# -*- coding: utf-8 -*-

import unittest

from cwr.grammar.factory.config import rule_config_file

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestConfigTerminalRule(unittest.TestCase):
    def setUp(self):
        self._rule = rule_config_file

    def test_common(self):
        rule_data = 'filename:' + '\n' + \
                    '    id: filename_old' + '\n' + \
                    '    rules:' + '\n' + \
                    '      [' + '\n' + \
                    '      sequence' + '\n' + \
                    '        [' + '\n' + \
                    '        field: header (compulsory)' + '\n' + \
                    '        field: year (compulsory)' + '\n' + \
                    '        field: sequence_n_old (compulsory)' + '\n' + \
                    '        field: sender (compulsory)' + '\n' + \
                    '        field: delimiter_ip (compulsory)' + '\n' + \
                    '        field: receiver (compulsory)' + '\n' + \
                    '        ]' + '\n' + \
                    '      option' + '\n' + \
                    '        [' + '\n' + \
                    '        sequence' + '\n' + \
                    '          [' + '\n' + \
                    '          field: delimiter_version (compulsory)' + '\n' + \
                    '          field: version (compulsory)' + '\n' + \
                    '          ]' + '\n' + \
                    '        sequence' + '\n' + \
                    '          [' + '\n' + \
                    '          field: delimiter_zip (compulsory)' + '\n' + \
                    '          ]' + '\n' + \
                    '        ]' + '\n' + \
                    '      ]'

        rule_data = rule_data + '\n' + rule_data

        result = self._rule.parseString(rule_data)

        self.assertEqual(2, len(result))

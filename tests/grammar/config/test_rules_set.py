# -*- coding: utf-8 -*-

import unittest

from cwr.grammar.factory.config import rule_config_set

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestConfigTerminalRule(unittest.TestCase):
    def setUp(self):
        self._rule = rule_config_set

    def test_empty(self):
        line = 'filename:' + '\n' + \
               '    id: filename_old' + '\n' + \
               '    rules:' + '\n' + \
               '      [' + '\n' + \
               '      ]'

        result = self._rule.parseString(line)

        self.assertEqual('filename', result.rule_type)
        self.assertEqual('filename_old', result.id)

        self.assertEqual(0, len(result.rules))

    def test_small(self):
        line = 'filename:' + '\n' + \
               '    id: filename_old' + '\n' + \
               '    rules:' + '\n' + \
               '      [' + '\n' + \
               '      sequence' + '\n' + \
               '        [' + '\n' + \
               '        field: header (compulsory)' + '\n' + \
               '        ]' + '\n' + \
               '      ]'

        result = self._rule.parseString(line)

        self.assertEqual('filename', result.rule_type)
        self.assertEqual('filename_old', result.id)

        self.assertEqual(1, len(result.rules))

    def test_full(self):
        line = 'filename:' + '\n' + \
               '    id: filename_old' + '\n' + \
               '    head: ABC' + '\n' + \
               '    results_name: name' + '\n' + \
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

        result = self._rule.parseString(line)

        self.assertEqual('filename', result.rule_type)
        self.assertEqual('filename_old', result.id)
        self.assertEqual('ABC', result.head)
        self.assertEqual('name', result.results_name)

        self.assertEqual(2, len(result.rules))

        self.assertEqual(6, len(result.rules[0].rules))
        self.assertEqual(2, len(result.rules[1].rules))
        self.assertEqual(2, len(result.rules[1].rules[0].rules))
        self.assertEqual(1, len(result.rules[1].rules[1].rules))

    def test_varied(self):
        line = 'group:' + '\n' + \
               '    id: group_info' + '\n' + \
               '    rules:' + '\n' + \
               '      [' + '\n' + \
               '      sequence' + '\n' + \
               '        [' + '\n' + \
               '        record: group_header' + '\n' + \
               '        group: transactions (optional)' + '\n' + \
               '        option' + '\n' + \
               '		  [' + '\n' + \
               '          record: group_trailer_base' + '\n' + \
               '          record: group_trailer_short' + '\n' + \
               '		  ]' + '\n' + \
               '		]' + '\n' + \
               '	  ]'

        result = self._rule.parseString(line)

        self.assertEqual('group', result.rule_type)
        self.assertEqual('group_info', result.id)

        self.assertEqual(1, len(result.rules))
        rules = result.rules[0]

        self.assertEqual('sequence', rules.list_type)
        self.assertEqual(3, len(rules.rules))

        rules = rules.rules[2]
        self.assertEqual(2, len(rules.rules))

    def test_terminals(self):
        line = 'group:' + '\n' + \
               '    id: group_info' + '\n' + \
               '    rules:' + '\n' + \
               '      [' + '\n' + \
               '      record: group_header' + '\n' + \
               '      record: group_header' + '\n' + \
               '      record: group_header' + '\n' + \
               '	  ]'

        result = self._rule.parseString(line)

        self.assertEqual('group', result.rule_type)
        self.assertEqual('group_info', result.id)

        self.assertEqual(3, len(result.rules))

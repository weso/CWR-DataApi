# -*- coding: utf-8 -*-

import unittest

from cwr.grammar.factory.config import rule_rules_tree


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestConfigTerminalRule(unittest.TestCase):
    def setUp(self):
        self._rule = rule_rules_tree

    def test_empty(self):
        line = 'option:' + '\n' + \
               '[' + '\n' + \
               ']'

        result = self._rule.parseString(line)

        self.assertEqual('option', result.list_type)

        self.assertEqual(0, len(result.rules))

    def test_one(self):
        line = 'option:' + '\n' + \
               '[' + '\n' + \
               'sequence:' + '\n' + \
               '[' + '\n' + \
               '  field: delimiter_zip (compulsory)' + '\n' + \
               ']' + '\n' + \
               ']'

        result = self._rule.parseString(line)

        self.assertEqual('option', result.list_type)

        self.assertEqual(1, len(result.rules))

    def test_common(self):
        line = 'option:' + '\n' + \
               '[' + '\n' + \
               'sequence:' + '\n' + \
               '[' + '\n' + \
               '  field: delimiter_version (compulsory)' + '\n' + \
               '  field: version (compulsory)' + '\n' + \
               ']' + '\n' + \
               'sequence:' + '\n' + \
               '[' + '\n' + \
               '  field: delimiter_zip (compulsory)' + '\n' + \
               ']' + '\n' + \
               ']'

        result = self._rule.parseString(line)

        self.assertEqual('option', result.list_type)

        self.assertEqual(2, len(result.rules))

    def test_mixed(self):
        line = 'option:' + '\n' + \
               '[' + '\n' + \
               'sequence:' + '\n' + \
               '[' + '\n' + \
               '  field: delimiter_zip (compulsory)' + '\n' + \
               ']' + '\n' + \
               'field: delimiter_zip (compulsory)' + '\n' + \
               ']'

        result = self._rule.parseString(line)

        self.assertEqual('option', result.list_type)

        self.assertEqual(2, len(result.rules))

    def test_nested(self):
        line = 'option:' + '\n' + \
               '[' + '\n' + \
               'option:' + '\n' + \
               '  [' + '\n' + \
               '  sequence:' + '\n' + \
               '    [' + '\n' + \
               '    field: delimiter_zip (compulsory)' + '\n' + \
               '    ]' + '\n' + \
               '  sequence:' + '\n' + \
               '    [' + '\n' + \
               '    field: delimiter_zip' + '\n' + \
               '    ]' + '\n' + \
               '  ]' + '\n' + \
               ']'

        result = self._rule.parseString(line)

        self.assertEqual('option', result.list_type)

        rules = result.rules
        self.assertEqual(1, len(rules))

        self.assertEqual(2, len(rules[0].rules))

    def test_nested_mixed(self):
        line = '      sequence:' + '\n' + \
               '        [' + '\n' + \
               '        record: group_header' + '\n' + \
               '        group: transactions (optional)' + '\n' + \
               '        option:' + '\n' + \
               '		  [' + '\n' + \
               '          record: group_trailer_base' + '\n' + \
               '          record: group_trailer_short' + '\n' + \
               '		  ]' + '\n' + \
               '		]'

        result = self._rule.parseString(line)

        self.assertEqual('sequence', result.list_type)

        rules = result.rules
        self.assertEqual(3, len(rules))

        self.assertEqual(2, len(rules[2].rules))

    def test_complex(self):
        line = 'option:' + '\n' + \
               '[' + '\n' + \
               'sequence:' + '\n' + \
               '  [' + '\n' + \
               '  field: delimiter_version (compulsory)' + '\n' + \
               '  field: version (compulsory)' + '\n' + \
               '  ]' + '\n' + \
               'option:' + '\n' + \
               '  [' + '\n' + \
               '  sequence:' + '\n' + \
               '    [' + '\n' + \
               '    field: delimiter_zip (compulsory)' + '\n' + \
               '    ]' + '\n' + \
               '  sequence:' + '\n' + \
               '    [' + '\n' + \
               '    field: delimiter_zip' + '\n' + \
               '    ]' + '\n' + \
               '  ]' + '\n' + \
               ']'

        result = self._rule.parseString(line)

        self.assertEqual('option', result.list_type)

        rules = result.rules
        self.assertEqual(2, len(rules))

        rules_b = rules[0].rules
        self.assertEqual(2, len(rules_b))

        rules_b = rules[1].rules
        self.assertEqual(2, len(rules_b))

        rules_c = rules_b[0].rules
        self.assertEqual(1, len(rules_c))

        rules_c = rules_b[1].rules
        self.assertEqual(1, len(rules_c))
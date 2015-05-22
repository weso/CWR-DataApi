# -*- coding: utf-8 -*-

from cwr.parser.decoder.file import default_grammar_factory, default_filename_grammar_factory

"""
Grammar utilities for the test classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

_group_rule_factory = default_grammar_factory()

_group_rule_factory_filename = default_filename_grammar_factory()


def get_record_grammar(id):
    return _group_rule_factory.get_rule(id)


def get_filename_grammar(id):
    return _group_rule_factory_filename.get_rule(id)
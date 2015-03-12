# -*- coding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import nra as rules_nr
from cwr.grammar.record import work_detail as rules_work_detail


"""
CWR work detail grammar.

This contains rules for work details.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Instrumentation
instrumentation_information = rules_work_detail.inst_summary + pp.Optional(pp.OneOrMore(rules_work_detail.inst_detail))

# Excerpts
information_for_excerpts = rules_work_detail.entire_title + pp.Optional(rules_nr.nra_work) + pp.Optional(
    pp.OneOrMore(rules_nr.now))

# Versions
information_for_versions = rules_work_detail.version + pp.Optional(rules_nr.nra_work) + pp.Optional(
    pp.OneOrMore(rules_nr.now))

# Components
information_for_components = rules_work_detail.component + pp.Optional(rules_nr.nra_work) + pp.Optional(
    pp.OneOrMore(rules_nr.now))

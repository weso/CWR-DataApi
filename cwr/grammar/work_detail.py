# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import nra, work_detail


"""
CWR work detail grammar.

This contains rules for work details.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Instrumentation
instrumentation_information = work_detail.inst_summary + pp.Optional(pp.OneOrMore(work_detail.inst_detail))

# Excerpts
information_for_excerpts = work_detail.entire_work_title + pp.Optional(nra.nra_work) + pp.Optional(
    pp.OneOrMore(nra.now))

# Versions
information_for_versions = work_detail.original_title + pp.Optional(nra.nra_work) + pp.Optional(
    pp.OneOrMore(nra.now))

# Components
information_for_components = work_detail.component + pp.Optional(nra.nra_work) + pp.Optional(
    pp.OneOrMore(nra.now))

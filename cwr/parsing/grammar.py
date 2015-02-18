# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data import __data__ as data


"""
Grammar for CWR files.

This is used along with pyparsing to create a BNF grammar.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# FILE NAME

# Fields
filename_year = pp.Word(pp.nums, exact=2).setResultsName("year")
filename_sequence_old = pp.Word(pp.nums, exact=2).setResultsName("sequence_n")
filename_sequence_new = pp.Word(pp.nums, exact=4).setResultsName("sequence_n")
filename_sender = pp.Word(pp.alphanums, min=2, max=3).setResultsName("sender")
filename_receiver = pp.Word(pp.alphanums, min=2, max=3).setResultsName("receiver")
filename_version_num = pp.Word(pp.nums, exact=2).setResultsName("version")

# Delimiters
filename_header = pp.CaselessLiteral('CW').suppress()
filename_delimiter_ip = pp.Literal('_').suppress()
filename_delimiter_version = pp.CaselessLiteral('.V').suppress()
filename_delimiter_zip = pp.CaselessLiteral('.zip').setResultsName("version")

# FILE CONTENTS

# Fields
record_type = pp.oneOf(data.record_types()).setResultsName("record_type")
transaction_n = pp.Word(pp.nums, exact=8).setResultsName("transaction_sequence_n")
sequence_n = pp.Word(pp.nums, exact=8).setResultsName("record_sequence_n")

# Patterns
record_prefix = record_type + transaction_n + sequence_n
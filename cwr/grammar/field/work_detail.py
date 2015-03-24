# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special


"""
CWR Work detail records fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Author fields
"""

# Writer 1 IPI Name #
writer_1_ipi_name_n = special.ipi_name_number()
writer_1_ipi_name_n = writer_1_ipi_name_n.setName('Writer 1 IPI Name #').setResultsName('writer_1_ipi_name_n')

# Writer 1 IPI Base #
writer_1_ipi_base_n = special.ipi_base_number()
writer_1_ipi_base_n = writer_1_ipi_base_n.setName('Writer 1 IPI Base #').setResultsName('writer_1_ipi_base_n')

# Writer 2 IPI Name #
writer_2_ipi_name_n = special.ipi_name_number()
writer_2_ipi_name_n = writer_2_ipi_name_n.setName('Writer 1 IPI Name #').setResultsName('writer_2_ipi_name_n')

# Writer 2 IPI Base #
writer_2_ipi_base_n = special.ipi_base_number()
writer_2_ipi_base_n = writer_2_ipi_base_n.setName('Writer 1 IPI Base #').setResultsName('writer_2_ipi_base_n')

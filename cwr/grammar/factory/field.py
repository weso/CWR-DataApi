# -*- coding: utf-8 -*-

from cwr.grammar.field import basic

from data.accessor import CWRConfiguration, CWRTables

"""
Grammar fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()


class LookupFieldFactory():
    # Singleton control object
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self._fields = {}

    def get_field(self, id):
        if id in self._fields:
            field = self._fields[id]
        else:
            field = self.__create_field(id)
            self._fields[id] = field

        return field

    def __create_field(self, id):
        config = _config.lookup_field_data(id)

        values_method = getattr(_tables, config['values'])

        field = basic.lookup(values_method(),
            columns=config['size'],
            compulsory=config['compulsory'],
            name=config['name'])

        if 'results_name' in config:
            results_name = config['results_name']
        else:
            results_name = id

        return field.setResultsName(results_name)
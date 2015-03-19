# -*- coding: utf-8 -*-

import pyparsing as pp

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
        self._fields_optional = {}

    def get_field(self, id, compulsory=False):
        """
        Returns the field identified by the id.

        This field is unique, it will be created just once and reused for all the following calls of the method.

        If it is set as not being compulsory, a special wrapping rule, allowing an empty string, will be added to
        the field.

        :param id: unique id in the system for the field
        :param compulsory: indicates if the empty string is rejected or not
        :return: a lookup field
        """
        config = _config.lookup_field_data(id)

        if id in self._fields:
            # Field already exists
            field = self._fields[id]
        else:
            # Field does not exist
            # It is created
            if 'values' in config:
                values_id = config['values']
            else:
                values_id = None

            values = self.__get_field_values(id, values_id)
            field = self.__create_field(id, name=config['name'], values=values)

            # Actions are added
            if 'actions' in config:
                self.__add_actions(field, config['actions'])

            # Field is saved
            self._fields[id] = field

        if not compulsory:
            if id in self._fields_optional:
                # Wrapped field already exists
                field = self._fields_optional[id]
            else:
                # It is not compulsory, the wrapped is added
                field = self.__not_compulsory_wrapper(field, config['name'], config['size'])

                # Wrapped field is saved
                self._fields_optional[id] = field

        return field

    def __get_field_values(self, id, values_id=None):
        """
        Returns the allowed values for the lookup field.

        :param id: id for the field
        :param values_id: id for the values
        :return: the list of values allowed to the field
        """
        if values_id is None:
            table = id
        else:
            table = values_id

        values_method = getattr(_tables, table)

        return values_method()

    def __create_field(self, id, name, values, results_name=None):
        """
        Creates a lookup field with the specified information.

        :param id: field id
        :param name: human readable name for the field
        :param values: allowed values
        :param results_name: results name for the field
        :return:the field correctly set up
        """

        field = basic.lookup(values, name=name, compulsory=True)

        if results_name is None:
            results_name = id

        return field.setResultsName(results_name)

    def __not_compulsory_wrapper(self, field, name, columns):
        """
        Adds a wrapper rule to the field to accept empty strings.

        This empty string should be of the same size as the columns parameter. One smaller or bigger will be rejected.

        This wrapper will return None if the field is empty.

        :param field: the field to wrap
        :param name: name of the field
        :param columns: number of columns it takes
        :return: the field with an additional rule to allow empty strings
        """
        field_option = pp.Regex('[ ]{' + str(columns) + '}')

        field_option.setName(name)

        field_option.leaveWhitespace()

        field_option.setParseAction(pp.replaceWith(None))

        field_option = field_option.setResultsName(field.resultsName)

        field = field | field_option

        field.setName(name)

        field.leaveWhitespace()

        return field

    def __add_actions(self, field, actions):
        for action in actions:
            action_method = getattr(self, action)

            field.setParseAction(lambda p: action_method(p))


    def to_int(self, parsed):
        value = parsed[0]

        if value is None:
            return None
        else:
            return int(parsed[0])
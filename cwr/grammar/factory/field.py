# -*- coding: utf-8 -*-

from cwr.grammar.factory.adapter import *
from cwr.grammar.factory.rule import RuleFactory
import logging


"""
Grammar fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class FieldTerminalRuleFactory(RuleFactory):
    """
    Factory for acquiring field rules.
    """

    def __init__(self, field_configs, adapters):
        super(FieldTerminalRuleFactory, self).__init__()
        # Fields already created
        self._fields = {}
        # Field adapters being used
        self._adapters = adapters
        # Configuration for creating the fields
        self._field_configs = field_configs

    def get_rule(self, field_id):
        """
        Returns the rule for the field identified by the id.

        If it is set as not being compulsory, the rule will be adapted to accept string composed only of white
        characters.

        :param field_id: unique id in the system for the field
        :return: the rule of a field
        """

        if field_id in self._fields:
            # Field already exists
            field = self._fields[field_id]
        else:
            # Field configuration info
            config = self._field_configs[field_id]

            # Field does not exist
            # It is created
            field = self.create_field(field_id, config)

            # Field is saved
            self._fields[field_id] = field

        return field

    def create_field(self, field_id, config):
        """
        Creates the field with the specified parameters.

        :param field_id: identifier for the field
        :param config: configuration info for the field
        :return: the basic rule for the field
        """

        adapter = self._adapters[config['type']]

        if 'name' in config:
            name = config['name']
        else:
            name = None

        if 'size' in config:
            columns = config['size']
        else:
            columns = None

        if 'values' in config:
            values = config['values']
        else:
            values = None

        field = adapter.get_field(name, columns, values)

        if 'results_name' in config:
            field = field.setResultsName(config['results_name'])
        else:
            field = field.setResultsName(field_id)

        return field


class OptionFieldTerminalRuleFactory(object):
    """
    Factory for acquiring field rules where those rules can be optional.

    This factory gives support to optional field rules.

    An optional field is one where a string composed only of white characters is valid.

    Field rules will be created only once. If the same one is required again, then the one created the first time will
    be returned.
    """

    def __init__(self, field_configs, adapters):
        super(OptionFieldTerminalRuleFactory, self).__init__()

        self._field_factory = FieldTerminalRuleFactory(field_configs,adapters)
        self._field_configs = field_configs
        self._adapters = adapters

        # Fields already wrapped with the optional wrapper
        self._fields_optional = {}

    def get_rule(self, field_id, compulsory=False):
        """
        Returns the field identified by the id.

        This field is unique, it will be created just once and reused for all the following calls of the method.

        If it is set as not being compulsory, a special wrapping rule, allowing an empty string, will be added to
        the field.

        :param field_id: unique id in the system for the field
        :param compulsory: indicates if the empty string is rejected or not
        :return: a lookup field
        """

        if not compulsory:
            if field_id in self._fields_optional:
                # Wrapped field already exists
                field = self._fields_optional[field_id]
            else:
                # Field configuration info
                config = self._field_configs[field_id]

                field = self._field_factory.get_rule(field_id)

                # It is not compulsory, the wrapped is added
                adapter = self._adapters[config['type']]
                field = adapter.wrap_as_optional(field, config['name'], config['size'])

                # Wrapped field is saved
                self._fields_optional[field_id] = field
        else:
            field = self._field_factory.get_rule(field_id)

        return field


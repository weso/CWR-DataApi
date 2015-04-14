# -*- coding: utf-8 -*-

import logging

from data.accessor import CWRConfiguration
from cwr.grammar.factory.adapter import *
from cwr.grammar.factory.rule import RuleFactory


"""
Grammar fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""


class FieldFactory(object):
    """
    Factory for acquiring field rules.
    """
    __metaclass__ = ABCMeta

    def __init__(self, field_configs):
        # Fields already created
        self._fields = {}
        # Field builders being used
        self._adapters = {}
        # Logger
        self._logger = logging.getLogger(__name__)
        # Configuration for creating the fields
        self._field_configs = field_configs

    def get_field(self, id):
        """
        Returns the rule for the field identified by the id.

        If it is set as not being compulsory, the rule will be adapted to accept string composed only of white
        characters.

        :param id: unique id in the system for the field
        :param compulsory: indicates if the empty string is rejected or not
        :return: the rule of a field
        """
        self._logger.info('Acquiring field %s' % id)

        # Field configuration info
        config = self._field_configs[id]

        if id in self._fields:
            # Field already exists
            self._logger.info('Field %s already exists, using saved instance' % id)
            field = self._fields[id]
        else:
            # Field does not exist
            # It is created
            self._logger.info('Field %s does not exist, creating new instance' % id)
            field = self.create_field(id, config)

            # Field is saved
            self._fields[id] = field

        return field

    @abstractmethod
    def create_field(self, id, config):
        """
        Creates the field with the specified parameters.

        :param id: identifier for the field
        :param config: configuration info for the field
        :return: the basic rule for the field
        """
        raise NotImplementedError("The create_field method is not implemented")


class OptionFieldFactory(FieldFactory, RuleFactory):
    """
    Factory for acquiring field rules where those rules can be optional.

    This factory gives support to optional field rules.

    An optional field is one where a string composed only of white characters is valid.

    Field rules will be created only once. If the same one is required again, then the one created the first time will
    be returned.
    """
    __metaclass__ = ABCMeta

    def __init__(self, field_configs):
        super(OptionFieldFactory, self).__init__(field_configs)

        # Fields already wrapped with the optional wrapper
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
        self._logger.info('Acquiring field %s' % id)

        if not compulsory:
            if id in self._fields_optional:
                # Wrapped field already exists
                self._logger.info('Wrapped field %s does not exist, creating new instance' % id)
                field = self._fields_optional[id]
            else:
                # Field configuration info
                config = self._field_configs[id]

                field = super(OptionFieldFactory, self).get_field(id)

                # It is not compulsory, the wrapped is added
                self._logger.info('Wrapped field %s already exists, using saved instance' % id)
                field = self.not_compulsory_wrapper(field, config['type'], config['name'], config['size'])

                # Wrapped field is saved
                self._fields_optional[id] = field
        else:
            field = super(OptionFieldFactory, self).get_field(id)

        return field

    @abstractmethod
    def not_compulsory_wrapper(self, field, type, name, columns):
        """
        Adds a wrapper rule to the field to accept empty strings.

        This empty string should be of the same size as the columns parameter. One smaller or bigger will be rejected.

        This wrapper will return None if the field is empty.

        :param field: the field to wrap
        :param name: name of the field
        :param columns: number of columns it takes
        :return: the field with an additional rule to allow empty strings
        """
        raise NotImplementedError("The create_field method is not implemented")


class DefaultFieldFactory(OptionFieldFactory):
    """
    Factory for acquiring fields rules using the default configuration.
    """

    def __init__(self, field_configs, field_values=None, field_rules=None, actions=None):
        super(DefaultFieldFactory, self).__init__(field_configs)

        # TODO: Don't do this manually
        self._adapters['alphanum'] = AlphanumAdapter()
        self._adapters['alphanum_ext'] = ExtendedAlphanumAdapter()
        self._adapters['numeric'] = NumericAdapter()
        self._adapters['boolean'] = BooleanAdapter()
        self._adapters['flag'] = FlagAdapter()
        self._adapters['date'] = DateAdapter()
        self._adapters['time'] = TimeAdapter()
        self._adapters['date_time'] = DateTimeAdapter()
        self._adapters['blank'] = BlankAdapter()
        self._adapters['lookup'] = LookupAdapter()
        self._adapters['iswc'] = ISWCAdapter()
        self._adapters['ipi_name_n'] = IPINameNumberAdapter()
        self._adapters['ipi_base_n'] = IPIBaseNumberAdapter()
        self._adapters['percentage'] = PercentageAdapter()
        self._adapters['ean13'] = EAN13Adapter()
        self._adapters['isrc'] = ISRCAdapter()
        self._adapters['visan'] = VISANAdapter()
        self._adapters['avi'] = AudioVisualKeydapter()
        self._adapters['charset'] = CharSetAdapter()
        self._adapters['alphanum_variable'] = VariableAlphanumAdapter()
        self._adapters['numeric_float'] = NumericFloatAdapter()

        # Field values are optional
        self._field_values = field_values

        if field_rules is None:
            self._field_rules = basic
        else:
            self._field_rules = field_rules

        if actions is None:
            self._actions = DefaultActionsSource()
        else:
            self._actions = actions

    def get_rule(self, id, modifiers):
        compulsory = 'compulsory' in modifiers

        return self.get_field(id, compulsory=compulsory)

    def create_field(self, id, config):
        """
        Creates the field with the specified parameters.

        :param id: identifier for the field
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
        elif self._field_values and 'source' in config:
            values_id = config['source']
            values = self._field_values.get_data(values_id)
        else:
            values = None

        field = adapter.get_field(name, columns, values)

        if 'results_name' in config:
            field = field.setResultsName(config['results_name'])
        else:
            field = field.setResultsName(id)

        # Actions are added
        if 'actions' in config:
            self.__add_actions(field, config['actions'])

        return field

    def not_compulsory_wrapper(self, field, type, name, columns):

        adapter = self._adapters[type]

        return adapter.wrap_as_optional(field, name, columns)

    def __add_actions(self, field, actions):
        """
        Adds parsing actions to the rule.

        :param field: field rule where the actions are to be added
        :param actions: identifiers for the actions to add
        """
        for action in actions:
            action_method = getattr(self._actions, action)

            field.setParseAction(lambda p: action_method(p))


class DefaultActionsSource():
    def __init__(self):
        self._config = CWRConfiguration()

    def to_default_filename_version(self, parsed):
        return self._config.default_version()

    def to_int(self, parsed):
        value = parsed[0]

        if value is None:
            return None
        else:
            return int(parsed[0])

    def to_year(self, parsed):
        """
        Transforms the parsed two digits integer into a valid year value.

        :param parsed: the parsed value
        """
        value = parsed[0]

        if not isinstance(value, int):
            value = int(value)
        else:
            value = parsed

        return 2000 + value
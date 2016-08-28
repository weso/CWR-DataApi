# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from cwr.parser.encoder.common import Encoder

"""
Classes for encoding sample field into cwr format. The encoding rules are based on config files, they understand type,
length and special features such as fill empty date by zeros

"""

__author__ = 'Yaroslav O. Golub'
__license__ = 'MIT'
__status__ = 'Development'


class CwrFieldEncoder(Encoder):
    """
    Abstract class for create sample handler for one field in record. Possible it can normalize data in encoding proccess
    """
    __metaclass__ = ABCMeta

    _rule = None
    _required = True

    def __init__(self, name, rule, required=True):
        super(CwrFieldEncoder, self).__init__()
        self.name = name
        self._required = required
        self._rule = rule

    def _blank(self):
        return "".center(self._rule['size'], ' ')

    @abstractmethod
    def format(self, value):
        """
        Return template for perform string formatting operation
        :return: format template
        """
        raise NotImplementedError('The format method must be implemented')

    def expand_entity(self, entity):
        """
        Search and return entity or sub entity that contain value of this field.
        :param entity:
        :return: entity
        :raise KeyError
        """
        if self.name in entity:
            return entity
        for key, value in entity.items():
            if isinstance(value, dict):
                if self.name in value:
                    return value
        raise KeyError("The field %s (%s) not found in %s" % (self.name, self._rule['type'], entity))

    def encode(self, entity):
        """
        Encode this
        :param entity:
        :return: cwr string
        """
        entity = self.expand_entity(entity)
        value = entity[self.name]
        result = self.format(value)
        return result

    def __repr__(self):
        return "Field %s, size: %d, type: %s, req: %s" % \
            (self.name, self._rule['size'], self._rule['type'], self._required)


class DefaultCwrFieldEncoder(CwrFieldEncoder):
    """
    String type encoder
    """
    def format(self, value):
        if value is None:
            return self._blank()
        tpl = "{!s:<%d}" % self._rule['size']
        return tpl.format(str(value))


class NumericCwrFieldEncoder(CwrFieldEncoder):
    """
    Numeric type encoder
    """
    def format(self, value):
        if value is None or value == '':
            value = 0
        tpl = "{:0>%d}" % self._rule['size']
        return tpl.format(str(value))


class NumericEmptyCwrFieldEncoder(CwrFieldEncoder):
    """
    Numeric type encoder but encode to blank string when value is none
    """
    def format(self, value):
        if value is None or value == '':
            return self._blank()
        else:
            tpl = "{:0>%d}" % self._rule['size']
            return tpl.format(str(value))


class BooleanCwrFieldEncoder(DefaultCwrFieldEncoder):
    """
    Boolean encoder
    """
    def format(self, value):
        return 'Y' if value else 'N'


class FlagCwrFieldEncoder(DefaultCwrFieldEncoder):
    """
    Empty inherit class for flag encoding
    """
    pass


class DateCwrFieldEncoder(CwrFieldEncoder):
    """
    Date encoder
    """
    def format(self, value):
        if value is None:
            fmt = "{:0>%d}" % (self._rule['size'])
            return fmt.format(0)
        else:
            return "{:%Y%m%d}".format(value)


class DateTimeCwrFieldEncoder(DateCwrFieldEncoder):
    """
    Datetime encoder
    """
    def format(self, value):
        if value is None:
            fmt = "{:0>%d}" % (self._rule['size'])
            return fmt.format(0)
        else:
            return "{:%Y%m%d%H%M%S}".format(value)

class TimeCwrFieldEncoder(DateCwrFieldEncoder):
    """
    Time encoder
    """
    def format(self, value):
        if value is None:
            fmt = "{:0>%d}" % (self._rule['size'])
            return fmt.format(0)
        else:
            return "{:%H%M%S}".format(value)

class LookupCwrFieldEncoder(DefaultCwrFieldEncoder):
    """
    Lookup type encoder
    """
    _values = []

    def __init__(self, name, rule, required=True, values=[]):
        super(LookupCwrFieldEncoder, self).__init__(name, rule, required=required)
        self.set_values(values)

    def set_values(self, values):
        self._values = values


class LookupNumericCwrFieldEncoder(NumericEmptyCwrFieldEncoder, LookupCwrFieldEncoder):
    """
    Lookup_int type encoder. Mu
    """
    pass

class BlankCwrFieldEncoder(DefaultCwrFieldEncoder):
    """
    The blank type encoder
    """
    def encode(self, entity):
        return "".center(self._rule['size'], ' ')


class PercentageCwrFieldEncoder(NumericCwrFieldEncoder):
    """
    Percentage type encoder
    """
    def format(self, value):
        if value is None or value == '':
            value = 0
        else:
            value = int(round(value * 100))
        return super(PercentageCwrFieldEncoder, self).format(value)


class IpiCwrFieldEncoder(NumericEmptyCwrFieldEncoder):
    """
    """
    pass


class AviCwrFieldEncoder(CwrFieldEncoder):
    """
    AVI decoder
    """
    def format(self, value):
        tpl = "{av_number!s:0>2}{society_code!s:<15}"
        return tpl.format(**value)


class CwrFieldEncoderFactory(object):
    """
    Factory for produce field encoders
    """

    def __init__(self, field_configs):
        super(CwrFieldEncoderFactory, self).__init__()
        self._field_configs = field_configs

    def get_field_encoder(self, name, req):
        field = self._field_configs[name]

        if 'results_name' in field:
            name = field['results_name']

        field_type = field['type']

        if field_type == 'alphanum':
            return DefaultCwrFieldEncoder(name, field, req)
        elif field_type == 'alphanum_ext':
            return DefaultCwrFieldEncoder(name, field, req)
        elif field_type == 'alphanum_end':
            return DefaultCwrFieldEncoder(name, field, req)
        elif field_type == 'numeric':
            return NumericCwrFieldEncoder(name, field, required=req)
        elif field_type == 'date':
            return DateCwrFieldEncoder(name, field, required=req)
        elif field_type == 'date_time':
            return DateTimeCwrFieldEncoder(name, field, required=req)
        elif field_type == 'time':
            return TimeCwrFieldEncoder(name, field, required=req)
        elif field_type == 'boolean':
            return BooleanCwrFieldEncoder(name, field, required=req)
        elif field_type == 'flag':
            return FlagCwrFieldEncoder(name, field, required=req)
        elif field_type == 'blank':
            return BlankCwrFieldEncoder(name, field, required=req)
        elif field_type == 'lookup':
            return LookupCwrFieldEncoder(name, field, required=req, values=field['values'])
        elif field_type == 'percentage':
            return PercentageCwrFieldEncoder(name, field, required=req)
        elif field_type == 'lookup_int':
            return LookupNumericCwrFieldEncoder(name, field, required=req, values=field['values'])
        elif field_type == 'ipi_base_n':
            return IpiCwrFieldEncoder(name, field, required=req)
        elif field_type == 'ipi_name_n':
            return IpiCwrFieldEncoder(name, field, required=req)
        elif field_type == 'avi':
            return AviCwrFieldEncoder(name, field, required=req)
        elif field_type == 'charset':
            return DefaultCwrFieldEncoder(name, field, required=req)
        elif field_type == 'iswc':
            return DefaultCwrFieldEncoder(name, field, required=req)
        elif field_type == 'ean13':
            return DefaultCwrFieldEncoder(name, field, required=req)
        elif field_type == 'isrc':
            return DefaultCwrFieldEncoder(name, field, required=req)
        elif field_type == 'visan':
            return DefaultCwrFieldEncoder(name, field, required=req)
        else:
            raise Exception('Not found type: %s' % field_type)
            return DefaultCwrFieldEncoder(name, field, req)

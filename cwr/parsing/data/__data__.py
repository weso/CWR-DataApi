import os
import csv

__author__ = 'Bernardo'

_types = []


def __path():
    return os.path.dirname(__file__)


def record_types():
    if len(_types) == 0:
        with open(os.path.join(__path(), os.path.basename('cwr_record_type.csv')), 'rt') as csvfile:
            headers_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for type_row in headers_reader:
                for t in type_row:
                    _types.append(t)

    return _types
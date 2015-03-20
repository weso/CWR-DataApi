# -*- coding: utf-8 -*-


from cwr.grammar.field import special
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from data.accessor import CWRConfiguration


"""
CWR Society-related grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_lookup_factory = DefaultFieldFactory(CWRConfiguration().load_field_config('table'), CWRTables())


# Performing Rights Share
def pr_share(maximum=100, compulsory=False):
    pr_share_field = special.shares(maximum=maximum, compulsory=compulsory)
    pr_share_field = pr_share_field.setName('Performing Rights Share').setResultsName('pr_share')

    return pr_share_field


# Mechanical Rights Share
def mr_share(maximum=100, compulsory=False):
    mr_share_field = special.shares(maximum=maximum, compulsory=compulsory)
    mr_share_field = mr_share_field.setName('Mechanical Rights Share').setResultsName('mr_share')

    return mr_share_field


# Synchronization Rights Share
def sr_share(maximum=100, compulsory=False):
    sr_share_field = special.shares(maximum=maximum, compulsory=compulsory)
    sr_share_field = sr_share_field.setName('Synchronization Rights Share').setResultsName('sr_share')

    return sr_share_field
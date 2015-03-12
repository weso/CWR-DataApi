# -*- coding: utf-8 -*-


from cwr.grammar.field import table, special


"""
CWR Society-related grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


# Performing Rights Affiliation Society
def pr_affiliation(compulsory=False):
    pr_affiliation_field = table.society(compulsory=compulsory)
    pr_affiliation_field = pr_affiliation_field.setName('Performing Rights Affiliation Society').setResultsName(
        'pr_society')

    return pr_affiliation_field


# Performing Rights Share
def pr_share(maximum=100, compulsory=False):
    pr_share_field = special.shares(maximum=maximum, compulsory=compulsory)
    pr_share_field = pr_share_field.setName('Performing Rights Share').setResultsName('pr_share')

    return pr_share_field


# Mechanical Rights Affiliation Society
def mr_affiliation(compulsory=False):
    mr_affiliation_field = table.society(compulsory=compulsory)
    mr_affiliation_field = mr_affiliation_field.setName('Mechanical Rights Affiliation Society').setResultsName(
        'mr_society')

    return mr_affiliation_field


# Mechanical Rights Share
def mr_share(maximum=100, compulsory=False):
    mr_share_field = special.shares(maximum=maximum, compulsory=compulsory)
    mr_share_field = mr_share_field.setName('Mechanical Rights Share').setResultsName('mr_share')

    return mr_share_field


# Synchronization Rights Affiliation Society
def sr_affiliation(compulsory=False):
    sr_affiliation_field = table.society(compulsory=compulsory)
    sr_affiliation_field = sr_affiliation_field.setName('Synchronization Rights Affiliation Society').setResultsName(
        'sr_society')

    return sr_affiliation_field


# Synchronization Rights Share
def sr_share(maximum=100, compulsory=False):
    sr_share_field = special.shares(maximum=maximum, compulsory=compulsory)
    sr_share_field = sr_share_field.setName('Synchronization Rights Share').setResultsName('sr_share')

    return sr_share_field
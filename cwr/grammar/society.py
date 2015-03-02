# -*- encoding: utf-8 -*-


from cwr.grammar import field_special


"""
CWR Society-related grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Performing Rights Affiliation Society
pr_affiliation = field_special.society()
pr_affiliation = pr_affiliation.setName('Performing Rights Affiliation Society').setResultsName('pr_society')

# Performing Rights Share
pr_share = field_special.shares()
pr_share = pr_share.setName('Performing Rights Share').setResultsName('pr_share')

# Mechanical Rights Affiliation Society
mr_affiliation = field_special.society()
mr_affiliation = mr_affiliation.setName('Mechanical Rights Affiliation Society').setResultsName('mr_society')

# Mechanical Rights Share
mr_share = field_special.shares()
mr_share = mr_share.setName('Mechanical Rights Share').setResultsName('mr_share')

# Synchronization Rights Affiliation Society
sr_affiliation = field_special.society()
sr_affiliation = sr_affiliation.setName('Synchronization Rights Affiliation Society').setResultsName('sr_society')

# Synchronization Rights Share
sr_share = field_special.shares()
sr_share = sr_share.setName('Synchronization Rights Share').setResultsName('sr_share')
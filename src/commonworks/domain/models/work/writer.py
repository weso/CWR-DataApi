# -*- encoding: utf-8 -*-
from commonworks.domain.models.entity import Entity

"""
Writer entity model classes.
"""

__author__ = 'Borja Garrido Bear'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Writer(Entity):
    """
    Represents a CWR writer.
    """

    def __init__(self, submitter_id):
        super(Writer, self).__init__(submitter_id)

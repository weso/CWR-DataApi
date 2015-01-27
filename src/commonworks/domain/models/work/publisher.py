# -*- encoding: utf-8 -*-
from commonworks.domain.models.entity import Entity

"""
Publisher entity model classes.
"""

__author__ = 'Borja Garrido Bear'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Publisher(Entity):
    """
    Represents a CWR publisher.
    """

    def __init__(self, submitter_id):
        super(Publisher, self).__init__(submitter_id)

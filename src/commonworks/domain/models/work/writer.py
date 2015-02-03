# -*- encoding: utf-8 -*-
from commonworks.domain.models.entity import Entity

"""
Writer entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Writer(Entity):
    """
    Represents a CWR writer.
    """

    def __init__(self, submitter_id, interested_party, first_name, last_name, designation_code,
                 tax_id_number, cae_ipi_name_id, pr_society, pr_share,
                 mr_society, mr_share, sr_society, sr_share, reversionary_indicator,
                 first_recording_refusal_indicator, work_for_hire_indicator,
                 ipi_base_number, personal_number, usa_license_indicator):
        super(Writer, self).__init__(submitter_id)

        self._interested_party = interested_party
        self._first_name = first_name
        self._last_name = last_name
        self._designation_code = designation_code
        self._tax_id_number = tax_id_number
        self._cae_ipi_name_id = cae_ipi_name_id
        self._pr_society = pr_society
        self._pr_share = pr_share
        self._mr_society = mr_society
        self._mr_share = mr_share
        self._sr_society = sr_society
        self._sr_share = sr_share
        self._reversionary_indicator = reversionary_indicator
        self._first_recording_refusal_indicator = first_recording_refusal_indicator
        self._work_for_hire_indicator = work_for_hire_indicator
        self._ipi_base_number = ipi_base_number
        self._personal_number = personal_number
        self._usa_license_indicator = usa_license_indicator

    @property
    def cae_ipi_name_id(self):
        return self._cae_ipi_name_id

    @property
    def designation_code(self):
        return self._designation_code

    @property
    def first_name(self):
        return self._first_name

    @property
    def first_recording_refusal_indicator(self):
        return self._first_recording_refusal_indicator

    @property
    def interested_party(self):
        return self._interested_party

    @property
    def ipi_base_number(self):
        return self._ipi_base_number

    @property
    def last_name(self):
        return self._last_name

    @property
    def mr_share(self):
        return self._mr_share

    @property
    def mr_society(self):
        return self._mr_society

    @property
    def personal_number(self):
        return self._personal_number

    @property
    def pr_share(self):
        return self._pr_share

    @property
    def pr_society(self):
        return self._pr_society

    @property
    def reversionary_indicator(self):
        return self._reversionary_indicator

    @property
    def sr_share(self):
        return self._sr_share

    @property
    def sr_society(self):
        return self._sr_society

    @property
    def tax_id_number(self):
        return self._tax_id_number

    @property
    def usa_license_indicator(self):
        return self._usa_license_indicator

    @property
    def work_for_hire_indicator(self):
        return self._work_for_hire_indicator

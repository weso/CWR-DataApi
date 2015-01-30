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

    def __init__(self, submitter_id, interested_party, first_name, last_name, designation_code,
                 tax_id_number, cae_ipi_name_id, pr_society, pr_share,
                 mr_society, mr_share, sr_society, sr_share, reversionary_indicator,
                 first_recording_refusal_indicator, work_for_hire_indicator,
                 ipi_base_number, personal_number, usa_license_indicator):
        super(Writer, self).__init__(submitter_id)

        self.interested_party = interested_party
        self.first_name = first_name
        self.last_name = last_name
        self.designation_code = designation_code
        self.tax_id_number = tax_id_number
        self.cae_ipi_name_id = cae_ipi_name_id
        self.pr_society = pr_society
        self.pr_share = pr_share
        self.mr_society = mr_society
        self.mr_share = mr_share
        self.sr_society = sr_society
        self.sr_share = sr_share
        self.reversionary_indicator = reversionary_indicator
        self.first_recording_refusal_indicator = first_recording_refusal_indicator
        self.work_for_hire_indicator = work_for_hire_indicator
        self.ipi_base_number = ipi_base_number
        self.personal_number = personal_number
        self.usa_license_indicator = usa_license_indicator

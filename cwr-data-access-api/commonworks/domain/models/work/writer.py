from commonworks.domain.models.entity import Entity

__author__ = 'borja'


class Writer(Entity):
    def __init__(self, submitter_id, json_item):
        super(Writer, self).__init__(submitter_id)

        self.interested_party_id = json_item['interested_party_id']
        self.mongo_ipa_id = None

        self.first_name = json_item['first_name']
        self.last_name = json_item['last_name']
        self.designation_code = json_item['designation_code']
        self.tax_id_number = json_item['tax_id_number']
        self.cae_ipi_name_id = json_item['cae_ipi_name_id']
        self.pr_society = json_item['pr_society']
        self.pr_share = json_item['pr_share']
        self.mr_society = json_item['mr_society']
        self.mr_share = json_item['mr_share']
        self.sr_society = json_item['sr_society']
        self.sr_share = json_item['sr_share']
        self.reversionary_indicator = json_item['reversionary_indicator']
        self.first_recording_refusal_indicator = json_item['first_recording_refusal_indicator']
        self.work_for_hire_indicator = json_item['work_for_hire_indicator']
        self.ipi_base_number = json_item['ipi_base_number']
        self.personal_number = json_item['personal_number']
        self.usa_license_indicator = json_item['usa_license_indicator']

    def to_mongo_dict(self):
        writer_dict = {}

        writer_dict['interested_party'] = self.mongo_ipa_id

        writer_dict['first_name'] = self.first_name
        writer_dict['last_name'] = self.last_name
        writer_dict['designation_code'] = self.designation_code
        writer_dict['tax_id_number'] = self.tax_id_number
        writer_dict['cae_ipi_name_id'] = self.cae_ipi_name_id
        writer_dict['pr_society'] = self.pr_society
        writer_dict['pr_share'] = self.pr_share
        writer_dict['mr_society'] = self.mr_society
        writer_dict['mr_share'] = self.mr_share
        writer_dict['sr_society'] = self.sr_society
        writer_dict['sr_share'] = self.sr_share
        writer_dict['reversionary_indicator'] = self.reversionary_indicator
        writer_dict['first_recording_refusal_indicator'] = self.first_recording_refusal_indicator
        writer_dict['work_for_hire_indicator'] = self.work_for_hire_indicator
        writer_dict['ipi_base_number'] = self.ipi_base_number
        writer_dict['personal_number'] = self.personal_number
        writer_dict['usa_license_indicator'] = self.usa_license_indicator

        return writer_dict
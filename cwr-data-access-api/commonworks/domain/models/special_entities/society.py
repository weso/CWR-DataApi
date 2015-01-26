__author__ = 'borja'


class Society(object):
    def __init__(self, code, name, former_name):
        self.id = code
        self.name = name
        self.former_name = former_name

    def to_mongo_dict(self):
        society_dict = {}

        society_dict['_id'] = self.id
        society_dict['name'] = self.name
        society_dict['former_name'] = self.former_name

        return society_dict

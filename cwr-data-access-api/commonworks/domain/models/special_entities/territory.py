__author__ = 'borja'


class Territory(object):
    def __init__(self, tis, iso2=None, territory_type=None, name=None, official_name=None):
        self.tis = tis
        self.iso2 = iso2
        self.type = territory_type
        self.name = name
        self.official_name = official_name

    def to_mongo_dict(self):
        territory_dict = {}

        territory_dict['_id'] = self.tis
        territory_dict['iso2'] = self.iso2
        territory_dict['type'] = self.type
        territory_dict['name'] = self.name
        territory_dict['official_name'] = self.official_name

        return territory_dict
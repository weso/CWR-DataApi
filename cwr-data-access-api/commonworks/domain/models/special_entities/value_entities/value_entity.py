__author__ = 'borja'


class ValueEntity(object):
    def __init__(self, id, name, description, table):
        self.table = table

        self.id = id
        self.name = name
        self.description = description

    def to_mongo_dict(self):
        value_dict = {}

        value_dict['_id'] = self.id
        value_dict['name'] = self.name

        if self.description is not None:
            value_dict['description'] = self.description

        return value_dict


class AgreementRole(ValueEntity):
    def __init__(self, id, name, description):
        super(AgreementRole, self).__init__(id, name, description, 'agreement_roles')


class AgreementType(ValueEntity):
    def __init__(self, id, name, description):
        super(AgreementType, self).__init__(id, name, description, 'agreement_types')


class CompositeType(ValueEntity):
    def __init__(self, id, name, description):
        super(CompositeType, self).__init__(id, name, description, 'composite_types')


class DistributionCategory(ValueEntity):
    def __init__(self, id, name, description):
        super(DistributionCategory, self).__init__(id, name, description, 'distribution_categories')


class ExcerptType(ValueEntity):
    def __init__(self, id, name, description):
        super(ExcerptType, self).__init__(id, name, description, 'excerpt_types')


class LyricAdaptation(ValueEntity):
    def __init__(self, id, name, description):
        super(LyricAdaptation, self).__init__(id, name, description, 'lyric_adaptations')


class MusicArrangement(ValueEntity):
    def __init__(self, id, name, description):
        super(MusicArrangement, self).__init__(id, name, description, 'music_arrangements')


class TextMusicRelationship(ValueEntity):
    def __init__(self, id, name, description):
        super(TextMusicRelationship, self).__init__(id, name, description, 'text_music_relationships')


class VersionType(ValueEntity):
    def __init__(self, id, name, description):
        super(VersionType, self).__init__(id, name, description, 'version_types')


class WorkType(ValueEntity):
    def __init__(self, id, name):
        super(WorkType, self).__init__(id, name, None, 'work_types')
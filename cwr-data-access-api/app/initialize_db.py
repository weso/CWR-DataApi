from app.infrastructure.mongo_repos.value_entities_repository import ValueEntityRepository
from commonworks.domain.models.special_entities.value_entities.value_entity import AgreementRole, AgreementType, \
    CompositeType, DistributionCategory, ExcerptType, LyricAdaptation, MusicArrangement, TextMusicRelationship, \
    VersionType, WorkType

__author__ = 'borja'

def _add_agreement_roles(url_root):
    agreement_role_repository = ValueEntityRepository(url_root=url_root, collection='agreement_roles')
    agreement_role_repository.insert_item(AgreementRole('AS', 'Assignor',
                                                'The entitled party who is assigning the rights to a musical work within an agreement'))
    agreement_role_repository.insert_item(AgreementRole('AC', 'Acquirer',
                                                'The entitled party who is acquiring the rights to a musical work within an agreement'))


def _add_agreement_types(url_root):
    agreement_type_repository = ValueEntityRepository(url_root=url_root, collection='agreement_types')
    agreement_type_repository.insert_item(AgreementType('OS', 'Original Specific',
                                                'Agreement between the songwriter and original publisher covering a list of specific work(s)'))
    agreement_type_repository.insert_item(AgreementType('PS', 'Subpublishing Specific',
                                                'Agreement between two publishers covering a list of specific work(s)'))
    agreement_type_repository.insert_item(AgreementType('PG', 'Subpublishing General',
                                                'Agreement between two publishers covering all works in a catalogue'))
    agreement_type_repository.insert_item(AgreementType('OG', 'Original General',
                                                'Agreement between the songwriter and original publisher covering all works in a catalogue'))


def _add_composite_types(url_root):
    composite_types_repository = ValueEntityRepository(url_root=url_root, collection='composite_types')
    composite_types_repository.insert_item(CompositeType('COS', 'Composite of Samples',
                                                 'A composite work containing new material and one or more samples of pre-existing recorded works'))
    composite_types_repository.insert_item(CompositeType('MED', 'Medley',
                                                 'A continuous and sequential combination of existing works or excerpts'))
    composite_types_repository.insert_item(CompositeType('POT', 'Porpourri',
                                                 'A composite work with the addition of original material which have been combined to form a new work, that has been published and printed'))
    composite_types_repository.insert_item(CompositeType('UCO', 'Unspecified Composite',
                                                 'Works known to be a composite but where the type of composite is unknown'))


def _add_distribution_categories(url_root):
    distribution_repository = ValueEntityRepository(url_root=url_root, collection='distribution_categories')
    distribution_repository.insert_item(DistributionCategory('JAZ', 'Jazz',
                                                     'Music originating in black America from the early 20th century, incorporating strands of Euro-American and African music and frequently containing improvisation'))
    distribution_repository.insert_item(DistributionCategory('POP', 'Popular',
                                                     'The musical mainstream, usually song-based and melody-orientated, created for mass consumption'))
    distribution_repository.insert_item(DistributionCategory('SER', 'Serious',
                                                     'Classical or art music'))
    distribution_repository.insert_item(DistributionCategory('UNC', 'Unclassified Distribution Category',
                                                     'The catch-all for societies who do not track genres; all works are paid the same regardless of genre'))


def _add_excerpt_types(url_root):
    excerpt_types_service = ValueEntityRepository(url_root=url_root, collection='excerpt_types')
    excerpt_types_service.insert_item(ExcerptType('MOV', 'Movement', 'A principal division of a musical work'))
    excerpt_types_service.insert_item(ExcerptType('UEX', 'Unspecified Excerpt',
                                             'A work that is known to be an excerpt from another work, however the type of excerpt is unknown'))


def _add_lyric_adaptations(url_root):
    lyric_adaptations_service = ValueEntityRepository(url_root=url_root, collection='lyric_adaptations')
    lyric_adaptations_service.insert_item(LyricAdaptation('NEW', 'New',
                                                     'New lyrics added to the existing lyrics'))
    lyric_adaptations_service.insert_item(LyricAdaptation('MOD', 'Modification',
                                                     'Lyrics modified in the original language'))
    lyric_adaptations_service.insert_item(LyricAdaptation('NON', 'None', 'No lyrics have been included in the work'))
    lyric_adaptations_service.insert_item(LyricAdaptation('ORI', 'Original', 'Lyrics have been used in the original form'))
    lyric_adaptations_service.insert_item(LyricAdaptation('REP', 'Replacement', 'Lyrics have been totally replaced'))
    lyric_adaptations_service.insert_item(LyricAdaptation('ADL', 'Addition',
                                                     'Lyrics added to a pre-existing instrumental work'))
    lyric_adaptations_service.insert_item(LyricAdaptation('UNS', 'Unspecified',
                                                     'Details of the lyric adaptation are not known at this time'))
    lyric_adaptations_service.insert_item(LyricAdaptation('TRA', 'Translation',
                                                     'Lyrics translated into another language'))


def _add_music_arrangements(url_root):
    music_arrangements_service = ValueEntityRepository(url_root=url_root, collection='music_arrangements')
    music_arrangements_service.insert_item(MusicArrangement('NEW', 'New',
                                                       'New music added to existing music'))
    music_arrangements_service.insert_item(MusicArrangement('ARR', 'Arrangement',
                                                       'A version of a work in which musical elements have been modified'))
    music_arrangements_service.insert_item(MusicArrangement('ADM', 'Addition',
                                                       'Music added to a pre-existing text'))
    music_arrangements_service.insert_item(MusicArrangement('UNS', 'Unspecified Arrangement',
                                                       'To be used when it is known the work is an arrangement, but no further details are available'))
    music_arrangements_service.insert_item(MusicArrangement('ORI', 'Original',
                                                       'Music used in its original form'))


def _add_text_music_relationships(url_root):
    text_music_service = ValueEntityRepository(url_root=url_root, collection='text_music_relationships')
    text_music_service.insert_item(TextMusicRelationship('MUS', 'Music', 'Music only'))
    text_music_service.insert_item(TextMusicRelationship('MTX', 'Music and Text', 'Music and text combined'))
    text_music_service.insert_item(TextMusicRelationship('TXT', 'Text', ''))


def _add_version_types(url_root):
    version_type_service = ValueEntityRepository(url_root=url_root, collection='version_types')
    version_type_service.insert_item(VersionType('MOD', 'Modified version of a musical work',
                                            'A work resulting from the modification of a musical work'))
    version_type_service.insert_item(VersionType('ORI', 'Original work',
                                            'The first established form of a work'))


def _add_work_types(url_root):
    work_types_service = ValueEntityRepository(url_root=url_root, collection='work_types')
    work_types_service.insert_item(WorkType('TA', 'Triple A'))
    work_types_service.insert_item(WorkType('AC', 'Adult Contemporary'))
    work_types_service.insert_item(WorkType('AR', 'Album Oriented Rock'))
    work_types_service.insert_item(WorkType('AL', 'Alternative Music'))
    work_types_service.insert_item(WorkType('AM', 'Americana'))
    work_types_service.insert_item(WorkType('BD', 'Band'))
    work_types_service.insert_item(WorkType('BL', 'Bluegrass Music'))
    work_types_service.insert_item(WorkType('CD', 'Childrens Music'))
    work_types_service.insert_item(WorkType('CL', 'Classical Music'))
    work_types_service.insert_item(WorkType('CC', 'Contemporary Christian'))
    work_types_service.insert_item(WorkType('CT', 'Country Music'))
    work_types_service.insert_item(WorkType('DN', 'Dance'))
    work_types_service.insert_item(WorkType('FM', 'Film/ Television Music'))
    work_types_service.insert_item(WorkType('FK', 'Folk Music'))
    work_types_service.insert_item(WorkType('BG', 'Black Gospel'))
    work_types_service.insert_item(WorkType('SG', 'Southern Gospel'))
    work_types_service.insert_item(WorkType('JZ', 'Jazz Music'))
    work_types_service.insert_item(WorkType('JG', 'Jingles'))
    work_types_service.insert_item(WorkType('LN', 'Latin'))
    work_types_service.insert_item(WorkType('LA', 'Latina'))
    work_types_service.insert_item(WorkType('NA', 'New Age'))
    work_types_service.insert_item(WorkType('OP', 'Opera'))
    work_types_service.insert_item(WorkType('PK', 'Polka Music'))
    work_types_service.insert_item(WorkType('PP', 'Pop Music'))
    work_types_service.insert_item(WorkType('RP', 'Rap Music'))
    work_types_service.insert_item(WorkType('RK', 'Rock Music'))
    work_types_service.insert_item(WorkType('RB', 'Rhythm and Blues'))
    work_types_service.insert_item(WorkType('SD', 'Sacred'))
    work_types_service.insert_item(WorkType('SY', 'Symphonic'))


def _initialize_database(url_root):
    _add_agreement_roles(url_root)
    _add_agreement_types(url_root)
    _add_composite_types(url_root)
    _add_distribution_categories(url_root)
    _add_excerpt_types(url_root)
    _add_lyric_adaptations(url_root)
    _add_music_arrangements(url_root)
    _add_text_music_relationships(url_root)
    _add_version_types(url_root)
    _add_work_types(url_root)


def _drop_previous_database(url_root):
    ValueEntityRepository(url_root=url_root, collection='agreement_roles').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='agreement_types').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='composite_types').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='distribution_categories').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='excerpt_types').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='lyric_adaptations').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='music_arrangements').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='text_music_relationships').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='version_types').drop_collection()
    ValueEntityRepository(url_root=url_root, collection='work_types').drop_collection()


def initialize(url_root):
    _drop_previous_database(url_root)
    _initialize_database(url_root)
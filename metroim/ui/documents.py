from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from ui.models import City, Line, Station


@registry.register_document
class CityDocument(Document):
    class Index:
        name = 'city'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = City
        fields = [
            'name'
        ]


@registry.register_document
class LineDocument(Document):
    city = fields.NestedField(properties={
        'name': fields.TextField(),
    })

    class Index:
        name = 'line'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super().get_queryset().select_related('city')

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Car instance(s) from the related model.
        The related_models option should be used with caution because it can lead in the index
        to the updating of a lot of items.
        """
        if isinstance(related_instance, City):
            return related_instance.lines.all()

    class Django:
        model = Line
        related_models = [City]
        fields = [
            'name'
        ]

@registry.register_document
class StationDocument(Document):

    class Index:
        name = 'station'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    id = fields.IntegerField(attr='id')
    line = fields.TextField(attr='line_field_indexing')
    city = fields.TextField(attr='city_field_indexing')
    location = fields.GeoPointField(attr='location_field_indexing')

    class Django:
        model = Station
        fields = [
            'name'
        ]
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from ui.models import City, Line, Station


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
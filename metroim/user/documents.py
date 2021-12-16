from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from user.models import User

@registry.register_document
class UserDocument(Document):

    class Index:
        name = 'user'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    favorite_stations = fields.TextField(attr='stations')

    class Django:
        model = User
        fields = [
            'id',
            'email', 
            'first_name', 
            'last_name'
        ]
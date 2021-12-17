from django.contrib.auth import get_user
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from ui.models import Station
from user.models import User

@registry.register_document
class UserDocument(Document):

    class Index:
        name = 'user'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    favorite_stations = fields.NestedField(properties={
        'name': fields.TextField(),
        'order': fields.TextField(),
        'pk': fields.IntegerField(),
    }, include_in_root=True)

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Station):
            return related_instance.user_set.all()

    class Django:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name'
        ]
        related_models = [Station]

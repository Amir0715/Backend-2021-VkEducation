from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers
from user.models import User
from api.serializers import StationSerializer
from user.documents import UserDocument
class UserSerializer(serializers.ModelSerializer):

    favorite_stations = StationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'favorite_stations')

class UserDocumentSerializer(DocumentSerializer):

    favorite_stations = serializers.SerializerMethodField()

    def get_favorite_stations(self, obj):
        """Represent favorite_stations value."""
        try:
            return obj.favorite_stations.to_dict()
        except:
            return {}

    class Meta:
        document = UserDocument
        fields = (
            'id',
            'email',
            'first_name',
            'last_name'
        )

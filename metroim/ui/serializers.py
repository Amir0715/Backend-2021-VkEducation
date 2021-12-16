import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from ui.documents import StationDocument


class StationDocumentSerializer(DocumentSerializer):

    location = serializers.SerializerMethodField()

    def get_location(self, obj):
        """Represent location value."""
        try:
            return obj.location.to_dict()
        except:
            return {}

    class Meta:
        document = StationDocument
        fields = (
            'id',
            'name',
            'line',
            'city',
        )

from django.db.models import fields
from rest_framework import serializers
from user.models import User
from api.serializers import StationSerializer

class UserSerializer(serializers.ModelSerializer):

    favorite_stations = StationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'favorite_stations')

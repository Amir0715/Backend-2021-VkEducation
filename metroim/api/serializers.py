from rest_framework import serializers
from ui.models import City, Line, Station

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('id', 'name', 'order', 'latitude', 'longitude', 'line')

class LineSerializer(serializers.ModelSerializer):
    stations = StationSerializer(many=True, read_only=True)

    class Meta:
        model = Line
        fields = ('id', 'name', 'hex_color', 'city', 'stations')

class CitySerializer(serializers.ModelSerializer):
    lines = LineSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'lines')


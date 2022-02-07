from datetime import datetime
from rest_framework import serializers
from ui.models import City, Line, Station
from api.tasks import send_email


class EmailSendMixin(serializers.Serializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        text = '[{}]\nБыл создан объект модели {} - {}'.format(
            datetime.now().isoformat(),
            self.Meta.model,
            instance.name)
        send_email.delay(subject='Новый объект', text=text)
        print("SENDING EMIAL")
        return instance


class StationSerializer(EmailSendMixin, serializers.ModelSerializer):

    def validate(self, attrs):
        if attrs['latitude'] < -180 or attrs['latitude'] > 180:
            raise serializers.ValidationError(
                "latitude must be in range [-180, 180]")
        if attrs['longitude'] < -90 or attrs['longitude'] > 90:
            raise serializers.ValidationError(
                "longitude must be in range [-90, 90]")
        return attrs

    class Meta:
        model = Station
        fields = ('id', 'name', 'order', 'latitude', 'longitude', 'line')


class LineSerializer(EmailSendMixin, serializers.ModelSerializer):
    stations = StationSerializer(many=True, read_only=True)

    def validate(self, attrs):
        if len(attrs['hex_color']) != 6:
            raise serializers.ValidationError(
                "the length of hex_color should be equal to 6")
        try:
            int(attrs['hex_color'], 16)
        except ValueError:
            raise serializers.ValidationError(
                "hex_color must be hexadecimal color")
        return attrs

    class Meta:
        model = Line
        fields = ('id', 'name', 'hex_color', 'city', 'stations')


class CitySerializer(EmailSendMixin, serializers.ModelSerializer):
    lines = LineSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'lines')

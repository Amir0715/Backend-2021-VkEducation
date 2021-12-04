from rest_framework import viewsets
from ui.models import City, Line, Station

from api.serializers import CitySerializer, LineSerializer, StationSerializer

from django.views.decorators.http import require_GET
class CityViewSet(viewsets.ModelViewSet):
    '''
    '''

    serializer_class = CitySerializer
    queryset = City.objects.all()


class LineViewSet(viewsets.ModelViewSet):
    '''
    '''

    serializer_class = LineSerializer
    queryset = Line.objects.all()


class StationViewSet(viewsets.ModelViewSet):
    '''
    '''

    serializer_class = StationSerializer
    queryset = Station.objects.all()

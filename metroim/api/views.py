import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from api.decorators import require_body
from ui.models import City, Line, Station
from rest_framework import viewsets
from api.serializers import CitySerializer, LineSerializer, StationSerializer


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

from django.urls import path
from api.views import lines, line_add, line_detail, cities, city_detail, city_add, stations, station_detail, station_add

urlpatterns = [
    path('lines/', lines, name='lines'), 
    path('lines/create/', line_add, name='line_add'),
    path('lines/<int:line_id>/', line_detail, name='line_detail'),

    path('cities/', cities, name='cities'),
    path('cities/create/', city_add, name='city_add'),
    path('cities/<int:city_id>/', city_detail, name='city_detail'),

    path('stations/', stations, name='stations'),
    path('stations/create/', station_add, name='station_add'),
    path('stations/<int:station_id>/', station_detail, name='station_detail'),
]

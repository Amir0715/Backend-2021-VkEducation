from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView
from api.views import lines, line_add, line_detail, cities, city_detail, city_add, stations, station_detail, station_add, CityViewSet
from rest_framework.routers import DefaultRouter

from api import views as api_views 

router = DefaultRouter()
router.register(r'cities', api_views.CityViewSet, basename='cities')
router.register(r'lines', api_views.LineViewSet, basename='lines')
router.register(r'stations', api_views.StationViewSet, basename='stations')

urlpatterns = [
    # path('lines/', lines, name='lines'), 
    # path('lines/create/', line_add, name='line_add'),
    # path('lines/<int:line_id>/', line_detail, name='line_detail'),

    # path('cities/', cities, name='cities'),
    # path('cities/create/', city_add, name='city_add'),
    # path('cities/<int:city_id>/', city_detail, name='city_detail'),

    # path('stations/', stations, name='stations'),
    # path('stations/create/', station_add, name='station_add'),
    # path('stations/<int:station_id>/', station_detail, name='station_detail'),
    path('', include(router.urls)),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

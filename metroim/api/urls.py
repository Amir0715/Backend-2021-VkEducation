from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter

from api import views as api_views

router = DefaultRouter()
router.register(r'cities', api_views.CityViewSet, basename='cities')
router.register(r'lines', api_views.LineViewSet, basename='lines')
router.register(r'stations', api_views.StationViewSet, basename='stations')


urlpatterns = [
    path('', include(router.urls)),
    path('', include('user.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

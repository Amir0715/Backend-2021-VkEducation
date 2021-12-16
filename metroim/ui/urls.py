from django.urls import path
from ui import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from ui.viewsets import StationDocumentView

router = DefaultRouter()
station = router.register(r'station', StationDocumentView, basename='station_document')

urlpatterns = [
    path('', views.index, name='index'),
    url(r'search/', include(router.urls)),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

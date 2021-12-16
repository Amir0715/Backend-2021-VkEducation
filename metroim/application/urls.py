from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('ui.urls')),
]

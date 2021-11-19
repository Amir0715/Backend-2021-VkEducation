from django.urls import path
from api.views import lines, line_add, line_detail

urlpatterns = [
    path('lines/', lines, name='lines'), 
    path('lines/create/', line_add, name='line_add'),
    path('lines/<int:line_id>/', line_detail, name='line_detail'),
]

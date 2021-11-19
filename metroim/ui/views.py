from django.shortcuts import render
from api.views import get_line

def index(request): 
    return render(request, 'index.html', {'lines': get_line()})
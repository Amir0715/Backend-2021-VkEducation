from django.shortcuts import render

from ui.models import Line

def index(request): 
    return render(request, 'index.html', {'lines': Line.objects.all()})

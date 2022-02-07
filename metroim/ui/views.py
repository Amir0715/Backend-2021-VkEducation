from django.shortcuts import redirect, render
from django.contrib.auth import logout

from ui.models import Line

def index(request): 
    return render(request, 'index.html', {'lines': Line.objects.all()})

def login(request): 
    return render(request, 'login.html')

def logout_view(request):
    logout(request);
    return render(request, 'logout.html')
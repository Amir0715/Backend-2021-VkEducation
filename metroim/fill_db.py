import os
import sys
import django
from django.template.defaultfilters import slugify
import json

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
    django.setup()

    from ui.models import City, Line, Station
    

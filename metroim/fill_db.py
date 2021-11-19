import os
import sys
import django
from django.template.defaultfilters import slugify
import json

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
    django.setup()

    from ui.models import City, Line, Station
    print('clean database')
    City.objects.all().delete()	
    Line.objects.all().delete()	
    Station.objects.all().delete()

    with open('api/stations.json') as f:
        data = json.load(f)
        for city in data:
            city_obj = City.objects.create(name=city["name"])
            city_obj.save()
            print(f'{city_obj.name} был создан!')
            for line in city["lines"]:
                line_obj = Line.objects.create(name=line["name"], city=city_obj, hex_color=line['hex_color'])
                line_obj.save()
                print(f"\t{line_obj.name} был создан!")
                for station in line["stations"]:
                    station_obj = Station.objects.create(
                        name=station["name"],
                        latitude=station["lat"], 
                        longitude=station["lng"], 
                        order=station["order"], 
                        line=line_obj
                    )
                    print(f"\t\tСтанция {station_obj.name} была создана! ")
                    station_obj.save()

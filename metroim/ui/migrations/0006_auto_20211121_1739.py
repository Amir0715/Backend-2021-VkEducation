# Generated by Django 3.2.9 on 2021-11-21 17:39

from django.db import migrations

import json
import os
from django.conf import settings

def fill_db(apps, shema_editor):
    City = apps.get_model('ui', 'City')
    Line = apps.get_model('ui', 'Line')
    Station = apps.get_model('ui', 'Station')

    print('clean database')
    City.objects.all().delete()	
    Line.objects.all().delete()	
    Station.objects.all().delete()
    filepath = os.path.join(settings.BASE_DIR, 'stations.json')
    with open(filepath) as f:
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


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0005_alter_station_order'),
    ]

    operations = [
        migrations.RunPython(fill_db),
    ]

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from ui.models import City, Line, Station


# TODO: добавить логику редактирование объектов

@csrf_exempt
@require_GET
def lines(request):
    lines = Line.objects.all()
    return JsonResponse(list(lines.values()), safe=False)


@csrf_exempt
@require_http_methods(['DELETE', 'GET', 'PUT'])
def line_detail(request, line_id):
    try:
        line = Line.objects.get(id=line_id)
    except Line.DoesNotExist:
        return JsonResponse({"error": f"Линии с id {line_id} нет в базе!"}, status=404)

    if request.method == "GET":
        return JsonResponse({
            'id': line.id,
            'name': line.name,
            'stations': list(line.stations.all().values())
        })

    elif request.method == "DELETE":
        line.delete()
        return JsonResponse({"message": "Линия успешно удалена!"})
    



@csrf_exempt
@require_POST
def line_add(request):
    data = json.loads(request.body)
    if len(list(set(['name', 'hex_color', 'city_id']) & set(data.keys()))) == 3:
        try:
            city = City.objects.get(id=data['city_id'])
        except City.DoesNotExist:
            return JsonResponse({"error": f"Города с id {data['city_id']} нет в базе!"}, status=400)

        line = Line.objects.create(name=data['name'],
                            hex_color=data['hex_color'],
                            city=city)

        return JsonResponse({
            "message": "Линия успешно создана!", 
            "data": {
                "id": line.id,
                "name": line.name,
                "hex_color": line.hex_color,
                "city": {
                    "id": city.id,
                    "name": city.name,                     
                }
            }
        })

    return JsonResponse({"error": "Недостаточно ключей"}, status=400)


@csrf_exempt
@require_GET
def cities(request):
    cities = City.objects.all()
    return JsonResponse(list(cities.values()), safe=False)


@csrf_exempt
@require_http_methods(['DELETE', 'GET'])
def city_detail(request, city_id):
    try:
        city = City.objects.get(id=city_id)
    except City.DoesNotExist:
        return JsonResponse({"error": f"Города с id {city_id} нет в базе!"}, status=404)

    if request.method == "GET":
        JsonResponse({
            'id': city.id, 
            'name': city.name, 
            'lines': list(city.lines.all().values())})

    elif request.method == "DELETE":
        city.delete()
        return JsonResponse({"message": "Город успешно удален!"})


@csrf_exempt
@require_POST
def city_add(request):
    data = json.loads(request.body)
    if 'name' in data:
        city = City.objects.create(name=data['name'])
        return JsonResponse(
            {
                "message": "Город успешно создан!", "data": {
                    "id": city.id,
                    "name": city.name
                }
            }
        )

    return JsonResponse({"error": "Недостаточно ключей"}, status=400)


@csrf_exempt
@require_GET
def stations(request):
    Stations = Station.objects.all()
    return JsonResponse(list(Stations.values()), safe=False)


@csrf_exempt
@require_http_methods(['DELETE', 'GET'])
def station_detail(request, station_id):
    try:
        station = Station.objects.get(id=station_id)
    except Station.DoesNotExist:
        return JsonResponse({"error": f"Станции с id {station_id} нет в базе!"}, status=404)

    if request.method == "GET":
        return JsonResponse({
                'id': station.id,
                'name': station.name,
                'order': station.order,
                'latitude': station.latitude,
                'longitude': station.longitude,
                'line': {
                    'id': station.line.id,
                    'name': station.line.name,
                    'hex_color': station.line.hex_color,
                    'city': {
                        'id': station.line.city.id,
                        'name': station.line.city.name,
                    }
                }
            })

    elif request.method == "DELETE":
        station.delete()
        return JsonResponse({"message": "Станция успешно удалена!"})

@csrf_exempt
@require_POST
def station_add(request):
    data = json.loads(request.body)
    if len(list(set(['name', 'order', 'latitude', 'longitude', 'line_id']) & set(data.keys()))) == 5:
        try:
            line = Line.objects.get(id=data['line_id'])
        except Line.DoesNotExist:
            return JsonResponse({"error": f"Линии с id {data['line_id']} нет в базе!"}, status=404)
        
        station = Station.objects.create(
            name=data['name'],
            order=data['order'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            line=line
        )
        return JsonResponse({
                "message": "Станция успешно создана!", 
                "data": {
                    "id": station.id,
                    "name": station.name,
                    "order": station.order,
                    "latitude": station.latitude,
                    "longitude": station.longitude,
                    "line": {
                        "id": line.id,
                        "name": line.name,
                        "hex_color": line.hex_color,
                        "city": {
                            "id": line.city.id,
                            "name": line.city.name,
                        }
                    }
                }
            })

    return JsonResponse({"error": "Недостаточно ключей"}, status=400)
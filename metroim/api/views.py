import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from api.decorators import require_body
from ui.models import City, Line, Station
from rest_framework import viewsets
from api.serializers import CitySerializer, LineSerializer, StationSerializer


@csrf_exempt
@require_GET
def lines(request):
    lines = Line.objects.all()
    return JsonResponse(list(lines.values()), safe=False)


@csrf_exempt
@require_http_methods(['DELETE', 'GET', 'PUT'])
@require_body('PUT', ['name', 'hex_color', 'city_id'])
def line_detail(request, line_id):
    try:
        line = Line.objects.get(id=line_id)
    except Line.DoesNotExist:
        # Если объект не найден
        return JsonResponse({"error": f"Линии с id {line_id} нет в базе!"}, status=404)

    if request.method == "GET":
        return JsonResponse({
            'id': line.id,
            'name': line.name,
            'hex_color': line.hex_color,
            'stations': list(line.stations.all().values())
        })

    elif request.method == "DELETE":
        line.delete()
        return JsonResponse({"message": "Линия успешно удалена!"})

    elif request.method == "PUT":
        # Если объект существует, то нужно изменить объект
        data = json.loads(request.body)
        line.name = data['name']
        line.hex_color = data['hex_color']

        try:
            city = City.objects.get(id=data['city_id'])
        except City.DoesNotExist:
            return JsonResponse({"error": f"Города с id {data['city_id']} нет в базе!"}, status=400)

        line.city = city
        line.save()
        return JsonResponse({
            'id': line.id,
            'name': line.name,
            'hex_color': line.hex_color,
            'city': {
                'id': line.city.id,
                'name': line.city.name
            },
            'stations': list(line.stations.all().values())
        })


@csrf_exempt
@require_POST
@require_body('POST', ['name', 'hex_color', 'city_id'])
def line_add(request):
    data = json.loads(request.body)
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


@csrf_exempt
@require_GET
def cities(request):
    cities = City.objects.all()
    return JsonResponse(list(cities.values()), safe=False)


@csrf_exempt
@require_http_methods(['DELETE', 'GET', 'PUT'])
@require_body('PUT', ['name'])
def city_detail(request, city_id):
    try:
        city = City.objects.get(id=city_id)
    except City.DoesNotExist:
        return JsonResponse({"error": f"Города с id {city_id} нет в базе!"}, status=404)

    if request.method == "GET":
        return JsonResponse({
            'id': city.id,
            'name': city.name,
            'lines': list(city.lines.all().values())})

    elif request.method == "DELETE":
        city.delete()
        return JsonResponse({"message": "Город успешно удален!"})

    elif request.method == "PUT":
        # Если объект существует, то нужно изменить объект
        data = json.loads(request.body)
        city.name = data['name']
        city.save()
        return JsonResponse({
            'id': city.id,
            'name': city.name,
            'lines': list(city.lines.all().values())
        })


@csrf_exempt
@require_POST
@require_body('POST', ['name'])
def city_add(request):
    data = json.loads(request.body)
    city = City.objects.create(name=data['name'])
    return JsonResponse({
        "message": "Город успешно создан!",
        "data": {
            "id": city.id,
            "name": city.name
        }
    })


@csrf_exempt
@require_GET
def stations(request):
    Stations = Station.objects.all()
    return JsonResponse(list(Stations.values()), safe=False)


@csrf_exempt
@require_http_methods(['DELETE', 'GET', 'PUT'])
@require_body('PUT', ['name', 'order', 'latitude', 'longitude', 'line_id'])
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

    elif request.method == "PUT":
        data = json.loads(request.body)
        try:
            line = Line.objects.get(id=data['line_id'])
        except Line.DoesNotExist:
            return JsonResponse({"error": f"Линии с id {data['line_id']} нет в базе!"}, status=404)

        station.name = data['name']
        station.order = data['order']
        station.latitude = data['latitude']
        station.longitude = data['longitude']
        station.line = line
        station.save()

        return JsonResponse({
            "message": "Станция успешно изменена!",
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


@csrf_exempt
@require_POST
@require_body('POST', ['name', 'order', 'latitude', 'longitude', 'line_id'])
def station_add(request):
    data = json.loads(request.body)
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


class CityViewSet(viewsets.ModelViewSet):
    '''
    '''

    serializer_class = CitySerializer
    queryset = City.objects.all()

class LineViewSet(viewsets.ModelViewSet):
    '''
    '''

    serializer_class = LineSerializer
    queryset = Line.objects.all()

class StationViewSet(viewsets.ModelViewSet):
    '''
    '''

    serializer_class = StationSerializer
    queryset = Station.objects.all()
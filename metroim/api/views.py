import json
from django.http import JsonResponse
from django.http.response import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

def get_line(line_id=None):
    # TODO: добавить в базу данных 
    # пока нет базы данных
    with open('api/stations.json') as f:
        data = json.load(f)
        if line_id:
            lines = data['lines']
            f = filter(lambda line: line["id"] == line_id, lines)
            for line in lines:
                if int(line['id']) == line_id:
                    return line
            return {"message":"Ветки метро с таким id не существует.", "status": "error"}
        else:
            return data

@csrf_exempt
def lines(request):
    if request.method == 'GET':
        return JsonResponse(get_line())
    else: 
        return HttpResponseNotAllowed(['GET']) 

@csrf_exempt
def line_detail(request, line_id):
    if request.method == 'GET':
        return JsonResponse(get_line(line_id))
    else: 
        return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def line_add(request):
    # CSRF токена нет в ответном куках
    if request.method == 'POST':
        return JsonResponse({"message":"Линия успешно создана!"})
    else: 
        return HttpResponseNotAllowed(['POST'])

import json
from django.http import JsonResponse
from django.http.response import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods

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
@require_GET
def lines(request):
    return JsonResponse(get_line())

@csrf_exempt
@require_GET
def line_detail(request, line_id):
    return JsonResponse(get_line(line_id))

@csrf_exempt
@require_POST
def line_add(request):
    return JsonResponse({"message":"Линия успешно создана!"})
    

import json
from functools import wraps
from json.decoder import JSONDecodeError
from typing import List

from django.http.response import JsonResponse


def require_body(method: str, require_keys: List[str]):
    """
    A decorator that checks for the presence of the required fields in 
    the request body for the specified method. Usage::

        @require_http_methods('POST', ['name', 'id'])
        def my_view(request):
            # ...

    """
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if request.method == method:
                # проверяем на наличия для указоного метода
                if not request.body:
                    return JsonResponse({"error": "Недостаточно ключей"}, status=400)

                try:
                    data = json.loads(request.body)
                except JSONDecodeError:
                    return JsonResponse({"error": "Неправильное тело запроса"}, status=400)

                # ищем пересечение
                cross = set(require_keys) & set(data.keys())

                # необходимые поля в теле запросе отсутствуют
                if len(cross) != len(require_keys):
                    return JsonResponse({"error": "Недостаточно ключей"}, status=400)

            return func(request, *args, **kwargs)
        return inner
    return decorator




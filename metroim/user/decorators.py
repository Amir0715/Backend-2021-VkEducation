from functools import wraps

from django.http.response import HttpResponseRedirect, JsonResponse
from rest_framework.request import Request

def login_required(func):
    """
    A decorator that checks login user. Usage::

        @require_http_methods
        def my_view(request):
            # ...

    """
    @wraps(func)
    def inner(*args, **kwargs):
        is_authenticated = False
        if isinstance(args[0], Request):
            is_authenticated = args[0].user.is_authenticated
        else:
            is_authenticated = args[1].user.is_authenticated
        if not is_authenticated:
            return HttpResponseRedirect('/login/')
        return func(*args, **kwargs)
    return inner

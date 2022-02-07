import json
from datetime import datetime

def app(environ, start_response):
    data = json.dumps({'time': datetime.now().time().isoformat(), 'url': None}).encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'application/json; charset=utf-8'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
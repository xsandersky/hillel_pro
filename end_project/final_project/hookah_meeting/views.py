import json

from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps({"massage": "hello"}))

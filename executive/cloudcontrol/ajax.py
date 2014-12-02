from django.http import HttpResponse
from django.utils.html import strip_tags
import json
import requests

class storeout:
    def __init__(self, key):
        self.actions = {}
        self.key = key
    def save(self, value):
        self.actions[self.key] = value

def start_server(request):
    server_name = request.GET.get('server_name')
    server_response = '{"percent_complete": "' + '10' + '","status":"' + 'ok' + '"}'
    return HttpResponse(server_response, content_type='application/json')

def suspend_server(request):
    server_name = request.GET.get('server_name')
    return HttpResponse(server_response, content_type='application/json')

def stop_server(request):
    server_name = request.GET.get('server_name')
    server_response = '{"percent_complete": "' + '100' + '","status":"' + 'ok' + '"}' # Hardcoded to stop immediately with 100
    return HttpResponse(server_response, content_type='application/json')

def boost_server(request):
    server_name = request.GET.get('server_name')
    response = requests.get('http://localhost:8888/boost/vm-b8e95c38-b899-496e-bd6b-bcfec39fc52e', data=None)
    json_data = json.loads(response.text)
    server_response = '{"percent_complete": "' + str(json_data['progress']) + '","status":"' + 'ok' + '"}'
    return HttpResponse(server_response, content_type='application/json')

def deboost_server(request):
    server_name = request.GET.get('server_name')
    response = requests.get('http://localhost:8888/deboost/vm-b8e95c38-b899-496e-bd6b-bcfec39fc52e', data=None)
    json_data = json.loads(response.text)
    server_response = '{"percent_complete": "' + str(json_data['progress']) + '","status":"' + 'ok' + '"}'
    return HttpResponse(server_response, content_type='application/json')
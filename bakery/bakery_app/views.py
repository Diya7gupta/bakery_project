from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from . import services
import json

# Create your views here.
inventory_service = services.InventoryService()
bakery_service = services.BakeryService()

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def inventory(request):
    print('Inventory reqeust received')
    if request.method == 'PUT':
        request_json = get_request_json(request)
        inventory_service.createInventoryItem(request_json['name'], request_json['quantity'], request_json['price'])
        return get_empty_success_response()
    elif request.method == 'POST':
        request_json = get_request_json(request)
        inventory_service.updateInventoryItem(request_json['name'], request_json['quantity'], request_json['price'])
        return get_empty_success_response()
    elif request.method == 'GET':
        prefix = request.GET.get('prefix', '')
        matching_items = inventory_service.searchInventoryItemByPrefix(prefix)

        # Convert the matching items to a list of dictionaries for JSON response
        response_data = [{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'price': str(item.price)} for item in matching_items]
        return get_success_response(response_data)
    else:
        raise Http404("Method not found.")

@csrf_exempt
def bakery(request):
    print('Bakery request received')
    if request.method == 'PUT':
        request_json = get_request_json(request)
        bakery_service.createBakeryItem(request_json)
        return get_empty_success_response()
    elif request.method == 'GET':
        prefix = request.GET.get('prefix', '')
        matching_items = bakery_service.searchBakeryItemByPrefix(prefix)

        response_data = [{'id': item.id, 'name': item.name, 'quantity': item.quantity} for item in matching_items]
        return get_success_response(response_data)
    else:
        raise Http404("Method not found.")
    
def get_request_json(request):
    request_json = json.loads(request.body)
    print(request_json)
    return request_json

def get_empty_success_response():
    return JsonResponse({
            'success': True
        })

def get_success_response(data):
    return JsonResponse({
            'success': True,
            'data': data
        })
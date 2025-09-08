from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    
    '''
    GET
    print(f"This is GET request:{request.GET}")
    print(f"This is POST request: {request.POST}")
    body = request.body
    data = {}
    try:
        data = json.loads(body)  # converts JSON data to a dictionary
    except:
        pass

    print(f"DATA: {data}")
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    '''
    
    '''
    Model Instace

    We basically have data in the form of rows, the problem is we cannot directly return a model instance as JSON
    so we use serialization where we convert the model instance to a dictionary and then return it as JSON

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        #data = model_to_dict(model_data)
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])  # we can specify the fields we want to return

    return JsonResponse(data)
    '''

    '''
    Django REST Framework

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])  # we can specify the fields we want to return
    return Response(data)
    '''

    '''
    Django REST Framework with Serializer
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance=instance).data
    return Response(data)
    '''

    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)

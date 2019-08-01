from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import DealSerializer, AirportSerializer
from .models import Deal, Airport

@api_view(['GET'])
def get_deals(request):
    '''
        GET: returns a list of deals
    '''

    if request.method == 'GET':
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_history(request, departure_airport, arrival_airport):
    '''
        GET: returns a history of a flight between two given airports
    '''

    if request.method == 'GET':
        deals = Deal.objects.filter(departure_airport__name=departure_airport, arrival_airport__name=arrival_airport).order_by('-created')
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)
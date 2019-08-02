from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import DealSerializer, AirportSerializer
from .models import Deal, Airport

@csrf_exempt
@api_view(['GET'])
def get_deals(request):
    '''
        GET: returns a list of active deals
    '''

    if request.method == 'GET':
        deals = Deal.objects.filter(is_active=True)
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def get_history(request, deal_id):
    '''
        GET: returns a history of a flight between two given airports. Order by date created.
    '''

    if request.method == 'GET':
        deal = Deal.objects.get(pk=deal_id)
        deals = Deal.objects.filter(departure_airport__name=deal.departure_airport, arrival_airport__name=deal.arrival_airport).order_by('-created')
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)
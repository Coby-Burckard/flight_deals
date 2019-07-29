from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

from .serializers import DealSerializer, AirportSerializer
from .models import Deal, Airport

@csrf_exempt
def get_deals(request):
    '''
        GET: returns a list of deals
        POST: scrapes the delta page for deals and updates the database.
    '''

    if request.method == 'GET':
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return JsonResponse(serializer.data, safe=False)

def verify_deal(deal):
    '''
        verifies the components of the deal, and updates necessary information in the database.
    '''
    pass

def verify_airport(airport):
    '''
        verifies that an airport exists and adds one to the database if not.
    '''
    pass

def check_delta():
    '''
        calls api from delta and up
    '''
    pass
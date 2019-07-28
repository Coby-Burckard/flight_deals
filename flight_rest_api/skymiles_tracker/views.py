from django.shortcuts import render
from django.views.decorators.csfr import csfr_exempt
from rest_framework.parsers import JSONParser

from .serializers import DealSerializer, AirportSerializer
from .models import Deal, Airport

@csfr_exempt
def get_deals(request):
    '''
        GET: returns a list of deals
        POST: scrapes the delta page for deals and updates the database.
    '''

def verify_deal(deal):
    '''
        verifies the components of the deal, and updates necessary information in the database.
    '''

def verify_airport(airport):
    '''
        verifies that an airport exists and adds one to the database if not.
    '''

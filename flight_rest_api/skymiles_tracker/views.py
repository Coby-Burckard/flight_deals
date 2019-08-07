from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .serializers import DealSerializer, AirportSerializer
from .models import Deal, Airport

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'active deals': reverse('active_deals', request=request, format=format),
        'deal history': reverse('deal_history', request=request, format=format)
    })

@api_view(['GET'])
def get_deals(request, format=None):
    '''
        GET: returns a list of active deals
    '''

    if request.method == 'GET':
        deals = Deal.objects.filter(is_active=True)
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_history(request, format=None):
    '''
        GET: returns a history of a flight between two given airports. Order by date created.
    '''

    if request.GET.get('departure') and request.GET.get('arrival'):
        arrival_airport = get_object_or_404(Airport, name=request.GET.get('arrival'))
        departure_airport = get_object_or_404(Airport, name=request.GET.get('departure'))
        deals = Deal.objects.filter(departure_airport__name=departure_airport.name, arrival_airport__name=arrival_airport.name).order_by('-created')
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)
    else: 
        return JsonResponse({'history': 'None Son'})
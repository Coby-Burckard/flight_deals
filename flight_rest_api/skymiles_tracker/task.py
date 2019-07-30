from background_task import background
import time
import requests
import json
import re

from .models import Airport, Deal

@background()
def check_delta():
    url = 'https://delta-api.xcheck.co/v1/c0003bf785?points=Y'
    routes_list = json.loads(requests.get(url).text)['routes']

    for route in routes_list:
        check_airports(route)
        check_deals(route)

    return None

def check_airports(route):
    airports = Airport.objects.all()
    new_arrival_airport = Airport(name=route['destination_queried'])
    new_departure_airport = Airport(name=route['origin_queried'])
    if new_arrival_airport in airports:
        print(new_arrival_airport.name, ' in database')
    else:
        print(new_arrival_airport, ' not in database')
        new_arrival_airport.save()
    if new_departure_airport in airports:
        print(new_departure_airport.name, ' in database')
    else:
        print(new_departure_airport.name, ' not in database')
        new_departure_airport.save()
    return None

def check_deals(route):
    # need to fix deals being replicated in the db... 
    all_deals = Deal.objects.all()
    active_deals = Deal.objects.filter(is_active=True)
    new_deal = Deal(
        departure_airport = Airport.objects.get(name=route['origin_queried']),
        arrival_airport = Airport.objects.get(name=route['destination_queried']),
        miles = int(''.join(re.findall('[0-9]*',route['products']['points']['price']))),
        start_date = convert_date_format(route['travel_date_start']),
        end_date = convert_date_format(route['travel_date_end']),
        is_active = True,
        dollars = int(''.join(re.findall('[0-9]*', route['price']))),
    )
    if new_deal in all_deals:
        print(new_deal, ' in db')
    else:
        print(new_deal, ' not in db')
        new_deal.save()
    
    return None

def convert_date_format(date):
    date_list = re.findall('[0-9]+', date)
    converted_date = '-'.join([date_list[2], date_list[0], date_list[1]])
    print(converted_date)
    return(converted_date)
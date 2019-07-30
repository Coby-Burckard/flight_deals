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
    new_deal_list = []

    for route in routes_list:
        check_airports(route)
        new_deal_list.append(check_deals(route))
    
    deactivate_old_deals(new_deal_list)

    return None

def check_airports(route):
    airports = Airport.objects.all()
    new_arrival_airport = Airport(name=route['destination_queried'])
    new_departure_airport = Airport(name=route['origin_queried'])
    if new_arrival_airport in airports:
        pass
    else:
        new_arrival_airport.save()
    if new_departure_airport in airports:
        pass
    else:
        new_departure_airport.save()
    return None

def check_deals(route):
    # need to fix deals being replicated in the db... Maybe has to do with airports not being linked until rerunning site
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
    return new_deal

def convert_date_format(date):
    date_list = re.findall('[0-9]+', date)
    converted_date = '-'.join([date_list[2], date_list[0], date_list[1]])
    return(converted_date)

def deactivate_old_deals(new_deal_list):
    active_deals = Deal.objects.filter(is_active = True)

    for active_deal in active_deals:
        if active_deal in new_deal_list:
            pass 
        else:
            active_deal.is_active = False
            active_deal.save()
            print('deactivated ', active_deal)
    
    return None

from background_task import background
import time
import requests
import json

@background()
def check_delta():
    url = 'https://delta-api.xcheck.co/v1/c0003bf785?points=Y'
    routes_list = json.loads(requests.get(url).text)['routes']
    for route in routes_list:
        print(route['od_pairs_returned'])
    return ''
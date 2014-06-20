import json

import requests

from common import CAMPSITES


URL = 'https://www.att.com/apis/maps/v2/locator/search/viewport.json'

ALL_APS = {}

for name, coords in CAMPSITES.items():
    lat, lng = coords
    params = {
        'apikey': '27d684f8e73c701f4e41b334813b54cf3c7fa46d',
        'channels': 'wifibasic',
        'ne': '%.15f,%.15f' % (lat + 0.5, lng + 0.5),
        'origin': '%.15f,%.15f' % (lat, lng),
        'sw': '%.15f,%.15f' % (lat - 0.5, lng - 0.5),
        'poi_types': 'wifi',
        'select': (
            'id,name,notes,services,phone,channel,address1,'
            'address2,addr_hint,city,postal,region,lon,lat,hours,ssid'
        ),
    }
    request = requests.get(URL, params=params)
    for result in request.json()['results']:
        ALL_APS[result['id']] = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    result['lon'],
                    result['lat']
                ]
            },
            'properties': {
                'title': result['name'],
                'address': result['address1'],
                'city': result['city'],
                'ssid': result['ssid'],
                'id': result['id'],
                'category': 'attwifi',
            }
        }

print json.dumps({
    'type': 'FeatureCollection',
    'features': ALL_APS.values()
}, indent=4)

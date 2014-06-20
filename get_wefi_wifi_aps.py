import json

import requests

from common import CAMPSITES

URL = 'http://www.wefi.com/maps/data.ajax.php'

ALL_APS = {}

for name, coords in CAMPSITES.items():
    lat, lng = coords
    data = {
        'data': json.dumps({
            'action': 1,
            'lat': coords[0],
            'lng': coords[1],
            'radius': 20000,
            'zoom': 14,
        })
    }
    request = requests.post(URL, data=data)
    result = request.json()
    if not result:
        continue
    for result in result['aps']:
        ALL_APS[result['CNRID']] = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    float(result['long']),
                    float(result['lat']),
                ]
            },
            'properties': {
                'title': result['apName'],
                'address': result['geoInfo'].get('Street', ''),
                'city': result['geoInfo'].get('City', ''),
                'ssid': result['SSID'],
                'id': result['CNRID'],
                'category': 'wefiwifi',
            }
        }

print json.dumps({
    'type': 'FeatureCollection',
    'features': ALL_APS.values()
}, indent=4)

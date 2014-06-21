import json

from fastkml import kml
import requests
from shapely.geometry import Point

from common import CAMPSITES, format_description, format_document

URL = 'http://www.wefi.com/maps/data.ajax.php'
ALL_APS = {}

kml_file = kml.KML()
ns = {}
document = kml.Document(
    id='wefiwifi',
    name='WeFi APs',
    description='List of WeFi Access Points',
)
kml_file.append(document)

for name, data in CAMPSITES.items():
    coords = data['coordinates']
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
    result_json = request.json()
    if not result_json:
        continue
    all_aps = result_json['aps']
    if isinstance(all_aps, dict):
        all_aps = [all_aps]
    for result in all_aps:
        placemark = kml.Placemark(
            id=result['CNRID'],
            name=result['apName'],
            description=format_description(
                """
                {title} [{ssid}]
                {address}, {city}

                (Source: WeFi)
                """,
                title=result['apName'] if result['apName'] else result['CNRID'],
                ssid=result['SSID'],
                address=result['geoInfo'].get('Street', 'Unknown Address'),
                city=result['geoInfo'].get('City', 'Unknown City'),
            ),
            styleUrl='#BookmarkStyle_25'
        )
        placemark.geometry = Point(
            float(result['long']),
            float(result['lat'])
        )
        ALL_APS[result['CNRID']] = placemark

for placemark in ALL_APS.values():
    document.append(placemark)

print format_document(kml_file)

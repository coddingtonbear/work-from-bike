from fastkml import kml
import requests
from shapely.geometry import Point

from common import CAMPSITES, format_description, format_document


URL = 'https://www.att.com/apis/maps/v2/locator/search/viewport.json'
ALL_APS = {}

kml_file = kml.KML()
ns = {}
document = kml.Document(
    id='attwifi',
    name='AT&T Wifi APs',
    description='List of AT&T Wifi Access Points',
)
kml_file.append(document)

for name, data in CAMPSITES.items():
    coords = data['coordinates']
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
        placemark = kml.Placemark(
            id=result['id'],
            name=result['name'],
            description=format_description(
                """
                {title} [{ssid}]
                {address}, {city}

                (Source: AT&T)
                """,
                title=result['name'],
                ssid=result['ssid'],
                address=result['address1'],
                city=result['city'],
            ),
            styleUrl='#BookmarkStyle_25',
        )
        placemark.geometry = Point(result['lon'], result['lat'])
        ALL_APS[result['id']] = placemark

for placemark in ALL_APS.values():
    document.append(placemark)

print format_document(kml_file)

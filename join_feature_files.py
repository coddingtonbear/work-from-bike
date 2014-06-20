import json
import sys


ALL_FEATURES = []


for filename in sys.argv[1:]:
    with open(filename, 'r') as datafile:
        data = json.loads(datafile.read())
        ALL_FEATURES.extend(data['features'])

print json.dumps({
    'type': 'FeatureCollection',
    'features': ALL_FEATURES
}, indent=4)

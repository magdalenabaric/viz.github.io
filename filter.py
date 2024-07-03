import json

with open('00-20.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

keys_to_remove = ['alert', 'code', 'tz', 'url', 'detail', 'mmi', 'status', 'tsunami',
                  'sig', 'net', 'ids', 'sources', 'types', 'nst', 'dmin', 'rms', 'gap', 'magType', 'cdi', 'felt']

for feature in data['features']:
    for key in keys_to_remove:
        if key in feature['properties']:
            del feature['properties'][key]

with open('updated_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

import json
import re


with open('data.json') as f:
    data = json.loads(f.read())


for date in data['run']:
    if date[:4] == '2022':
        for text in data['run'][date][0].split('\n'):
            if '*' in text:
                if 'через' in text:
                    pass
                else:
                    pass
            else:
                distance_km = sum([int(x) for x in re.findall(r'(\d+)\s?км', text)])
                distance_m = sum([int(x) for x in re.findall(r'(\d+)\s?м', text)])
            print(text, distance_km, distance_m)
import json

import requests

tmp = [{'id': 'id11', 'title': ['apple', 'banana']}]
headers = {
    'Content-type': 'application/json', 'Accept': 'application/json'
}
r = requests.post('http://localhost:8983/solr/gettingstarted/update?commit=true', headers=headers, data=json.dumps(tmp))
print(r)

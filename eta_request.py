import requests

data = {'route': [100, 200, 300],
        'avgSpeed': "20"
}
url = "http://localhost:8080/calculate_eta"

r = requests.post(url, json=data)

print(r.json())
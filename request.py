import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'attenuation':2})

print(r.json())
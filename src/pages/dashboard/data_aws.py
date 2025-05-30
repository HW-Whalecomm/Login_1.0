import requests
import json

request = requests.get('https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/consulta')

data = request.json()

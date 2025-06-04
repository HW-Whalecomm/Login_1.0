import requests
import json




dummy_data={}

def request_data():
   global dummy_data



   medidores = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/consulta")
   lectura = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/lectura")
   status = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/status")

   medidores = json.loads(medidores.text)
   lectura = json.loads(lectura.text)
   status = json.loads(status.text)

   ids = list(medidores.keys())

   for medidor in ids:
      if medidor in lectura:
         dummy_data[medidor]={
               "id":medidor,
               "cuenta": medidores[medidor]['cuenta'],
               "titular": medidores[medidor]['titular'],
               "lectura":lectura[medidor]['lectura'],
               "batería":lectura[medidor]['bateria'],
               "direccion": medidores[medidor]['direccion'],
               "ubicacion":medidores[medidor]['ubicacion']
               }
      else:
         dummy_data[medidor]={
               "id":medidor,
               "cuenta": medidores[medidor]['cuenta'],
               "titular": medidores[medidor]['titular'],
               "lectura":"--",
               "batería":"--",
               "direccion": medidores[medidor]['direccion'],
               "ubicacion":medidores[medidor]['ubicacion']
               }
      if medidor in status:
         dummy_data[medidor]['status']=status[medidor]['status']
      else:
         dummy_data[medidor]['status']="--"


   print(dummy_data)

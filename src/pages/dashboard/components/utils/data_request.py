import requests
import json
import datetime

medidores_data={}
medidores_corte={}


def corte_periodo():
   global medidores_corte

   fecha = datetime.datetime.now()
   fecha = str(fecha)
   fecha_corte = fecha.split()

   periodo = {
      "periodo": fecha_corte[0],
      "hora": fecha_corte[1]
   }

   headers = {'Content-type': 'application/json'}
   
   cortes = requests.post("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/corte", json = periodo, headers=headers)
   cortes = json.loads(cortes.text)
   medidores_corte = cortes

   #print(medidores_corte)


def request_data():
   global medidores_data



   medidores = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/consulta")
   lectura = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/lectura")
   status = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/status")

   medidores = json.loads(medidores.text)
   lectura = json.loads(lectura.text)
   status = json.loads(status.text)

   ids = list(medidores.keys())

   for medidor in ids:
      if medidor in lectura:
         fecha = str(datetime.datetime.fromtimestamp(int(lectura[medidor]['timestamp'])/1000))
         medidores_data[medidor]={
               "id":medidor,
               "cuenta": medidores[medidor]['cuenta'],
               "titular": medidores[medidor]['titular'],
               "lectura":lectura[medidor]['lectura'],
               "fecha":fecha,
               "batería":lectura[medidor]['bateria'],
               "direccion": medidores[medidor]['direccion'],
               "ubicacion":medidores[medidor]['ubicacion']
               }
      else:
         medidores_data[medidor]={
               "id":medidor,
               "cuenta": medidores[medidor]['cuenta'],
               "titular": medidores[medidor]['titular'],
               "lectura":"--",
               "batería":"--",
               "direccion": medidores[medidor]['direccion'],
               "ubicacion":medidores[medidor]['ubicacion']
               }
      if medidor in status:
         medidores_data[medidor]['status']=status[medidor]['status']
      else:
         medidores_data[medidor]['status']="--"


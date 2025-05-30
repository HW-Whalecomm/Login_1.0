import requests
import json

medidores = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/consulta")
lectura = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/lectura")
status = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/status")

medidores = json.loads(medidores.text)
lectura = json.loads(lectura.text)
status = json.loads(status.text)

ids = list(medidores.keys())


dummy_data={}

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


""" ummy_data={
    0:{"encoder":"232006626",
       "cuenta":"04356",
       "consumo":46.8463,
       "status":"OK",
       "detalles":"Dashboard"},
    1:{"encoder":"232006627",
        "cuenta":"04357",
        "consumo":6.8463,
        "status":"OK",
        "detalles":"Dashboard"},
    2:{"encoder":"232006628",
       "cuenta":"04358",
       "consumo":12.6532,
       "status":"OK",
       "detalles":"Dashboard"},
    3:{"encoder":"232006629",
       "cuenta":"04359",
       "consumo":1.3114,
       "status":"OK",
       "detalles":"Dashboard"},
    4:{"encoder":"232006630",
       "cuenta":"04360",
       "consumo":23.6423,
       "status":"OK",
       "detalles":"Dashboard"},
    5:{"encoder":"232006631",
       "cuenta":"04361",
       "consumo":3.0987,
       "status":"OK",
       "detalles":"Dashboard"},
    6:{"encoder":"232006632",
       "cuenta":"04362",
       "consumo":0.6345,
       "status":"OK",
       "detalles":"Dashboard"},
    
} """
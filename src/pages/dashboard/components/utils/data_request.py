import requests
import json
import datetime

medidores_data={}
medidores_corte={}
medidores_historico={}
medidores_consumos = {}
medidor_historico = {}
medidor_historico_desor={}

mes ={
      "Ene":'01',
      "Feb":'02',
      "Mar":'03',
      "Abr":'04',
      "May":'05',
      "Jun":'06',
      "Jul":'07',
      "Ago":'08',
      "Sep":'09',
      "Oct":'10',
      "Nov":'11',
      "Dic":'12'
      }

mes_num ={
      "01":"Ene",
      "02":"Feb",
      "03":"Mar",
      "04":"Abr",
      "05":"May",
      "06":"Jun",
      "07":"Jul",
      "08":"Ago",
      "09":"Sep",
      "10":"Oct",
      "11":"Nov",
      "12":"Dic"
      }

def historicos():
   global medidores_historico
   global medidores_consumos
   aux_register = 0
   medidores = requests.get("https://nkldhxv7pi.execute-api.us-east-1.amazonaws.com/historicos")
   medidores = json.loads(medidores.text)
   medidores_consumos = medidores
   ids = list(medidores.keys())
   for encoder in ids:
      medidor_historico_desor[encoder]={}
      for periodo in medidores[encoder]:
         medidores_historico[aux_register]={
            "medidor":encoder,
            "cuenta": medidores_data[encoder]['cuenta'],
            "periodo":periodo,
            "fecha":medidores[encoder][periodo]["fecha"],
            "consumo":medidores[encoder][periodo]["consumo"],
            "inicio":medidores[encoder][periodo]["lec_inicio"],
            "corte":medidores[encoder][periodo]["lec_corte"]
                  }
         medidor_historico_desor[encoder][aux_register]={
            "periodo":periodo,
            "consumo":medidores[encoder][periodo]["consumo"],
            "inicio":medidores[encoder][periodo]["lec_inicio"],
            "corte":medidores[encoder][periodo]["lec_corte"]
         }
         aux_register = aux_register + 1
      consumo_meter={}
      for consumo in medidor_historico_desor[encoder]:
         datos_fecha = medidor_historico_desor[encoder][consumo]['periodo'].split('-')
         fecha = mes[datos_fecha[0]]+"/01/"+datos_fecha[1]
         datetime_object = datetime.datetime.strptime(fecha, '%m/%d/%y')
         consumo_meter[datetime_object]={
            "consumo":medidor_historico_desor[encoder][consumo]['consumo'],
            "inicio":medidor_historico_desor[encoder][consumo]['inicio'],
            "corte":medidor_historico_desor[encoder][consumo]['corte']
         }
      
      dic_ordenado = dict(sorted(consumo_meter.items()))
      consumos_ordenados={}
      aux_consumo=0
      for fechas in dic_ordenado:
         fecha_dic=(str(fechas)).split()
         fecha_dic=fecha_dic[0].split('-')
         fecha_con=mes_num[fecha_dic[1]]+"-"+fecha_dic[0]
         consumos_ordenados[aux_consumo]={"periodo":fecha_con,
                                          "consumo":consumo_meter[fechas]["consumo"],
                                          "inicio":consumo_meter[fechas]["inicio"],
                                          "corte":consumo_meter[fechas]["corte"]}
         aux_consumo=aux_consumo+1
         #consumos_ordenados[fecha_con]=consumo_meter[fechas]
      
      medidor_historico[encoder]=consumos_ordenados

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


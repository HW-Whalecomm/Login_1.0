import hashlib
import datetime
import pages.dashboard.components.utils.data_request as datos

usuario = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"  #admin
contraseña = "9b68500804a354c185a02f34c5773815ba9039b587ce079f1d9ecb91b75ac0dc"  #CSJ_2024.Wh
token=[]
def hash_verify(password,user):
    global token
    password = hashlib.sha256(password.encode()).hexdigest()
    user = hashlib.sha256(user.encode()).hexdigest()
    
    if (contraseña == password) and (usuario  == user):
        datos.request_data()
        datos.historicos()
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        token.append("WH_OK")
        token.append(timestamp)
        return True
    else:
        False 

#print(hash_password("admin"))
#print(hash_password("CSJ_2024.Wh"))
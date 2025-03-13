import hashlib

usuario = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"  #admin
contraseña = "9b68500804a354c185a02f34c5773815ba9039b587ce079f1d9ecb91b75ac0dc"  #CSJ_2024.Wh

def hash_verify(password,user):
    password = hashlib.sha256(password.encode()).hexdigest()
    user = hashlib.sha256(user.encode()).hexdigest()
    
    if (contraseña == password) and (usuario  == user):
        return True
    else:
        False 

#print(hash_password("admin"))
#print(hash_password("CSJ_2024.Wh"))
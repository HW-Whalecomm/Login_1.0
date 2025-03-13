import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

print(hash_password("admin"))
print(hash_password("CSJ_2024.Wh"))
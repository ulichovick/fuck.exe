import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from nuevo_usuario import Usuario
usu = input("Ingrese el nombre de usuario: \n")
pwwd = input("Ingrese la contraseña: \n")
pwwd_conf = input("Ingrese la contraseña de nuevo: \n")
while pwwd != pwwd_conf:
    print("las contraseñas no coinciden")
    pwwd = input("Ingrese la contraseña: \n")
    pwwd_conf = input("Ingrese la contraseña de nuevo: \n")

pwwd = str.encode(pwwd)
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = base64.urlsafe_b64encode(kdf.derive(pwwd))
f=Fernet(key)
test = Usuario(usu,key)
test.crear_usuario()
print("todo ok: ")


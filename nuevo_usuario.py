import base64
import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Usuario:
    def __init__ (self,nombre_usuario,password,salt):
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.salt = salt

    def ingresar(self):
        
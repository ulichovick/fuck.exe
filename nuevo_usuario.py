import base64
import os
import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Usuario:
    def __init__ (self,nombre_usuario,password):
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.salt =  os.urandom(16)
        self.conexion = sqlite3.connect("usuarios.db")

    def crear_usuario(self):
        try:
            self.query = self.conexion.execute("insert into usuarios(nombre_usuario,contraseña,sal) values (?,?,?)",(self.nombre_usuario,self.password,self.salt))
            self.conexion.commit()
        except Exception as err:
            print('Insersión fallida: %s\nError: %s' % (self.query, str(err)))
        finally:
            self.conexion.close()

"""
CLASE BASURAS
"""
# *Importar MONGO DB
from pymongo import MongoClient


class Conexion():

    def __init__(self):

        pass

    def conectar(self):
        MONGO_URL_ATLAS = "mongodb+srv://username:passwordpassword@cluster0-gc7xr.mongodb.net/test?retryWrites=true&w=majority"
        client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
        db = client['sorteo']
        return db

    # def comprobar_usuario(self, dni):
    #     db = self.conectar()
    #     collection = db['usuarios']
    #     comprobacion = collection.find({})

    #     return comprobacion

    # def agregar_Datos(self, arrayObjetos):
    #     db = self.conectar()
    #     collection = db['usuarios']
    #     comprobacion = collection.find({})

    #     return comprobacion

    

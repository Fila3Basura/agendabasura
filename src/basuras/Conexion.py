
"""
CLASE BASURAS
"""
# *Importar MONGO DB
from pymongo import MongoClient


class Conexion():

    def __init__(self):

        pass

    def _conectar(self):
        MONGO_URL_ATLAS = "mongodb+srv://username:passwordpassword@cluster0-2rsyp.mongodb.net/test?retryWrites=true&w=majority"
        client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
        db = client['sorteo']
        return db

    def leer(self, arrayObjetos):
        db = self._conectar()
        collection = db['diasbasura']

        pass


    def guardar(self, arrayObjetos):
        pass



    def borrar(self):

        pass

    def modificar(self):
        pass

    

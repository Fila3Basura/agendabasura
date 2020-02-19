
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
        db = client['agendabasura']
        return db

    def leer(self):
        db = self._conectar()
        collection = db['diasbasura']

        #* lista que contendrá el resultado de la query de mongoDB
        listaContenedor = []

        buscarDocumento = collection.find({})

        for i in list(buscarDocumento):
            #* Se agrega a la lista, porque no funciono colocar list(buscarDocumento) directamente en el condicional.
            listaContenedor.append(i)
                

        if listaContenedor != []:
            
            #* Ahora esta lista tiene todos los documentos
            print(listaContenedor)
            
            return listaContenedor





    def guardar(self, arrayObjetos):
        db = self._conectar()
        collection = db['diasbasura']
        #* lista que contendrá el resultado de la query de mongoDB
        listaContenedor = []

        for i in arrayObjetos:

            #* Query de mongoDB para buscar si el documento existe para despues comprobarlo mediante el condicional.
            # buscarDocumento = collection.find(i)
            #* Si no funciona el anterior query, probar con este.
            # buscarDocumento = collection.find({'dia': i['dia'], 'basura': i['basura']})

            # for i in list(buscarDocumento):
                #* Se agrega a la lista, porque no funciono colocar list(buscarDocumento) directamente en el condicional.
                # listaContenedor.append(i)
                

            # if listaContenedor != []:

                #* mensaje de que ya existen documentos de algún día
                # mensaje = f'Ya existen el documento del día: {i['dia']}'

                # return mensaje

            # else:

                #* Método que nos agrega el documento del día a la BD de mongoDB
            collection.insert_one(i)

                #* Mensaje de que aún no exsite un documento de ese día, pero ya se acaba de agregar
                # mensaje = f'No existe el documento del día: {i['dia']}, pero ya se acaba de agregar'

                # return mensaje



    def borrar(self):
        db = self._conectar()
        collection = db['diasbasura']

        collection.delete_many({})



    def modificar(self):
        pass



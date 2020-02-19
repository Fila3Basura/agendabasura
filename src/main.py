import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session

#* import Clase Basuras
from basuras.Basuras import Basuras
# from basuras.Fechas import Fechas

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def inicio():
    return render_template('index.html')

#ruta para abrir el archivo configuracion
@app.route('/configuracion', methods = ['GET', 'POST'])
def configuracion():
    
    if(request.method == 'POST'):
        lunes = request.form('lunes')
        print(lunes)

    return render_template('configuracion.html')


@app.route('/pruebajose', methods = ['GET', 'POST'])
def pruebajose():
    return render_template('pruebajose.html')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
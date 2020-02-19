#* necesitamos esta libreria que nos ayudará con el if main.
import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session

#* import Clase Basuras
# 
from basuras.logica import sacarDiaSemanaNombre, sacarArraySemana

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
<<<<<<< HEAD
def index():
=======
def inicio():
    if(request.method == 'POST'):
        
        # lunes = request.form.getlist('lunes')
        # martes = request.form.getlist('martes')
        # miercoles = request.form.getlist('miercoles')
        # jueves = request.form.getlist('jueves')
        # viernes = request.form.getlist('viernes')
        # sabado = request.form.getlist('sabado')
        # domingo = request.form.getlist('domingo')
        lunes = ['papel']
        martes = ['vidrio', 'plastico']
        miercoles = ['maceta', 'pila']
        jueves = ['patata']
        viernes = []
        sabado = []
        domingo = []
        array = sacarArraySemana(lunes, martes, miercoles, jueves, viernes, sabado, domingo)

        nombreDiaSemana = sacarDiaSemanaNombre()

        return render_template('index.html', array = array, nombreDiaSemana = nombreDiaSemana)
>>>>>>> daf24946714a38b25c50ce1cf07892bc5e3de8b7
    return render_template('index.html')

#ruta para abrir el archivo configuracion
@app.route('/configuracion', methods = ['GET', 'POST'])
def configuracion():
    return render_template('configuracion.html')

@app.route('/pruebajose', methods = ['GET', 'POST'])
def pruebajose():
    return render_template('pruebajose.html')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
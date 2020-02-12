import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session


app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def inicio():
    return 'hola'

#ruta para abrir el archivo configuracion
@app.route('/configuracion', methods = ['GET', 'POST'])
def configuracion():
    return render_template('configuracion.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
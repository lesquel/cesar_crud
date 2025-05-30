from flask import Flask, render_template, request, redirect
from utils.helpers import guardar_cliente, obtener_clientes, eliminar_cliente
import os

app = Flask(__name__)

@app.route('/')
def index():
    clientes = obtener_clientes()
    return render_template('index.html', clientes=clientes)

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    fecha_nacimiento = request.form['fecha_nacimiento']
    correo = request.form['correo']
    celular = request.form['celular']

    guardar_cliente(nombre, apellido, fecha_nacimiento, correo, celular)
    return redirect('/')

@app.route('/eliminar', methods=['POST'])

def eliminar():
    cliente_id = request.form['cliente_id']
    eliminar_cliente(cliente_id)
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)


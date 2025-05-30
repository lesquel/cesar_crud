from sqlalchemy import create_engine, text
import sqlite3

engine = create_engine('sqlite:///crudregistro.db')

def guardar_cliente(nombre, apellido, fecha_nacimiento, correo, celular):
    with engine.connect() as conn:
        query = text("""
            INSERT INTO registro_cliente (nombre, apellido, fecha_nacimiento, correo, celular)
            VALUES (:nombre, :apellido, :fecha_nacimiento, :correo, :celular)
        """)
        conn.execute(query, {
            'nombre': nombre,
            'apellido': apellido,
            'fecha_nacimiento': fecha_nacimiento,
            'correo': correo,
            'celular': celular
        })
        conn.commit()
        
def obtener_clientes():
    conexion = sqlite3.connect('crudregistro.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, apellido, fecha_nacimiento, correo, celular FROM registro_cliente")
    filas = cursor.fetchall()
    conexion.close()
    
    return [
        {
            'id': fila[0],
            'nombre': fila[1],
            'apellido': fila[2],
            'fecha_nacimiento': fila[3],
            'correo': fila[4],
            'celular': fila[5]
        } for fila in filas
    ]

def eliminar_cliente(cliente_id):
    import sqlite3
    conexion = sqlite3.connect('crudregistro.db')
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM registro_cliente WHERE id = ?", (cliente_id,))
    conexion.commit()
    conexion.close()



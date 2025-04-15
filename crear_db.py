import sqlite3

def crear_base_datos():

    conexion = sqlite3.connect('contactos.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            correo TEXT,
            telefono TEXT
        )
    ''')

    conexion.commit()
    conexion.close()

crear_base_datos()

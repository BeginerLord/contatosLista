import sqlite3

def crear_base_datos():
    # Conectar a la base de datos (se crea el archivo si no existe)
    conexion = sqlite3.connect('contactos.db')
    cursor = conexion.cursor()

    # Crear la tabla de contactos si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            correo TEXT,
            telefono TEXT
        )
    ''')

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

# Llamar a la función para crear la base de datos y la tabla
crear_base_datos()

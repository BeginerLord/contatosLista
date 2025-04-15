import sqlite3

class Contacto:
    def __init__(self):
        self.db = 'contactos.db'  # Nombre del archivo de base de datos

    def obtener_todos(self):
        # Obtener todos los contactos desde la base de datos
        conexion = sqlite3.connect(self.db)
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM contactos')
        contactos = cursor.fetchall()

        conexion.close()
        return contactos

    def agregar_contacto(self, nombre, apellido, correo, telefono):
        # Agregar un nuevo contacto a la base de datos
        conexion = sqlite3.connect(self.db)
        cursor = conexion.cursor()

        cursor.execute('''
            INSERT INTO contactos (nombre, apellido, correo, telefono)
            VALUES (?, ?, ?, ?)
        ''', (nombre, apellido, correo, telefono))

        conexion.commit()
        conexion.close()

    def eliminar_contacto(self, codigo):
        # Eliminar un contacto de la base de datos
        conexion = sqlite3.connect(self.db)
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM contactos WHERE id = ?', (codigo,))
        conexion.commit()
        conexion.close()

    def actualizar_contacto(self, codigo, nombre, apellido, correo, telefono):
        # Actualizar un contacto en la base de datos
        conexion = sqlite3.connect(self.db)
        cursor = conexion.cursor()

        cursor.execute('''
            UPDATE contactos
            SET nombre = ?, apellido = ?, correo = ?, telefono = ?
            WHERE id = ?
        ''', (nombre, apellido, correo, telefono, codigo))

        conexion.commit()
        conexion.close()

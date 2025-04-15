from flask import Flask, render_template, request, redirect, flash
import re
from contacto_modelo import Contacto  # Importar la clase Contacto

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # necesaria para usar flash

contacto_db = Contacto()  # Instanciar la clase Contacto

def es_valido(nombre, apellido, correo, telefono):
    errores = []

    if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", nombre):
        errores.append("El nombre solo debe contener letras.")
    if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", apellido):
        errores.append("El apellido solo debe contener letras.")
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
        errores.append("El correo electrónico no tiene un formato válido.")
    if not telefono.isdigit():
        errores.append("El número de teléfono solo debe contener dígitos.")

    return errores

@app.route('/')
def index():
    contactos = contacto_db.obtener_todos()  # Obtener los contactos de la base de datos
    return render_template("index.html", contactos=contactos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    telefono = request.form['telefono']

    errores = es_valido(nombre, apellido, correo, telefono)

    if errores:
        for error in errores:
            flash(error, 'error')
        return redirect('/')

    contacto_db.agregar_contacto(nombre, apellido, correo, telefono)  # Agregar contacto a la base de datos
    flash("Contacto agregado correctamente.", 'success')
    return redirect('/')

@app.route('/eliminar/<int:codigo>')
def eliminar(codigo):
    contacto_db.eliminar_contacto(codigo)  # Eliminar contacto de la base de datos
    flash("Contacto eliminado correctamente.", 'success')
    return redirect('/')

@app.route('/actualizar/<int:codigo>', methods=['GET', 'POST'])
def actualizar(codigo):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        telefono = request.form['telefono']

        errores = es_valido(nombre, apellido, correo, telefono)

        if errores:
            for error in errores:
                flash(error, 'error')
            return redirect(f'/actualizar/{codigo}')

        contacto_db.actualizar_contacto(codigo, nombre, apellido, correo, telefono)  # Actualizar contacto en la base de datos
        flash("Contacto actualizado correctamente.", 'success')
        return redirect('/')

    contacto = [c for c in contacto_db.obtener_todos() if c[0] == codigo][0]
    return render_template("actualizar.html", contacto=contacto)

if __name__ == "__main__":
    app.run(debug=True)

# 📇 Sistema de Gestión de Contactos (Consola)

## 🧩 Introducción

El **Sistema de Gestión de Contactos** es una aplicación de consola que permite gestionar contactos personales. Puedes agregar, buscar, actualizar, eliminar y listar contactos almacenados en una base de datos SQLite.

---

## ⚙️ Funcionalidades

1. **Agregar Contacto**: Permite registrar un nuevo contacto con nombre, apellido, correo y teléfono.
2. **Eliminar Contacto**: Elimina un contacto existente utilizando su código único.
3. **Buscar Contacto**: Busca contactos por nombre o correo electrónico.
4. **Actualizar Contacto**: Modifica los datos de un contacto existente.
5. **Mostrar Todos**: Lista todos los contactos almacenados.
6. **Salir**: Finaliza la aplicación.

---

## 🔄 Flujo de Trabajo

1. **Inicio**: Ejecuta el archivo `main.py` para iniciar el programa.
2. **Menú Principal**: Selecciona una opción del menú para realizar una acción.
3. **Interacción**: Ingresa los datos solicitados según la opción seleccionada.
4. **Base de Datos**: Los datos se almacenan y gestionan en un archivo SQLite llamado `contactos.db`.

---

## 🛠️ Archivos del Proyecto

### 1. **`main.py`**
   - Es el punto de entrada del programa.
   - Contiene el menú principal y la lógica para interactuar con el usuario.
   - Llama a los métodos de la clase `Contacto` para realizar las operaciones.

### 2. **`contacto_modelo.py`**
   - Contiene la clase `Contacto`, que implementa la lógica para interactuar con la base de datos SQLite.
   - Métodos principales:
     - `obtener_todos()`: Recupera todos los contactos.
     - `agregar_contacto(nombre, apellido, correo, telefono)`: Agrega un nuevo contacto.
     - `eliminar_contacto(codigo)`: Elimina un contacto por su ID.
     - `actualizar_contacto(codigo, nombre, apellido, correo, telefono)`: Actualiza los datos de un contacto.

### 3. **`crear_db.py`**
   - Crea la base de datos SQLite (`contactos.db`) y la tabla `contactos` si no existe.
   - Se ejecuta automáticamente al iniciar el proyecto por primera vez.

---

## 🧰 Tecnologías Utilizadas

- **Lenguaje**: Python 3.
- **Base de Datos**: SQLite.
- **Paradigma**: Programación Orientada a Objetos (POO).

---

## 🧩 Uso de POO y Herencia

### **Programación Orientada a Objetos (POO)**
El proyecto utiliza POO para organizar el código y separar responsabilidades:
- **Clase `Contacto`**:
  - Encapsula toda la lógica relacionada con la gestión de contactos.
  - Proporciona métodos para interactuar con la base de datos (`agregar_contacto`, `eliminar_contacto`, etc.).
  - Mejora la reutilización y el mantenimiento del código.

### **Herencia**
Aunque este proyecto no utiliza herencia directamente, la estructura basada en clases permite extender fácilmente la funcionalidad en el futuro. Por ejemplo:
- Podrías crear una clase `ContactoVIP` que herede de `Contacto` y agregue funcionalidades específicas, como un campo adicional para notas importantes.

---

## 🚀 Cómo Ejecutar el Proyecto

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ContactList-Python

   ContactList-Python/

   Instala Python: Asegúrate de tener Python 3 instalado en tu sistema.

Crea la base de datos: Ejecuta el archivo crear_db.py para generar la base de datos:

python crear_db.py

Ejecuta el programa: Inicia la aplicación ejecutando main.py:

python main.py

📂 Estructura del Proyecto

│
├── [contacto_modelo.py](http://_vscodecontentref_/1)   # Clase para gestionar contactos en la base de datos
├── [crear_db.py](http://_vscodecontentref_/2)          # Script para crear la base de datos SQLite
├── [main.py](http://_vscodecontentref_/3)              # Punto de entrada del programa
└── [contactos.db](http://_vscodecontentref_/4)         # Base de datos SQLite (se genera automáticamente)

📖 Ejemplo de Uso
Agregar un contacto:
Selecciona la opción 1 en el menú.
Ingresa los datos del contacto (nombre, apellido, correo, teléfono).
Buscar un contacto:
Selecciona la opción 3.
Ingresa el nombre o correo del contacto que deseas buscar.
Actualizar un contacto:
Selecciona la opción 4.
Ingresa el código del contacto y los nuevos datos.
Eliminar un contacto:
Selecciona la opción 2.
Ingresa el código del contacto que deseas eliminar.
📝 Notas
Asegúrate de ejecutar crear_db.py antes de usar el programa por primera vez.
Los datos se almacenan en el archivo contactos.db, que se genera automáticamente.
Este proyecto es modular y puede extenderse fácilmente con nuevas funcionalidades.


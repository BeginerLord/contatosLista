# 📇 Sistema de Gestión de Contactos

## 🧩 Introducción

El **Sistema de Gestión de Contactos** es una aplicación web ligera y eficiente que permite a los usuarios almacenar, visualizar, actualizar y eliminar contactos personales. Diseñada con una interfaz limpia y moderna, esta herramienta es ideal para pequeñas empresas o uso personal. 

Permite gestionar información clave de cada contacto, como:  
➡️ Nombre  
➡️ Apellido  
➡️ Correo electrónico  
➡️ Teléfono  

---

## ⚙️ Características Principales

- ✅ **Agregar Contactos**: Ingreso de nuevos contactos a través de un formulario validado.
- 📄 **Visualizar Contactos**: Listado completo en formato tabla.
- 🔁 **Actualizar Contactos**: Modificación de datos existentes.
- ❌ **Eliminar Contactos**: Eliminación directa desde el listado.
- 🛡️ **Validación de Datos**: Asegura que nombres no contengan números y formatos de email/teléfono sean correctos.

---

## 🔄 Flujo de Trabajo

1. **Inicio**: Se muestran todos los contactos disponibles en la base de datos.
2. **Agregar Contacto**: Formulario para crear un nuevo contacto con validaciones.
3. **Actualizar Contacto**: Edición de datos de un contacto existente.
4. **Eliminar Contacto**: Opción para eliminar desde el listado principal.
5. **Mensajes de error**: Se notifican errores de validación de forma clara y amigable.

---

## 🧰 Tecnologías Utilizadas

### 🔙 Backend

- **Python 3**  
  Lenguaje principal de desarrollo. Fácil de aprender y potente para desarrollo web.
  
- **Flask**  
  Micro-framework ligero usado para manejar rutas, solicitudes HTTP y lógica del negocio.

- **SQLite**  
  Base de datos integrada, ideal para proyectos pequeños. No necesita servidor adicional.

- **Jinja2**  
  Motor de plantillas que permite generar HTML dinámico desde Python.

---

### 🎨 Frontend

- **HTML5 & CSS3**  
  Estructura y estilos básicos de la interfaz.

- **Bootstrap 4**  
  Framework CSS para lograr un diseño moderno y completamente responsivo sin esfuerzo adicional.

---

## 📦 Requisitos e Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/gestion-contactos.git
cd gestion-contactos

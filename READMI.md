Introducción

El software de Gestión de Contactos es una aplicación web diseñada para almacenar, actualizar, eliminar y visualizar contactos de manera sencilla y eficiente. Esta aplicación permite a los usuarios gestionar información de sus contactos, como nombre, apellido, correo electrónico y teléfono. A continuación, se detalla cómo funciona la aplicación y las tecnologías empleadas en su desarrollo.

2. Funcionamiento del Software

2.1 Características Principales

El software permite realizar las siguientes operaciones:

- Aregar Contactos: El usuario puede ingresar los detalles de un nuevo contacto, como nombre, apellido, correo electrónico y teléfono.

- visualizar Contactos: Todos los contactos almacenados en la base de datos se muestran en una tabla con su información correspondiente.

- Atualizar Contactos: El usuario puede modificar los detalles de un contacto existente.

- Eliminar Contactos: Permite eliminar contactos de la base de datos.

- Validación de Datos: Durante la adición o actualización de un contacto, el sistema valida los datos ingresados para asegurarse de que el nombre y apellido no contengan números y que el correo electrónico y teléfono tengan el formato correcto.



2.2 Flujo de Trabajo

El flujo de trabajo del software se puede desglosar en los siguientes pasos:

Inicio de la Aplicación: Al acceder a la aplicación, se muestra una lista de todos los contactos almacenados en la base de datos.

Agregar un Nuevo Contacto: Cuando el usuario hace clic en "Agregar Contacto", se muestra un formulario donde se deben ingresar los datos del nuevo contacto.

Validación de Datos: Al enviar el formulario, se verifica que los campos del contacto sean válidos. Si los datos son incorrectos, se muestran mensajes de error.

Actualizar un Contacto: Si el usuario desea actualizar un contacto, puede seleccionar un contacto de la lista, lo cual lo llevará a un formulario donde podrá modificar los datos. Este formulario también tiene validación de datos.

Eliminar un Contacto: El usuario puede eliminar un contacto de la base de datos al hacer clic en el botón de eliminar.

3. Tecnologías Utilizadas


3.1 Flask (Backend)
Flask es un micro-framework de Python utilizado para desarrollar aplicaciones web. En este proyecto, se utiliza Flask para gestionar las rutas, procesar las solicitudes HTTP (como GET y POST) y manejar la lógica de negocio relacionada con los contactos. Flask permite la fácil creación de rutas y la integración con el sistema de plantillas Jinja2 para renderizar las vistas de la interfaz.

Ventajas de Flask:

Ligero y fácil de usar.

Escalable y flexible.

Gran comunidad y muchas extensiones disponibles.



3.2 HTML5 y CSS (Frontend)
Para la interfaz de usuario, se ha utilizado HTML5 para la estructura básica de las páginas y CSS para los estilos. Se emplea la estructura estándar de HTML con formularios, tablas y enlaces para interactuar con la base de datos. Además, se utiliza Bootstrap 4 para proporcionar un diseño responsivo y moderno.

Ventajas de HTML y CSS:

HTML5 proporciona la semántica adecuada para estructurar el contenido.

CSS permite personalizar los estilos de la página de manera eficiente.

Bootstrap facilita la creación de interfaces atractivas y responsivas.



3.3 Bootstrap 4
Bootstrap 4 es un framework de CSS utilizado para crear interfaces web responsivas y visualmente atractivas. Se ha utilizado para mejorar la apariencia de la aplicación y facilitar el diseño de formularios, botones y tablas sin necesidad de escribir mucho código CSS desde cero.

Ventajas de Bootstrap:

Ofrece componentes listos para usar (como botones, formularios, tablas, etc.).

Diseño responsivo que se adapta a diferentes tamaños de pantalla.

Amplia documentación y comunidad de soporte.



3.4 SQLite (Base de Datos)
SQLite es una base de datos ligera que se utiliza para almacenar los contactos de manera persistente. SQLite está integrada en Python y no requiere un servidor de base de datos independiente, lo que hace que sea ideal para aplicaciones pequeñas o medianas. En este proyecto, se utiliza para guardar la información de los contactos, como el nombre, apellido, correo electrónico y teléfono.

Ventajas de SQLite:

No requiere configuración de servidor.

Ligera y fácil de usar.

Ideal para aplicaciones con pocos usuarios o pequeña escala.



3.5 Python 3
El backend de la aplicación está desarrollado en Python 3, un lenguaje de programación de alto nivel y muy popular debido a su simplicidad y versatilidad. Python facilita la creación de aplicaciones web utilizando frameworks como Flask y la integración con bases de datos como SQLite.

Ventajas de Python:

Sintaxis clara y fácil de aprender.

Gran cantidad de bibliotecas y herramientas para desarrollo web y bases de datos.

Compatible con múltiples plataformas.



3.6 Jinja2 (Plantillas)
Jinja2 es un motor de plantillas utilizado por Flask para renderizar las vistas de la aplicación. Con Jinja2, se pueden insertar variables y realizar operaciones lógicas dentro del HTML, lo que permite generar contenido dinámico basado en los datos del backend.

Ventajas de Jinja2:

Potente y flexible para generar contenido dinámico.

Compatible con estructuras de control como bucles y condicionales dentro del HTML.

Permite reutilizar plantillas y mantener el código limpio.
# Formularios de Negocio con Bootstrap y Flask

Tarea de la semana 8 del curso Desarrollo Web (036).
Universidad Mariano Gálvez.

## Funcionalidades

- Página de inicio con enlaces a los formularios.
- Registro de clientes y confirmación de los datos recibidos.
- Registro de proveedores y confirmación de los datos recibidos.
- Inicio de sesión con validación de usuario y contraseña.
- Plantilla compartida con menú y pie de página.

Los formularios utilizan GET y POST. Los datos no se guardan de forma permanente.

## Ejecución

1. Instalar Flask: `python -m pip install flask`
2. Ejecutar el proyecto: `python app.py`
3. Abrir http://localhost:5000 en el navegador.

Se necesita conexión a internet para cargar Bootstrap por CDN.

## Credenciales de prueba

- Usuario: `admin`
- Contraseña: `1234`

El inicio de sesión es una práctica con un diccionario de Python, sin base de datos ni cifrado. La casilla Recordarme no guarda la sesión.

## Bonus: modal de confirmación

Se agregó un modal de Bootstrap al formulario de clientes para confirmar el envío.

- Al completar los campos y presionar Enviar, aparece el modal.
- Cancelar cierra el modal y conserva los datos del formulario.
- Confirmar envío manda los datos por POST y muestra la página de confirmación.

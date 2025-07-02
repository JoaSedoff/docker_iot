# CRUD Agenda Flask

Este proyecto es una pequeña agenda web desarrollada con Flask, que permite gestionar contactos (nombre, teléfono y email) y cuenta con autenticación de usuarios. Además, incluye la opción de alternar entre dos temas visuales (claro y oscuro) utilizando Bootswatch.

## Características

- Registro e inicio de sesión de usuarios.
- Alta, edición y eliminación de contactos.
- Visualización de todos los contactos en una tabla.
- Cambio de tema visual (claro/oscuro) desde la barra de navegación.
- Mensajes de confirmación y error mediante alertas.
- Interfaz responsiva basada en Bootstrap 5 (Bootswatch).

## Requisitos

- Python 3.11+
- MariaDB o MySQL

## Variables de entorno necesarias
- CRUD_USER=usuario_db
- CRUD_PASS=contraseña_db
- CRUD_DB=nombre_db
- MARIADB_SERVER=nombre_o_ip_del_servidor
- FLASK_SECRET_KEY=clave_secreta_flask

## Estructura principal

- `crud/crud.py`: Código principal de la aplicación Flask.
- `crud/templates/`: Plantillas HTML.
- `crud/static/`: Archivos estáticos (JS, CSS).
- `compose.yaml`: Configuración de Docker Compose.

## Notas

- El cambio de tema se realiza guardando la preferencia en la sesión del usuario.
- El sistema requiere que la base de datos y el usuario existan previamente en MariaDB/MySQL.

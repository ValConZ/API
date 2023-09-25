Código del API de la materia de Automatización de Infraestructura Digital 1.
master:    MICHEL OROZCO CARRERA
branches:
>valeria:  CONTRERAS ZARAGOZA VALERIA
>oscar:    DOMINGUEZ GARCIA OSCAR
>miguel:   FLORES NESTLE MIGUEL ANGEL
>marlen:   FRUCTUOSO BRAVO MARLEN
>karen:    FUENTES ARCOS KAREN JULIE
>denilson: PEREZ EUGENIO DENILSON ISAAC
>janeth:   RIVERA HERNANDEZ JANETH
>angel:    SANCHEZ ORTEGA ANGEL YAIR

=== LIBRERÍAS ===

Flask
SQLAlchemy
Marshmallow
---
Flask_Restful
Flask_SQLAlchemy
Flask_Migrate
Flask_Marshmallow
Marshmallow_SQLAlchemy

=== ESTRUCTURA DE ARCHIVOS/CARPETAS ===

+api-peliculas
|_+ app
  |_+ common
    |_ __init__.py
    |_ error_handling.py   # Utilidades para el manejo de errores
  |_+ films
    |_+ api_v1_0
      |_ __init__.py
      |_ resources.py   # Endpoints del API
      |_ schemas.py     # Esquemas para serializar los modelos
    |_ __init__.py
    |_ models.py   # Modelos
  |_ __init__.py   # Configuración de la aplicación
  |_ db.py         # Configuración de la base de datos
  |_ ext.py        # Instanciación de las extensiones
|_+ config         # Directorio para la configuración
  |_ __init__.py
  |_ default.py    # Configuración por defecto
|_ entrypoint.py   # Crea la instancia de la app


=== BD AUTOMATIZACIÓN DE TAREAS EN UN S.O. ===

tasks:
>id, clave primaria.
>title, título de la tarea
>description, pequeña descripción de la tarea
>date_creation, fecha de la creación de la tarea
>status, valor A (activo) ó I (inactivo)

execution_logs:
>id, clave primaria.
>task_id, clave externa de la tarea a la que hace referencia
>user_id, clave externa del usuario que realizó la tarea
>length, duración (en segundos) de la ejecución de la tarea
>status, valor A (activo) ó I (inactivo)

usuario:
> id, clave primaria
> nombre, nombre de usuario de ingreso
> password, la clave de ingreso del usuario
> status, valor A (activo) ó I (inactivo)


=== env/bin/activate ===

...
export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"

=== proceso de configuración ===

1. pip install virtualenv env
2. virtualenv env
3. editar: env/bin/activate
...
export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"
4. source env/bin/activate
5. pip install flask sqlalchemy marshmallow flask_restful flask_sqlalchemy flask_migrate flask_marshmallow marshmallow_sqlalchemy
6. pip freeze > requirements.txt

=== proceso de inicialización y ejecución ===

1. flask db init
2. flask db migrate -m "Initial_DB"
3. flask db upgrade
*. flask run

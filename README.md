# LilMarcian

## Ubicación de la página

http://lilmarcian.pythonanywhere.com/

## Instalación

### Requisitos:
  * Python
  * MySQL
    * CREATE DATABASE lilmarcian;
    * Modificar el config.py con los datos necesarios


### Comandos Python
* Crear entorno virtual (env es el nombre del environment)
```Console
python -m venv env
```

* Accediendo al entorno virtual (env) (Desde windows)
```Console
.\env\Scripts\activate
```

* Agregar dependencias instaladas en el env
```Console
pip freeze > requirements.txt
```

* Inicializar la base de datos (Si aparece por consola la base de datos fue inicializada esta todo ok)
```Console
flask init-db
```

* Correr la app
```Console
python run.py
```

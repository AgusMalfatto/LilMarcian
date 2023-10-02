# Comandos de GIT

* Traer actualizaciones en github
```Console
git pull origin
```

* Ver los archivos que modificaste y el estado en el que se encuentran
```Console
git status
```

* Agegar cambios de archivos (Esto es previo al commit)
```Console
git add nombre_archivo1 nombre_archivo2
```

* Realizar el commit para despues subirlo en el github (Garantizar que funciona el codigo y no se agrega cualquier cosa)
```Console
git commit -m "Comentario descriptivo de los cambios realizados"
```

* Subir los cambios al repo de github (antes de publicar un cambio asegurarse que el codigo esta bien y no rompe nada)
```Console
git push origin master
```


# Comandos Python
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

* Instalar nuevas dependencias
```Console
pip install -r requirements.txt
```


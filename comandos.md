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


# Comandos pip
Agregar dependencias instaladas en el env
```Pip
pip freeze > requirements.txt
```

Instalar nuevas dependencias
```Pip
pip install -r requirements.txt
```

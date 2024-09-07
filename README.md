1. creacion del entorno virtual `py -3 -m venv .venv`
2. `F1` en vs-code y `Python: Select Interpreter`, finalmente seleccionar la opcion que contiene las palabras venv, de esta manera la terminal usada durante el proyecto activara automaticamente el entorno
3. descargar archivo `.gitignore` de [toptal](https://www.toptal.com/developers/gitignore/api/python)
4. inicio del repositorio `git init`, `git add .`y `git commit -m "first commit"`
5. creacion `Dockerfile`
6. creacion de la estructura de carpetas
   1. `/`: raiz
   2. `src`: Carpeta principal con todo el codigo
      1. `database`: Contiene informacion de conexion a la base de datos
      2. `resources` o `routes`: Contiene todas las rutas o endpoints
      3. `models`: Contiene las clases que manejan la logica de la base de datos, todos los queries necesarios
      4. `services`: Contiene todas las operaciones logicas que podemos hacer con los modelos
      5. `utils`: Contiene todo lo relacionado a la seguridad y manejo de tokens
      6. `tests`: Contiene todo lo relacionado a las pruebas sobre el codigo
   3. `.env`: Variables de entorno que no se deben compartir
   4. `.gitignore`: Archivos locales innecesarios de compartir
   5. `config.py`: Todas las configuraciones de la app
   6. `app.py`: Se encarga de lanzar toda la aplicacion
   7. `Dockerfile`: Informacion del contenedor
   8. `README.md`: Guia sobre el proyecto
7. para que las carpetas funcionen como modulos, cada una debe contener un archivo llamado `__init__.py`, incluida la propia carpeta `src`
8. instalar los paquetes necesarios
   1. `flask`: Libreria principal
   2. `python-dotenv` para usar el `.env`
9.  generar listado de requerimientos `pip freeze > requirements.txt`
10. crear imagen docker `docker build -t prueba-tecnica .` para comprobar que todo funcione correctamente hasta este punto
11. Creacion de los modelos `department`, `employment_record`y `job`; cumpliendo con las especificaciones de las tablas encontradas en los documentos `*.csv`
12. Creacion del archivo `schemas` para el manejo de errores en el ingreso de datos, (¿Es este el dto?)
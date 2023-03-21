

# Proyecto Prefectura El Oro

![Screenshot_1](docs/screenshots/logo_django.ico "Biome list" )

## BioORO 

Este programa te permitirá observar y conocer con detalle sobre el terreno las flora, fauna y areas naturales de la provincia de El ORO. Está basada en el libro [Sistema Dulceacuícola de la provincia de El ORO]("http://inabio.biodiversidad.gob.ec/wp-content/uploads/2019/12/Libro%20Corredor%20Ecol%C3%B3gico%20de%20El%20Oro-web_compressed.pdf"), y además de las fichas de identificación de flora y fauna

Esta aplicación te permitirá subir las fotografías para demonstrar el hallazgo de una nueva especie de flora o fauna hallada por los usuarios.



`Homepage`

![Screenshot_1](docs/screenshots/homepage.jpg "Homepage" )


`Lista de biomas`

![Screenshot_1](docs/screenshots/biomalist.jpg "Biome list" )
 

`Detalles de las especies`

![Screenshot_1](docs/screenshots/specie_detail.jpg "Species detail" )
 -->

`Descarga la guia de especies de El ORO`

 http://inabio.biodiversidad.gob.ec/wp-content/uploads/2019/12/Libro%20Corredor%20Ecol%C3%B3gico%20de%20El%20Oro-web_compressed.pdf



# Uso

Django es un framework de desarrollo para Python que se emplea para la creación de páginas web. 
 

Si no tines django instalado para python3 entonces ejecuta:

```
pip3 install django
```

Activa el entorno virtual para el proyecto.

```
virtualenv2 --no-site-packages env
source env/bin/activate
```

Instala las dependencias del proyecto:

```
pip install -r requirements.txt
```

Simplemente aplica las migraciones:

```
python manage.py migrate
```
Ahora puedes ejecutar el servidor de desarrollo:

```
python manage.py runserver
```


# Configuración de la Base de Datos

El código de la aplicación de muestra contienen la configuración de conexión de la base de datos y las credenciales que se basan en poder usar ```Mysql```.

### APP_CONFIG
Puede ajustar la configuración de gunicorn a través de la variable de entorno APP_CONFIG que, cuando se configura, debe apuntar a un archivo de configuración. 

### DJANGO_SECRET_KEY
Esta variable de entorno tiene su valor generado automáticamente. Por motivos de seguridad, asegúrese de establecer esto en una cadena aleatoria.



<!-- Este programa tiene como fin reunir el mayor número posible de datos conocidos, o que se vayan dando a conocer en el futuro, sobre los Biomas, Fauna y Flora en la  provincia de El Oro -->

<!-- Python3, Django, MySQL,  -->

# technical_test
Prueba tecnica desarrollada por juan pablo perez santos para la empresa tusDatos.co

Este programa cuenta con 3 carpetas la cuales son

* punto1
* api
* client

## Punto1
Es un script de python el cual va a generar archivos csv con la información estructurada de los procesos según el filtro escogido,
el programa va a preguntar sobre cual tipo se desea hacer la consulta (actor o demandado) y la identificación del mismo, al momento
de terminar la consulta este va a generar un archivo csv en el directorio de carpetas **api/data/** el cual sera consumido por al momento
de llamar un endpoint con fastapi

## api
Este es un proyecto realizado con fastapi el cual contiene la autenticación de usuarios y tambien un endpoint que consulta a razón de unos paramettos
los archivos csv generados en el script del punto1 

## client
Proyecto desarrollado en angular que dispone una interfaz grafica la cual se conecta con la api y muestra en una tabla los elementos
estructuras del webscraping realizado en el script **punto 1**

### Pre-requisitos 📋

```
python 3 
MySQL
pip3
```

### Instalación 🚀

Para comenzar se recomienda crear un entorno virtual de python (no es obligatorio pero si recomendado), lo cual pude ejecutar el comando

> python -m venv entorno

Despues debe instalar los packages que se especifican en el requirements.txt

> pip install -r requirements.txt

Luego una vez que ya todo esta instalado, se debe crear un archivo .env dentro de el proyecto **api** el cual debe contener las siguientes
variables de entorno:

```
SECRET=
USER_DB=
PASSWORD_DB=
DB=
```
Antes de especificar cada una de las variables, el proyecto de **api** es manejado con una gestor de bases de datos mysql, por lo que previamente
usted debe tener una base de datos creada con el mismo nombre que le va a colocar en la variable de entorno **DB**

**SECRET** una llave secreta generada por usted
**USER_DB** es su usuario de base de datos por lo general es **root**
**PASSWORD_DB** contraseña de sus usuario para acceder a la BD
**DB** Nombre de la base de datos

Ahora solo falta instalar las dependencias del proyecto client de angular para ello, es necesario entrar a la carpeta y ejecutar 

> npm i --force

Y listo de esa manera ya tenemos todas las instalaciones necesarias para correr los 3 proyectos

## Correr programas 📦

Se recomienda correr los programas en el siguiente orden para de esa manera el debido flujo y funcionamiento

Primero se recomienda correr el script que se encuentra en la carpeta punto1 

> python main.py

Luego puede levantar el servidor api, dirigiendose a la carpeta de api y ejecutando

> python main:app --reload

Una vez levantado el servidor puedes acceder a la documentación de la API dirigiendose a

> localhost:8000/docs

Y por ultimo con el servidor arriba, se levanta el cliente de angular

> ng serve

De esa manera ya se tiene el flujo corriendo de manera correcta

## Autores ✒️

* **Juan pablo perez santos**

# Pequeña documentacion del proyecto
## Explicacion de estructuras de carpetas
##### Api: Contiene todas la configuracion de las endpoints de la aplicacion
##### Auth: Contiene configuracion de autenticacion como es la generacion y validacion de tokens usando JWT
##### BD: Contiene las configuracion de la base de datos en esta caso mySql y una carpetas modelos que son interpretados por el orm SqlAlchemy
##### Schemas: Contiene los modelos usando pydantic para validacion y gestion de datos
##### Services: Contiene servicios para el uso de la base de datos y otros uso separando las responsabilidad a los routers, router usan servicios
##### utils: Herramientas adicionales para nuestro programa como algoritmos de encriptamiento para nuestra bd
##### main.py: Centro de la app donde se inicializan nuestros routers

## Uvicorn
Se utiliza para iniciar una aplicación FastAPI con el servidor Uvicorn, que es un servidor ASGI para aplicaciones web en Python. 
### Ejecucion:

```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --workers 3
```

##### El port puedo ser cambiado por otro puerto si lo deseamos
##### Los worker nos servira para trabajar con multiples solicitudes simultaneamente la configuracion dependera de los requisitos de la cpu
## Configuración del Bucket de S3 en un Servidor EC2 y desarrollo en distribuciones de linux

Para configurar el acceso al bucket de S3 en un servidor EC2 para un entorno de producción, sigue estos pasos:

## 1. Crear el Directorio para las Credenciales de AWS

En primer lugar, debes crear un directorio para almacenar las credenciales de AWS si no existe.

```bash
mkdir -p ~/.aws
nano ~/.aws/credentials
```

## Agregar lo de aws cli

```bash
[default]
aws_access_key_id = 
aws_secret_access_key = 
```

## Verifcar si instalo

```bash
aws s3 ls
```

## Adicional

En el proyecto existe una carpeta de test para probar la api para subida de archivo 
y sirve como ejemplo de como se debe mandar la imagen y una pequeña descripcion


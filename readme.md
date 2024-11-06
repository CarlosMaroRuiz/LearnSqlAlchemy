# Configuración del Bucket de S3 en un Servidor EC2 y desarrollo en distribuciones de linux

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

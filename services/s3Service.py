
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from fastapi import UploadFile, HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

bucket_name = os.getenv("BUCKET_NAME")

def upload_file_to_s3(file: UploadFile,description: str = "", region_name: str = "us-east-1"):
    if file.content_type not in ["image/jpeg", "image/png", "image/gif"]:
        raise HTTPException(status_code=400, detail="Solo se permiten archivos de imagen (JPEG, PNG, GIF).")


    s3_client = boto3.client('s3', region_name=region_name)

    try:
   
        s3_client.upload_fileobj(file.file, bucket_name, file.filename)
        return {
            "message": f"Archivo '{file.filename}' subido correctamente a '{bucket_name}'.",
            "description": description
        }
    
    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="Credenciales de AWS no encontradas.")
    except PartialCredentialsError:
        raise HTTPException(status_code=403, detail="Las credenciales de AWS están incompletas.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir el archivo: {str(e)}")

from fastapi import APIRouter, File, UploadFile, Form, HTTPException, Depends
from services.s3Service import upload_file_to_s3
from schemas.fileModel import FileUpload  
from auth.decoderToken import get_current_user

router = APIRouter()

@router.post("/image")
async def upload_file(
    file: UploadFile = File(...),    
    description: str = Form(...),      
    token: str = Depends(get_current_user)  # Dependencia para obtener el token del usuario puedes usarlo en varias rutas :)
):
    response = upload_file_to_s3(file, description)
    return response

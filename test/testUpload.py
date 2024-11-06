import requests

url = "http://127.0.0.1:5000/upload/image"


file_path = "descarga.jpeg"


with open(file_path, "rb") as file:
  
    files = {
        "file": (file_path, file, "image/jpeg")  
    }
    data = {
        "description": "test"
    }
    
   
    response = requests.post(url, files=files, data=data)

print(response.json())

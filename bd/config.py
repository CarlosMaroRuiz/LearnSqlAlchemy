from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.base import Base
import os
from dotenv import load_dotenv

load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Creamos el motor de la base de datos en este caso usamos sqlite como bd
engine = create_engine(DATABASE_URL, echo=True)

#para inicializar nuestras tablas 
Base.metadata.create_all(bind=engine)


# Crear una sesion configurada
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
Mas por aprender
---------------------------------------------------------------------------- 
El metodo sessionmaker en SQLAlchemy es una fábrica que crea 
sesiones para interactuar con la base de datos. 
Una sesión es el contexto en 
el que se realizan todas las transacciones, 
consultas, inserciones, y actualizaciones a la base de datos
---------------------------------------------------------------------------- 


------------------------------------------------------------------------------------
autocommit=False:
Este parámetro desactiva el autocommit, lo que significa que las transacciones 
no se confirman automáticamente. Es decir, debes llamar a session.commit()
manualmente para confirmar los cambios (inserciones, actualizaciones o eliminaciones) 
en la base de datos.

Con autocommit=False, las operaciones se agrupan en una transacción, y debes decidir 
cuándo terminar la transacción con commit() o rollback().
Si fuera True, los cambios se confirmarían inmediatamente después de cada operación
sin necesidad de llamar a commit().
------------------------------------------------------------------------------------


bind=engine: La sesión esta vinculada a una base de datos especifica definida en el engine
"""
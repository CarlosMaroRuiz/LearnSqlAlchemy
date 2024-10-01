from .config import SessionLocal



# Crear una dependencia de sesionn para interactuar con la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

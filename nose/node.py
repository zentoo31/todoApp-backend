from sqlalchemy.orm import Session
from config.db import get_db

# Obtener la sesión de la base de datos
db: Session = next(get_db())

# Realizar operaciones en la base de datos (consultas, inserciones, etc.)
# Ejemplo de consulta:
usuarios = db.query(Usuario).all()
print(usuarios)

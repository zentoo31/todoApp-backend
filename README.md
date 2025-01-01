# Flask Todo App - Backend

Este es el backend de la aplicación de tareas (Todo App), desarrollado con Flask y SQLAlchemy. Proporciona una API REST para gestionar tareas y usuarios, y soporta comunicación en tiempo real con Flask-SocketIO.

## Tecnologías Utilizadas
- **Python**
- **Flask**: Framework web principal.
- **Flask-SQLAlchemy**: ORM para gestionar la base de datos SQL.
- **Flask-SocketIO**: Para soporte de WebSockets y comunicación en tiempo real.
- **PostgreSQL** (configurable para otros motores SQL).
- **Flask-Migrate**: Manejo de migraciones para la base de datos.

## Requisitos Previos
- Python 3.8 o superior
- pip (administrador de paquetes de Python)
- Git (opcional, para clonar el repositorio)
- PostgreSQL

## Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo/backend
```

### 2. Crear un Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate   # Windows
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Crea un archivo `.env` en el directorio principal del backend y agrega:
```env
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///todoapp.db  # Cambia a tu URL de base de datos si usas otro motor
SECRET_KEY=una_clave_secreta_segura
```

### 5. Inicializar la Base de Datos
```bash
flask db init
flask db migrate -m "Inicializar base de datos"
flask db upgrade
```

### 6. Ejecutar el Servidor
```bash
flask run
```
El backend estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Endpoints Principales

### Tareas (/tasks)
- `GET /tasks`: Obtiene todas las tareas.
- `POST /tasks`: Crea una nueva tarea.
- `PUT /tasks/<id>`: Actualiza una tarea existente.
- `DELETE /tasks/<id>`: Elimina una tarea.

### Usuarios (/users)
- `GET /users`: Obtiene todos los usuarios.
- `POST /users`: Crea un nuevo usuario.
- `GET /users/<id>`: Obtiene información de un usuario específico.

### WebSockets
- Canal: `/ws/tasks`
- Eventos:
  - `task_updated`: Notifica cuando una tarea es actualizada en tiempo real.
  - `task_deleted`: Notifica cuando una tarea es eliminada en tiempo real.

## Estructura del Proyecto
```
backend/
├── main.py            # Punto de entrada de la aplicación
├── models.py         # Modelos de datos con SQLAlchemy
├── routes/           # Rutas de la API
├── static/           # Archivos estáticos (si aplica)
└── .env              # Configuraciones sensibles
```

## Pruebas
Para ejecutar pruebas unitarias:
```bash
pytest
```

## Contribución
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad: `git checkout -b feature/nueva-funcionalidad`.
3. Haz commit de tus cambios: `git commit -m "Agregar nueva funcionalidad"`.
4. Sube los cambios: `git push origin feature/nueva-funcionalidad`.
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.



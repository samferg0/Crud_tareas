# CRUD de Tareas con FastAPI

API REST desarrollada en Python utilizando FastAPI, SQLAlchemy y SQLite para la gestión de tareas mediante operaciones CRUD (Crear, Consultar, Actualizar y Eliminar).

## Tecnologías utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Funcionalidades

- Crear una nueva tarea.
- Consultar todas las tareas registradas.
- Consultar una tarea por su ID.
- Actualizar cualquier información de una tarea.
- Eliminar tareas.
- Marcar tareas como completadas.
- Buscar tareas por título.
- Filtrar tareas por prioridad.
- Filtrar tareas por estado.

## Estructura del proyecto

```
Crud_tareas/
│
├── database.py        # Configuración de la base de datos
├── main.py            # Endpoints de la API
├── models.py          # Modelos de SQLAlchemy
├── schemas.py         # Esquemas de validación con Pydantic
├── requirements.txt   # Dependencias del proyecto
├── .gitignore
└── README.md
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/samferg0/Crud_tareas.git
```

Entrar al proyecto:

```bash
cd Crud_tareas
```

Crear un entorno virtual:

```bash
python -m venv venv
```

Activarlo:

### Windows

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
python -m uvicorn main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

## Documentación interactiva

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

## Base de datos

El proyecto utiliza SQLite mediante SQLAlchemy. La base de datos se genera automáticamente al ejecutar la aplicación por primera vez.

## Autor

**Samira Fernanda Guillen Cruz**

Proyecto desarrollado como práctica de una API REST con FastAPI implementando operaciones CRUD.
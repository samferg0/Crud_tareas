from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db

import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def inicio():
    return {"message": "¡Bienvenido a la API de FastAPI!"}


# Crear una tarea
@app.post("/tareas", response_model=schemas.TareaResponse)
def crear_tarea(
    tarea: schemas.TareaCreate,
    db: Session = Depends(get_db)
):
    nueva_tarea = models.Tarea(
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        prioridad=tarea.prioridad,
        estado=tarea.estado
    )

    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)

    return nueva_tarea


# Obtener todas las tareas
@app.get("/tareas", response_model=list[schemas.TareaResponse])
def obtener_tareas(
    db: Session = Depends(get_db)
):
    tareas = db.query(models.Tarea).all()
    return tareas


# Buscar tareas por título
@app.get("/tareas/buscar", response_model=list[schemas.TareaResponse])
def buscar_tarea(
    titulo: str,
    db: Session = Depends(get_db)
):
    tareas = db.query(models.Tarea).filter(
        models.Tarea.titulo.contains(titulo)
    ).all()

    return tareas


# Filtrar por prioridad
@app.get("/tareas/prioridad", response_model=list[schemas.TareaResponse])
def filtrar_prioridad(
    prioridad: str,
    db: Session = Depends(get_db)
):
    tareas = db.query(models.Tarea).filter(
        models.Tarea.prioridad.ilike(prioridad.strip())
    ).all()

    return tareas


# Filtrar por estado
@app.get("/tareas/estado", response_model=list[schemas.TareaResponse])
def filtrar_estado(
    estado: str,
    db: Session = Depends(get_db)
):
    tareas = db.query(models.Tarea).filter(
        models.Tarea.estado.ilike(estado.strip())
    ).all()

    return tareas


# Consultar una tarea por ID
@app.get("/tareas/{id}", response_model=schemas.TareaResponse)
def consultar_tarea(
    id: int,
    db: Session = Depends(get_db)
):
    tarea = db.query(models.Tarea).filter(
        models.Tarea.id == id
    ).first()

    if tarea is None:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return tarea


# Actualizar una tarea
@app.put("/tareas/{id}", response_model=schemas.TareaResponse)
def actualizar_tarea(
    id: int,
    tarea_actualizada: schemas.TareaCreate,
    db: Session = Depends(get_db)
):
    tarea = db.query(models.Tarea).filter(
        models.Tarea.id == id
    ).first()

    if tarea is None:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    tarea.titulo = tarea_actualizada.titulo
    tarea.descripcion = tarea_actualizada.descripcion
    tarea.prioridad = tarea_actualizada.prioridad
    tarea.estado = tarea_actualizada.estado

    db.commit()
    db.refresh(tarea)

    return tarea


# Eliminar una tarea
@app.delete("/tareas/{id}")
def eliminar_tarea(
    id: int,
    db: Session = Depends(get_db)
):
    tarea = db.query(models.Tarea).filter(
        models.Tarea.id == id
    ).first()

    if tarea is None:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    db.delete(tarea)
    db.commit()

    return {"message": "Tarea eliminada con éxito"}


# Marcar una tarea como completada
@app.put("/tareas/{id}/completar", response_model=schemas.TareaResponse)
def completar_tarea(
    id: int,
    db: Session = Depends(get_db)
):
    tarea = db.query(models.Tarea).filter(
        models.Tarea.id == id
    ).first()

    if tarea is None:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    tarea.estado = "Completada"

    db.commit()
    db.refresh(tarea)

    return tarea
from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime


class Tarea(Base):



    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    descripcion = Column(String(300))
    prioridad = Column(String(20))
    estado = Column(String(20))
    fecha_creacion = Column(DateTime, default=datetime.now)


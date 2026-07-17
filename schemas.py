from pydantic import BaseModel
from datetime import datetime




class TareaBase(BaseModel):
    titulo: str
    descripcion: str
    prioridad: str
    estado: str



class TareaCreate(TareaBase):
    pass


class TareaResponse(TareaBase):
    id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True
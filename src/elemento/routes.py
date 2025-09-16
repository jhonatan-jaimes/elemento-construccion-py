from fastapi import APIRouter
from pydantic import BaseModel, Field
from src.elementos import ElementoEntity
from src.elemento import elemento_service
from src.placa import PlacaEntity

router = APIRouter(prefix="/elemento")
service = elemento_service


class Element(BaseModel):
    id: int = Field(default=0)
    name: str = Field(default="")
    lot: int = Field(default=0)
    material: str = Field(default="")


@router.post("/save")
def save_elemento(elemento: Element):
    if elemento.lot > 0:
        ele = ElementoEntity(
            elemento.id,
            elemento.name,
            elemento.lot
        )
        service.save_elemento(ele)
        return {"message": "guardado"}
    elif elemento.material != "":
        ele = PlacaEntity(
            elemento.id,
            elemento.name,
            elemento.lot
        )
        service.save_elemento(ele)
        return {"message": "guardado"}
    else:
        return {"message": "No se puede guardar"}


@router.get("/get-all")
def get_elementos():
    return service.get_elementos()

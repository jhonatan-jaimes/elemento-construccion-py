from fastapi import APIRouter

router = APIRouter(prefix="/elemento", tags=["elemento"])


@router.get("/passsos")
def get_elemento():
    return {"message": "Todos los elementos guardados en la base de datos"}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.api.deps import get_db
from src.crud import maquina as maquina_crud #traigo todos los metodos que voy a definir en maquina(crud)
from src.schemas import maquina as maquina_schema


router = APIRouter()

@router.get('/', response_model = List[maquina_schema.Maquina])
def read_maquinas(db: Session = Depends(get_db)):  #para traer las maquinas utilice la funcion get_db
    return maquina_crud.get_maquinas(db)

@router.get('/{id}', response_model = maquina_schema.Maquina)
def read_maquina_id( id : int, db: Session = Depends(get_db)):
    maquina_id = maquina_crud.get_maquina_id(db, id = id)
    if maquina_id is None:
        raise HTTPException(status_code = 404, detail = 'Maquina no encontrada')
    return maquina_id
    

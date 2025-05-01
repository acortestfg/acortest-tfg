from sqlalchemy.orm import Session
from src.models.maquinas import Maquinas
from src.schemas.maquina import MaquinaCreate

def get_maquinas(db: Session):
    return db.query(Maquinas).all() #AQUI ESTOY COGIENDO TODAS LAS MAQUINAS DE LA BASE DE DATOS

def get_maquina_id(db: Session, id : int):
    return db.query(Maquinas).filter(Maquinas.id == id).first() #AQUI ESTOY CONSULTANDO A LA BASE DE DATOS

#def create_machine(db: Session, maquina: MaquinaCreate):
    #db_maquina = 

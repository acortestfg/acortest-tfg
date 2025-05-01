from pydantic import BaseModel

class MaquinaBase(BaseModel):
    name : str
    ubication : str

class Maquina(MaquinaBase):
    id : int

    class Config:
        from_attributes = True

class MaquinaCreate(MaquinaBase):
    pass #TIENE LO MISMO QUE MaquinaBase, es decir, name y ubication
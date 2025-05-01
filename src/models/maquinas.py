from sqlite3 import Cursor
from sqlalchemy import Column, BigInteger, String
from src.db.base_class import Base
from sqlalchemy.orm import relationship


class Maquinas(Base):
    id = Column(BigInteger, primary_key = True, index = True)
    name = Column(String, unique = True, index = True)
    ubication = Column(String, nullable = False)

    #Relacion con MaquinaProducto
    #productos = relationship("MaquinaProducto", back_populates = "maquina")
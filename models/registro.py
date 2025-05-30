from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

class RegistroCliente(Base):
    __tablename__ = 'registro_cliente'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    celular = Column(String(20), nullable=False)

engine = create_engine('sqlite:///crudregistro.db')
Base.metadata.create_all(engine)

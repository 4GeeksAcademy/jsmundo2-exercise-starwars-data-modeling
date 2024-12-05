import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla Usuario
class usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    edad = Column(Integer)
    correo = Column(String(250), unique=True, nullable=False)
    favoritos = relationship("favorito", back_populates="usuario")

# Tabla Personaje
class personaje(Base):
     __tablename__ = 'personaje'
     id = Column(Integer, primary_key=True)
     nombre = Column(String(250), nullable=False)
     edad = Column(Integer)
     raza = Column(String(250))
     altura = Column(String(250))
     color_piel = Column(String(250))

# # Tabla Vehículos
class vihicles(Base):
     __tablename__ = 'vihicles'
     id = Column(Integer, primary_key=True)
     nombre = Column(String(100), nullable=False)
     tripulacion = Column(Integer)
     capacidad_carga = Column(Integer)
     fabricante = Column(String(100), nullable=False)

 # Tabla Planetas
class planetas(Base):
     __tablename__ = 'planetas'
     id = Column(Integer, primary_key=True)
     nombre = Column(String(100), nullable=False)
     clima = Column(String(50), nullable=True)
     terreno = Column(String(50), nullable=False)

 # Tabla Armas
class armas(Base):
     __tablename__ = 'armas'
     id = Column(Integer, primary_key=True)
     nombre = Column(String(80), nullable=False)
     tamano = Column(String(70), nullable=False)
     creada_porquien = Column(String(300), nullable=False)

 # Tabla Favorito
class favorito(Base):
     __tablename__ = 'favorito'
     id = Column(Integer, primary_key=True)
     usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
     personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
     vehicles_id = Column(Integer, ForeignKey('vihicles.id'), nullable=True)
     planeta_id = Column(Integer, ForeignKey('planetas.id'), nullable=True)
     armas_id = Column(Integer, ForeignKey('armas.id'), nullable=True)

     usuario = relationship("usuario", back_populates="favoritos")

# Método to_dict
     def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

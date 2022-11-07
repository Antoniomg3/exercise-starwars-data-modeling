import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}

class Usuario(Base):

    __tablename__ = 'Usuario'    
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Apellidos = Column(String(250))
    Email = Column(String(250))
    Nick = Column(String(250))
    Constraseña = Column(String(250))
    Birthday = Column(Integer)

class Favoritos(Base):

    __tablename__ = 'Favoritos'    
    id = Column(Integer, primary_key=True)
    User_Id = Column(Integer, ForeignKey('Usuario.id'))
    Planetas_Fav = Column(Integer)
    Personajes_Fav = Column(Integer)
    Vehiculos_Fav = Column(Integer)
    Favoritos = relationship(Usuario)

class Planetas(Base):

    __tablename__ = 'Planetas'    
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Planeta_Id= Column(Integer, ForeignKey('Favoritos.Planetas_Fav'))
    Planetas = relationship(Favoritos)

class Personajes(Base):

    __tablename__ = 'Personajes'    
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Planeta_Id= Column(Integer, ForeignKey('Favoritos.Personajes_Fav'))
    Personajes = relationship(Favoritos)

class Vehiculos(Base):

    __tablename__ = 'Vehiculos'    
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Planeta_Id= Column(Integer, ForeignKey('Favoritos.Vehiculos_Fav'))
    Vehiculos = relationship(Favoritos)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
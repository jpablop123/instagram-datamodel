import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class  Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombreusuario = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Seguidores(Base):
    __tablename__ = 'seguidores'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    users_from_id = Column(Integer, ForeignKey('users.id'))
    users_to_id = Column(Integer, ForeignKey('users.id'))

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))

class Comentarios(Base):
    __tablename__ = 'comentarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comentarios_text = Column(String(250), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    media_type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    users_id = Column(Integer, ForeignKey('users.id'))
    favorite_folders = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

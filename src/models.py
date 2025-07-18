from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    favoritos_planetas = db.relationship("FavoritosPlanetas", back_populates="usuario", cascade="all, delete-orphan")
    favoritos_personajes = db.relationship("FavoritosPersonajes", back_populates="usuario", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # do not serialize the password, its a security breach
        }

class Planetas(db.Model):
    __tablename__ = 'planetas'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    clima: Mapped[str] = mapped_column(nullable=False)
    poblacion: Mapped[str] = mapped_column(nullable=False)
    diametro: Mapped[str] = mapped_column(nullable=True)
    periodo_rotacion: Mapped[str] = mapped_column(nullable=True)
    periodo_orbital: Mapped[str] = mapped_column(nullable=True)
    gravedad: Mapped[str] = mapped_column(nullable=True)
    terreno: Mapped[str] = mapped_column(nullable=True)
    superficie_agua: Mapped[str] = mapped_column(nullable=True)

    favoritos = relationship("FavoritosPlanetas", back_populates="planeta", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "poblacion": self.poblacion,
            "diametro": self.diametro,
            "periodo_rotacion": self.periodo_rotacion,
            "periodo_orbital": self.periodo_orbital,
            "gravedad": self.gravedad,
            "terreno": self.terreno,
            "superficie_agua": self.superficie_agua,
        }

class Personajes(db.Model):
    __tablename__ = 'personajes'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    altura: Mapped[str] = mapped_column(nullable=False)
    peso: Mapped[str] = mapped_column(nullable=False)
    color_cabello: Mapped[str] = mapped_column(nullable=False)
    color_piel: Mapped[str] = mapped_column(nullable=False)
    color_ojos: Mapped[str] = mapped_column(nullable=False)
    año_nacimiento: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)

    favoritos = relationship("FavoritosPersonajes", back_populates="personaje", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "peso": self.peso,
            "color_cabello": self.color_cabello,
            "color_piel": self.color_piel,
            "color_ojos": self.color_ojos,
            "año_nacimiento": self.año_nacimiento,
            "genero": self.genero,
        }

class FavoritosPlanetas(db.Model):
    __tablename__ = 'favoritos_planetas'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=False)
    id_planeta: Mapped[int] = mapped_column(ForeignKey('planetas.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="favoritos_planetas")
    planeta = relationship("Planetas", back_populates="favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_planeta": self.id_planeta,
            "planeta": self.planeta.serialize() if self.planeta else None
        }

class FavoritosPersonajes(db.Model):
    __tablename__ = 'favoritos_personajes'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=False)
    id_personaje: Mapped[int] = mapped_column(ForeignKey('personajes.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="favoritos_personajes")
    personaje = relationship("Personajes", back_populates="favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_personaje": self.id_personaje,
            "personaje": self.personaje.serialize() if self.personaje else None
        }
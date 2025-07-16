from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True, nullable=False)

    # Relationships
    favoritos_planetas = relationship("Favoritos_Planetas", back_populates="usuario", cascade="all, delete-orphan")
    favoritos_personajes = relationship("Favoritos_Personajes", back_populates="usuario", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class Planetas(db.Model):
    __tablename__ = 'planetas'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    clima: Mapped[str] = mapped_column(String(120), nullable=False)
    poblacion: Mapped[str] = mapped_column(String(120), nullable=False)
    terreno: Mapped[str] = mapped_column(String(120), nullable=False)
    diametro: Mapped[str] = mapped_column(String(120), nullable=False)
    
    # Relationships
    favoritos_planetas = relationship("Favoritos_Planetas", back_populates="planeta", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "poblacion": self.poblacion,
            "terreno": self.terreno,
            "diametro": self.diametro
        }

class Personajes(db.Model):
    __tablename__ = 'personajes'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    color_cabello: Mapped[str] = mapped_column(String(120), nullable=False)
    color_ojos: Mapped[str] = mapped_column(String(120), nullable=False)
    altura: Mapped[str] = mapped_column(String(120), nullable=False)
    peso: Mapped[str] = mapped_column(String(120), nullable=False)
    genero: Mapped[str] = mapped_column(String(120), nullable=False)
    
    # Relationships
    favoritos_personajes = relationship("Favoritos_Personajes", back_populates="personaje", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "color_cabello": self.color_cabello,
            "color_ojos": self.color_ojos,
            "altura": self.altura,
            "peso": self.peso,
            "genero": self.genero
        }

class Favoritos_Planetas(db.Model):
    __tablename__ = 'favoritos_planetas'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    planeta_id: Mapped[int] = mapped_column(ForeignKey("planetas.id"), nullable=False)

    # Relationships
    usuario = relationship("Usuario", back_populates="favoritos_planetas")
    planeta = relationship("Planetas", back_populates="favoritos_planetas")

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id,
            "usuario": self.usuario.serialize() if self.usuario else None,
            "planeta": self.planeta.serialize() if self.planeta else None
        }

class Favoritos_Personajes(db.Model):
    __tablename__ = 'favoritos_personajes'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    personaje_id: Mapped[int] = mapped_column(ForeignKey("personajes.id"), nullable=False)

    # Relationships
    usuario = relationship("Usuario", back_populates="favoritos_personajes")
    personaje = relationship("Personajes", back_populates="favoritos_personajes")

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id,
            "usuario": self.usuario.serialize() if self.usuario else None,
            "personaje": self.personaje.serialize() if self.personaje else None
        }

# Alias for backward compatibility with existing admin.py
User = Usuario
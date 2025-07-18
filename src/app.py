"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Usuario, Planetas, Personajes, FavoritosPersonajes, FavoritosPlanetas

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///starwars.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# ENDPOINTS DE USUARIOS
@app.route('/users', methods=['GET'])
def get_users():
    """Listar todos los usuarios del blog"""
    try:
        users = Usuario.query.all()
        return jsonify([user.serialize() for user in users]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_user_favorites(user_id):
    """Listar todos los favoritos que pertenecen al usuario actual"""
    try:
        user = Usuario.query.get(user_id)
        if not user:
            raise APIException("Usuario no encontrado", status_code=404)
        
        favoritos_planetas = FavoritosPlanetas.query.filter_by(id_usuario=user_id).all()
        favoritos_personajes = FavoritosPersonajes.query.filter_by(id_usuario=user_id).all()
        
        favorites = {
            "planetas": [fav.serialize() for fav in favoritos_planetas],
            "personajes": [fav.serialize() for fav in favoritos_personajes]
        }
        
        return jsonify(favorites), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ENDPOINTS DE PLANETAS
@app.route('/planets', methods=['GET'])
def get_planets():
    """Listar todos los registros de planetas en la base de datos"""
    try:
        planets = Planetas.query.all()
        return jsonify([planet.serialize() for planet in planets]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    """Muestra la información de un solo planeta según su id"""
    try:
        planet = Planetas.query.get(planet_id)
        if not planet:
            raise APIException("Planeta no encontrado", status_code=404)
        return jsonify(planet.serialize()), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ENDPOINTS DE PERSONAJES
@app.route('/people', methods=['GET'])
def get_people():
    """Listar todos los registros de personajes en la base de datos"""
    try:
        people = Personajes.query.all()
        return jsonify([person.serialize() for person in people]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    """Muestra la información de un solo personaje según su id"""
    try:
        person = Personajes.query.get(people_id)
        if not person:
            raise APIException("Personaje no encontrado", status_code=404)
        return jsonify(person.serialize()), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ENDPOINTS DE FAVORITOS
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    """Añade un nuevo planeta favorito al usuario actual"""
    try:
        # Para simplificar, usamos el primer usuario como "usuario actual"
        # En una implementación real, esto vendría del token de autenticación
        user = Usuario.query.first()
        if not user:
            raise APIException("No hay usuarios en el sistema", status_code=404)
        
        planet = Planetas.query.get(planet_id)
        if not planet:
            raise APIException("Planeta no encontrado", status_code=404)
        
        # Verificar si ya existe en favoritos
        existing_favorite = FavoritosPlanetas.query.filter_by(
            id_usuario=user.id, 
            id_planeta=planet_id
        ).first()
        
        if existing_favorite:
            raise APIException("Este planeta ya está en favoritos", status_code=400)
        
        new_favorite = FavoritosPlanetas(
            id_usuario=user.id,
            id_planeta=planet_id
        )
        
        db.session.add(new_favorite)
        db.session.commit()
        
        return jsonify({"message": "Planeta añadido a favoritos", "favorite": new_favorite.serialize()}), 201
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_person(people_id):
    """Añade un nuevo personaje favorito al usuario actual"""
    try:
        # Para simplificar, usamos el primer usuario como "usuario actual"
        user = Usuario.query.first()
        if not user:
            raise APIException("No hay usuarios en el sistema", status_code=404)
        
        person = Personajes.query.get(people_id)
        if not person:
            raise APIException("Personaje no encontrado", status_code=404)
        
        # Verificar si ya existe en favoritos
        existing_favorite = FavoritosPersonajes.query.filter_by(
            id_usuario=user.id, 
            id_personaje=people_id
        ).first()
        
        if existing_favorite:
            raise APIException("Este personaje ya está en favoritos", status_code=400)
        
        new_favorite = FavoritosPersonajes(
            id_usuario=user.id,
            id_personaje=people_id
        )
        
        db.session.add(new_favorite)
        db.session.commit()
        
        return jsonify({"message": "Personaje añadido a favoritos", "favorite": new_favorite.serialize()}), 201
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    """Elimina un planeta favorito con el id = planet_id"""
    try:
        # Para simplificar, usamos el primer usuario como "usuario actual"
        user = Usuario.query.first()
        if not user:
            raise APIException("No hay usuarios en el sistema", status_code=404)
        
        favorite = FavoritosPlanetas.query.filter_by(
            id_usuario=user.id, 
            id_planeta=planet_id
        ).first()
        
        if not favorite:
            raise APIException("Este planeta no está en favoritos", status_code=404)
        
        db.session.delete(favorite)
        db.session.commit()
        
        return jsonify({"message": "Planeta eliminado de favoritos"}), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_person(people_id):
    """Elimina un personaje favorito con el id = people_id"""
    try:
        # Para simplificar, usamos el primer usuario como "usuario actual"
        user = Usuario.query.first()
        if not user:
            raise APIException("No hay usuarios en el sistema", status_code=404)
        
        favorite = FavoritosPersonajes.query.filter_by(
            id_usuario=user.id, 
            id_personaje=people_id
        ).first()
        
        if not favorite:
            raise APIException("Este personaje no está en favoritos", status_code=404)
        
        db.session.delete(favorite)
        db.session.commit()
        
        return jsonify({"message": "Personaje eliminado de favoritos"}), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# ENDPOINTS ADICIONALES PARA ADMINISTRACIÓN (BONUS)
@app.route('/planets', methods=['POST'])
def create_planet():
    """Crear un nuevo planeta"""
    try:
        data = request.get_json()
        
        if not data or not data.get('nombre'):
            raise APIException("El nombre del planeta es requerido", status_code=400)
        
        new_planet = Planetas(
            nombre=data.get('nombre'),
            clima=data.get('clima', 'unknown'),
            poblacion=data.get('poblacion', 'unknown'),
            diametro=data.get('diametro', 'unknown'),
            periodo_rotacion=data.get('periodo_rotacion', 'unknown'),
            periodo_orbital=data.get('periodo_orbital', 'unknown'),
            gravedad=data.get('gravedad', 'unknown'),
            terreno=data.get('terreno', 'unknown'),
            superficie_agua=data.get('superficie_agua', 'unknown')
        )
        
        db.session.add(new_planet)
        db.session.commit()
        
        return jsonify({"message": "Planeta creado exitosamente", "planet": new_planet.serialize()}), 201
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/people', methods=['POST'])
def create_person():
    """Crear un nuevo personaje"""
    try:
        data = request.get_json()
        
        if not data or not data.get('nombre'):
            raise APIException("El nombre del personaje es requerido", status_code=400)
        
        new_person = Personajes(
            nombre=data.get('nombre'),
            altura=data.get('altura', 'unknown'),
            peso=data.get('peso', 'unknown'),
            color_cabello=data.get('color_cabello', 'unknown'),
            color_piel=data.get('color_piel', 'unknown'),
            color_ojos=data.get('color_ojos', 'unknown'),
            año_nacimiento=data.get('año_nacimiento', 'unknown'),
            genero=data.get('genero', 'unknown')
        )
        
        db.session.add(new_person)
        db.session.commit()
        
        return jsonify({"message": "Personaje creado exitosamente", "person": new_person.serialize()}), 201
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    """Actualizar un planeta existente"""
    try:
        planet = Planetas.query.get(planet_id)
        if not planet:
            raise APIException("Planeta no encontrado", status_code=404)
        
        data = request.get_json()
        if not data:
            raise APIException("No se proporcionaron datos para actualizar", status_code=400)
        
        # Actualizar campos si están presentes en los datos
        if 'nombre' in data:
            planet.nombre = data['nombre']
        if 'clima' in data:
            planet.clima = data['clima']
        if 'poblacion' in data:
            planet.poblacion = data['poblacion']
        if 'diametro' in data:
            planet.diametro = data['diametro']
        if 'periodo_rotacion' in data:
            planet.periodo_rotacion = data['periodo_rotacion']
        if 'periodo_orbital' in data:
            planet.periodo_orbital = data['periodo_orbital']
        if 'gravedad' in data:
            planet.gravedad = data['gravedad']
        if 'terreno' in data:
            planet.terreno = data['terreno']
        if 'superficie_agua' in data:
            planet.superficie_agua = data['superficie_agua']
        
        db.session.commit()
        
        return jsonify({"message": "Planeta actualizado exitosamente", "planet": planet.serialize()}), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/people/<int:people_id>', methods=['PUT'])
def update_person(people_id):
    """Actualizar un personaje existente"""
    try:
        person = Personajes.query.get(people_id)
        if not person:
            raise APIException("Personaje no encontrado", status_code=404)
        
        data = request.get_json()
        if not data:
            raise APIException("No se proporcionaron datos para actualizar", status_code=400)
        
        # Actualizar campos si están presentes en los datos
        if 'nombre' in data:
            person.nombre = data['nombre']
        if 'altura' in data:
            person.altura = data['altura']
        if 'peso' in data:
            person.peso = data['peso']
        if 'color_cabello' in data:
            person.color_cabello = data['color_cabello']
        if 'color_piel' in data:
            person.color_piel = data['color_piel']
        if 'color_ojos' in data:
            person.color_ojos = data['color_ojos']
        if 'año_nacimiento' in data:
            person.año_nacimiento = data['año_nacimiento']
        if 'genero' in data:
            person.genero = data['genero']
        
        db.session.commit()
        
        return jsonify({"message": "Personaje actualizado exitosamente", "person": person.serialize()}), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    """Eliminar un planeta"""
    try:
        planet = Planetas.query.get(planet_id)
        if not planet:
            raise APIException("Planeta no encontrado", status_code=404)
        
        db.session.delete(planet)
        db.session.commit()
        
        return jsonify({"message": "Planeta eliminado exitosamente"}), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/people/<int:people_id>', methods=['DELETE'])
def delete_person(people_id):
    """Eliminar un personaje"""
    try:
        person = Personajes.query.get(people_id)
        if not person:
            raise APIException("Personaje no encontrado", status_code=404)
        
        db.session.delete(person)
        db.session.commit()
        
        return jsonify({"message": "Personaje eliminado exitosamente"}), 200
    except APIException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
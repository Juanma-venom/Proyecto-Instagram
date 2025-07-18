#!/usr/bin/env python3
"""
Prueba rápida de la API de StarWars
"""
import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app import app, db
from models import Usuario, Planetas, Personajes, FavoritosPlanetas, FavoritosPersonajes

def test_api():
    """Prueba rápida de la API"""
    with app.app_context():
        print("🧪 Probando la API de StarWars...")
        
        # Probar que las tablas existen y tienen datos
        try:
            usuarios = Usuario.query.all()
            print(f"✅ Usuarios: {len(usuarios)} encontrados")
            
            planetas = Planetas.query.all()
            print(f"✅ Planetas: {len(planetas)} encontrados")
            
            personajes = Personajes.query.all()
            print(f"✅ Personajes: {len(personajes)} encontrados")
            
            # Probar relaciones
            if usuarios and planetas:
                usuario = usuarios[0]
                planeta = planetas[0]
                
                # Crear un favorito de prueba
                favorito = FavoritosPlanetas(id_usuario=usuario.id, id_planeta=planeta.id)
                db.session.add(favorito)
                db.session.commit()
                
                print(f"✅ Favorito creado: Usuario {usuario.username} -> Planeta {planeta.nombre}")
                
                # Verificar que la relación funciona
                favoritos = FavoritosPlanetas.query.filter_by(id_usuario=usuario.id).all()
                print(f"✅ Favoritos del usuario: {len(favoritos)}")
                
                # Limpiar
                db.session.delete(favorito)
                db.session.commit()
                
            print("🎉 ¡Todas las pruebas pasaron!")
            print("\n📋 Resumen de datos:")
            print(f"   - {len(usuarios)} usuarios")
            print(f"   - {len(planetas)} planetas")
            print(f"   - {len(personajes)} personajes")
            
            print("\n🚀 La API está lista para usar!")
            print("   Ejecuta: python3 start_server.py")
            print("   URL: http://localhost:3000")
            print("   Admin: http://localhost:3000/admin")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        
        return True

if __name__ == "__main__":
    success = test_api()
    sys.exit(0 if success else 1)
#!/usr/bin/env python3
"""
Script de prueba para la API de StarWars
Prueba todos los endpoints principales
"""

import requests
import json
import time
import sys

# Configuración
BASE_URL = "http://localhost:3000"
TIMEOUT = 10

def test_endpoint(method, endpoint, data=None, expected_status=200):
    """Prueba un endpoint específico"""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=TIMEOUT)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=TIMEOUT)
        elif method == "PUT":
            response = requests.put(url, json=data, timeout=TIMEOUT)
        elif method == "DELETE":
            response = requests.delete(url, timeout=TIMEOUT)
        
        success = response.status_code == expected_status
        
        print(f"[{'✓' if success else '✗'}] {method} {endpoint} - Status: {response.status_code}")
        
        if not success:
            print(f"    Error: {response.text}")
        elif response.status_code == 200 and method == "GET":
            try:
                data = response.json()
                if isinstance(data, list):
                    print(f"    Resultados: {len(data)} elementos")
                else:
                    print(f"    Respuesta: {type(data).__name__}")
            except:
                print(f"    Respuesta: {len(response.text)} caracteres")
        
        return success, response
    
    except requests.exceptions.RequestException as e:
        print(f"[✗] {method} {endpoint} - Error de conexión: {e}")
        return False, None

def main():
    """Función principal de pruebas"""
    print("🚀 Iniciando pruebas de la API de StarWars")
    print("=" * 50)
    
    # Verificar que el servidor esté funcionando
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        print(f"✓ Servidor disponible en {BASE_URL}")
    except:
        print(f"✗ No se puede conectar al servidor en {BASE_URL}")
        print("Asegúrate de que la aplicación esté ejecutándose con: python3 app.py")
        sys.exit(1)
    
    print("\n📋 Probando endpoints principales...")
    
    # Pruebas de lectura
    tests = [
        ("GET", "/users", None, 200),
        ("GET", "/planets", None, 200),
        ("GET", "/people", None, 200),
        ("GET", "/planets/1", None, 200),
        ("GET", "/people/1", None, 200),
        ("GET", "/users/1/favorites", None, 200),
    ]
    
    passed = 0
    total = len(tests)
    
    for method, endpoint, data, expected_status in tests:
        success, response = test_endpoint(method, endpoint, data, expected_status)
        if success:
            passed += 1
        time.sleep(0.5)  # Pausa entre pruebas
    
    print(f"\n📊 Resultados: {passed}/{total} pruebas pasaron")
    
    # Pruebas de escritura (opcionales)
    print("\n🔧 Probando endpoints de escritura...")
    
    # Agregar planeta a favoritos
    success, response = test_endpoint("POST", "/favorite/planet/1", None, 201)
    if success:
        print("    ✓ Planeta agregado a favoritos")
    
    # Agregar personaje a favoritos
    success, response = test_endpoint("POST", "/favorite/people/1", None, 201)
    if success:
        print("    ✓ Personaje agregado a favoritos")
    
    # Verificar favoritos
    success, response = test_endpoint("GET", "/users/1/favorites", None, 200)
    if success and response:
        try:
            favorites = response.json()
            print(f"    ✓ Favoritos del usuario: {len(favorites.get('planetas', []))} planetas, {len(favorites.get('personajes', []))} personajes")
        except:
            pass
    
    # Crear nuevo planeta
    new_planet = {
        "nombre": "Planeta de Prueba",
        "clima": "templado",
        "poblacion": "1000000",
        "diametro": "12000",
        "periodo_rotacion": "24",
        "periodo_orbital": "365",
        "gravedad": "1 standard",
        "terreno": "montañas, océanos",
        "superficie_agua": "70"
    }
    
    success, response = test_endpoint("POST", "/planets", new_planet, 201)
    if success:
        print("    ✓ Nuevo planeta creado")
    
    print("\n🎉 Pruebas completadas!")
    print("\n📚 Endpoints disponibles:")
    print("  GET    /users                     - Listar usuarios")
    print("  GET    /users/<id>/favorites      - Favoritos del usuario")
    print("  GET    /planets                   - Listar planetas")
    print("  GET    /planets/<id>              - Obtener planeta")
    print("  POST   /planets                   - Crear planeta")
    print("  PUT    /planets/<id>              - Actualizar planeta")
    print("  DELETE /planets/<id>              - Eliminar planeta")
    print("  GET    /people                    - Listar personajes")
    print("  GET    /people/<id>               - Obtener personaje")
    print("  POST   /people                    - Crear personaje")
    print("  PUT    /people/<id>               - Actualizar personaje")
    print("  DELETE /people/<id>               - Eliminar personaje")
    print("  POST   /favorite/planet/<id>      - Agregar planeta a favoritos")
    print("  POST   /favorite/people/<id>      - Agregar personaje a favoritos")
    print("  DELETE /favorite/planet/<id>      - Eliminar planeta de favoritos")
    print("  DELETE /favorite/people/<id>      - Eliminar personaje de favoritos")
    print("  GET    /admin                     - Panel de administración")

if __name__ == "__main__":
    main()
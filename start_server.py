#!/usr/bin/env python3
"""
Script para iniciar el servidor de la API de StarWars
"""

import os
import sys

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Importar y ejecutar la aplicación
from app import app

if __name__ == '__main__':
    print("🚀 Iniciando API de StarWars...")
    print("📍 Servidor disponible en: http://localhost:3000")
    print("🔧 Panel de administración: http://localhost:3000/admin")
    print("📖 Documentación: Ver README.md")
    print("⚡ Presiona Ctrl+C para detener el servidor")
    print("-" * 50)
    
    try:
        app.run(host='0.0.0.0', port=3000, debug=True)
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido. ¡Que la fuerza te acompañe!")
    except Exception as e:
        print(f"\n❌ Error al iniciar el servidor: {e}")
        sys.exit(1)
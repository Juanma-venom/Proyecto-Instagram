# Documentación de la API REST de StarWars

## 🚀 Inicio Rápido

### Instalación
```bash
# Instalar dependencias
pip install --user --break-system-packages Flask Flask-SQLAlchemy Flask-CORS Flask-Admin python-dotenv

# Poblar la base de datos
cd src && python3 seed_data.py

# Iniciar el servidor
python3 start_server.py
```

### URLs Principales
- **API Base**: `http://localhost:3000`
- **Panel Admin**: `http://localhost:3000/admin`
- **Documentación**: Este archivo

## 📚 Endpoints de la API

### 👥 Usuarios

#### Listar todos los usuarios
```http
GET /users
```
**Respuesta:**
```json
[
  {
    "id": 1,
    "username": "luke_skywalker"
  }
]
```

#### Obtener favoritos de un usuario
```http
GET /users/{user_id}/favorites
```
**Respuesta:**
```json
{
  "planetas": [
    {
      "id": 1,
      "id_usuario": 1,
      "id_planeta": 1,
      "planeta": {
        "id": 1,
        "nombre": "Tatooine",
        "clima": "arid",
        "poblacion": "200000"
      }
    }
  ],
  "personajes": [
    {
      "id": 1,
      "id_usuario": 1,
      "id_personaje": 1,
      "personaje": {
        "id": 1,
        "nombre": "Luke Skywalker",
        "altura": "172",
        "peso": "77"
      }
    }
  ]
}
```

### 🪐 Planetas

#### Listar todos los planetas
```http
GET /planets
```
**Respuesta:**
```json
[
  {
    "id": 1,
    "nombre": "Tatooine",
    "clima": "arid",
    "poblacion": "200000",
    "diametro": "10465",
    "periodo_rotacion": "23",
    "periodo_orbital": "304",
    "gravedad": "1 standard",
    "terreno": "desert",
    "superficie_agua": "1"
  }
]
```

#### Obtener un planeta específico
```http
GET /planets/{planet_id}
```

#### Crear un nuevo planeta
```http
POST /planets
Content-Type: application/json

{
  "nombre": "Jakku",
  "clima": "arid",
  "poblacion": "unknown",
  "diametro": "unknown",
  "periodo_rotacion": "unknown",
  "periodo_orbital": "unknown",
  "gravedad": "unknown",
  "terreno": "desert",
  "superficie_agua": "unknown"
}
```

#### Actualizar un planeta
```http
PUT /planets/{planet_id}
Content-Type: application/json

{
  "clima": "temperate",
  "poblacion": "1000000"
}
```

#### Eliminar un planeta
```http
DELETE /planets/{planet_id}
```

### 👤 Personajes

#### Listar todos los personajes
```http
GET /people
```
**Respuesta:**
```json
[
  {
    "id": 1,
    "nombre": "Luke Skywalker",
    "altura": "172",
    "peso": "77",
    "color_cabello": "blond",
    "color_piel": "fair",
    "color_ojos": "blue",
    "año_nacimiento": "19BBY",
    "genero": "male"
  }
]
```

#### Obtener un personaje específico
```http
GET /people/{people_id}
```

#### Crear un nuevo personaje
```http
POST /people
Content-Type: application/json

{
  "nombre": "Rey",
  "altura": "170",
  "peso": "54",
  "color_cabello": "brown",
  "color_piel": "light",
  "color_ojos": "hazel",
  "año_nacimiento": "15ABY",
  "genero": "female"
}
```

#### Actualizar un personaje
```http
PUT /people/{people_id}
Content-Type: application/json

{
  "altura": "171",
  "peso": "55"
}
```

#### Eliminar un personaje
```http
DELETE /people/{people_id}
```

### ⭐ Favoritos

#### Agregar planeta a favoritos
```http
POST /favorite/planet/{planet_id}
```
**Respuesta:**
```json
{
  "message": "Planeta añadido a favoritos",
  "favorite": {
    "id": 1,
    "id_usuario": 1,
    "id_planeta": 1,
    "planeta": {
      "id": 1,
      "nombre": "Tatooine",
      "clima": "arid"
    }
  }
}
```

#### Agregar personaje a favoritos
```http
POST /favorite/people/{people_id}
```

#### Eliminar planeta de favoritos
```http
DELETE /favorite/planet/{planet_id}
```

#### Eliminar personaje de favoritos
```http
DELETE /favorite/people/{people_id}
```

## 🔧 Códigos de Estado HTTP

- `200 OK` - Solicitud exitosa
- `201 Created` - Recurso creado exitosamente
- `400 Bad Request` - Datos inválidos
- `404 Not Found` - Recurso no encontrado
- `500 Internal Server Error` - Error del servidor

## 📋 Ejemplos de Uso con curl

### Obtener todos los planetas
```bash
curl -X GET http://localhost:3000/planets
```

### Crear un nuevo planeta
```bash
curl -X POST http://localhost:3000/planets \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Jakku",
    "clima": "arid",
    "poblacion": "unknown",
    "diametro": "unknown",
    "periodo_rotacion": "unknown",
    "periodo_orbital": "unknown",
    "gravedad": "unknown",
    "terreno": "desert",
    "superficie_agua": "unknown"
  }'
```

### Agregar planeta a favoritos
```bash
curl -X POST http://localhost:3000/favorite/planet/1
```

### Obtener favoritos de un usuario
```bash
curl -X GET http://localhost:3000/users/1/favorites
```

## 🧪 Pruebas

Para ejecutar las pruebas automatizadas:

```bash
# Asegúrate de que el servidor esté ejecutándose
python3 start_server.py

# En otra terminal, ejecuta las pruebas
pip install --user --break-system-packages requests
python3 test_api.py
```

## 🗄️ Estructura de la Base de Datos

### Tablas Principales
- **usuario**: Usuarios del sistema
- **planetas**: Planetas de StarWars
- **personajes**: Personajes de StarWars
- **favoritos_planetas**: Relación usuario-planeta favorito
- **favoritos_personajes**: Relación usuario-personaje favorito

### Datos de Ejemplo
La base de datos incluye:
- 3 usuarios de ejemplo
- 10 planetas icónicos de StarWars
- 20 personajes principales de StarWars

## 🚨 Notas Importantes

1. **Usuario Actual**: Por simplicidad, la API usa el primer usuario de la base de datos como "usuario actual" para las operaciones de favoritos.

2. **Autenticación**: Esta versión no incluye autenticación. En producción, se debería implementar JWT o similar.

3. **Validación**: Se incluye validación básica de datos. Se pueden agregar más validaciones según sea necesario.

4. **CORS**: Habilitado para permitir peticiones desde cualquier origen.

## 🔗 Panel de Administración

Accede a `http://localhost:3000/admin` para:
- Ver todos los datos en formato tabular
- Agregar nuevos registros
- Editar registros existentes
- Eliminar registros

## 🐛 Solución de Problemas

### Error de conexión
- Verifica que el servidor esté ejecutándose
- Comprueba que el puerto 3000 esté disponible

### Error de base de datos
- Ejecuta `python3 seed_data.py` para recrear la base de datos
- Verifica que el archivo `starwars.db` se haya creado

### Error de dependencias
- Instala las dependencias: `pip install --user --break-system-packages Flask Flask-SQLAlchemy Flask-CORS Flask-Admin python-dotenv`

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

¡Que la fuerza te acompañe! 🌟
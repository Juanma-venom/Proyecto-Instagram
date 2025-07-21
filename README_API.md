# API Estática de Familia Jackson

Una API REST construida con Flask para gestionar los miembros de la familia Jackson.

## 🚀 Instalación y Configuración

### Método 1: Usando pipenv (Recomendado)
```bash
# Instalar dependencias
pipenv install

# Activar el entorno virtual
pipenv shell

# Iniciar el servidor
pipenv run start
```

### Método 2: Usando pip
```bash
# Instalar dependencias
pip3 install -r requirements.txt

# Iniciar el servidor
python3 src/app.py
```

### Método 3: Usando el archivo app.py del directorio raíz
```bash
# Instalar Flask
pip3 install flask

# Ejecutar la aplicación
python3 app.py
```

## 🧪 Ejecutar Pruebas
```bash
# Con pipenv
pipenv run test

# Con pytest directamente
python -m pytest tests/ -v
```

## 📊 Estructura de Datos

Cada miembro de la familia Jackson es representado como un diccionario con los siguientes campos:

```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Jackson",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}
```

### Miembros Iniciales
- **John Jackson**: 33 años, números de la suerte: 7, 13, 22
- **Jane Jackson**: 35 años, números de la suerte: 10, 14, 3  
- **Jimmy Jackson**: 5 años, números de la suerte: 1

## 🔗 Endpoints de la API

### 1. Obtener Todos los Miembros
**GET** `/members`

Devuelve todos los miembros de la familia Jackson.

**Ejemplo de uso:**
```bash
curl -X GET http://localhost:3000/members
```

**Respuesta exitosa (200):**
```json
[
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Jackson",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Jackson",
        "age": 35,
        "lucky_numbers": [10, 14, 3]
    },
    {
        "id": 3,
        "first_name": "Jimmy",
        "last_name": "Jackson",
        "age": 5,
        "lucky_numbers": [1]
    }
]
```

### 2. Obtener un Miembro Específico
**GET** `/members/<int:member_id>`

Devuelve un miembro específico por su ID.

**Ejemplo de uso:**
```bash
curl -X GET http://localhost:3000/members/1
```

**Respuesta exitosa (200):**
```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Jackson",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}
```

**Respuesta de error (404):**
```json
{
    "error": "Member not found"
}
```

### 3. Agregar un Nuevo Miembro
**POST** `/members`

Agrega un nuevo miembro a la familia Jackson.

**Content-Type:** `application/json`

**Cuerpo de la petición:**
```json
{
    "first_name": "Jack",
    "age": 25,
    "lucky_numbers": [5, 9]
}
```

**Ejemplo de uso:**
```bash
curl -X POST http://localhost:3000/members \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Jack", "age": 25, "lucky_numbers": [5, 9]}'
```

**Respuesta exitosa (200):**
```json
{
    "id": 4,
    "first_name": "Jack",
    "last_name": "Jackson",
    "age": 25,
    "lucky_numbers": [5, 9]
}
```

**Respuesta de error (400):**
```json
{
    "error": "Missing required field: first_name"
}
```

### 4. Eliminar un Miembro
**DELETE** `/members/<int:member_id>`

Elimina un miembro específico de la familia.

**Ejemplo de uso:**
```bash
curl -X DELETE http://localhost:3000/members/1
```

**Respuesta exitosa (200):**
```json
{
    "done": true
}
```

**Respuesta de error (404):**
```json
{
    "error": "Member not found"
}
```

## 🔧 Códigos de Estado HTTP

- **200**: Operación exitosa
- **400**: Error en la petición del cliente (datos faltantes o inválidos)
- **404**: Recurso no encontrado
- **500**: Error interno del servidor

## 🧪 Probando con Hoppscotch o Postman

### Configuración Base
- **URL Base**: `http://localhost:3000`
- **Content-Type**: `application/json` (para peticiones POST)

### Ejemplos de Pruebas

1. **Obtener todos los miembros:**
   - Método: GET
   - URL: `http://localhost:3000/members`

2. **Obtener un miembro específico:**
   - Método: GET
   - URL: `http://localhost:3000/members/1`

3. **Agregar un nuevo miembro:**
   - Método: POST
   - URL: `http://localhost:3000/members`
   - Headers: `Content-Type: application/json`
   - Body:
     ```json
     {
         "first_name": "Sarah",
         "age": 28,
         "lucky_numbers": [3, 7, 11]
     }
     ```

4. **Eliminar un miembro:**
   - Método: DELETE
   - URL: `http://localhost:3000/members/1`

## 📁 Estructura del Proyecto

```
project/
├── src/
│   ├── app.py              # API Flask con endpoints
│   └── datastructure.py    # Clase FamilyStructure
├── tests/
│   └── test_api.py         # Pruebas unitarias
├── app.py                  # Punto de entrada principal
├── Pipfile                 # Dependencias pipenv
├── requirements.txt        # Dependencias pip
└── README_API.md          # Esta documentación
```

## ⚠️ Notas Importantes

- Esta API funciona completamente en memoria (RAM), los datos se pierden al reiniciar el servidor
- Todos los miembros tienen automáticamente el apellido "Jackson"
- Los IDs se generan automáticamente de forma incremental
- La API valida que se proporcionen todos los campos requeridos
- Se incluye manejo de errores para casos comunes

## 🎯 Funcionalidades Implementadas

- ✅ Estructura de datos FamilyStructure completa
- ✅ 4 endpoints REST funcionales
- ✅ Validación de datos de entrada
- ✅ Manejo de errores HTTP apropiados
- ✅ Respuestas en formato JSON
- ✅ Miembros iniciales precargados
- ✅ Pruebas unitarias incluidas
- ✅ Documentación completa
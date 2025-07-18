# API REST de StarWars

Una API REST completa para administrar un blog de StarWars que permite gestionar planetas, personajes y favoritos de usuarios.

## 🚀 Características

- **Gestión de Planetas**: Crear, leer, actualizar y eliminar planetas
- **Gestión de Personajes**: Crear, leer, actualizar y eliminar personajes
- **Sistema de Favoritos**: Añadir y eliminar favoritos por usuario
- **Gestión de Usuarios**: Listar usuarios y sus favoritos
- **Panel de Administración**: Interfaz web para gestionar datos
- **Base de Datos SQLite/PostgreSQL**: Soporte para ambos motores

## 📋 Requisitos

- Python 3.7+
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-Admin
- Flask-CORS

## 🛠️ Instalación

1. **Clonar el repositorio**
```bash
git clone <tu-repositorio>
cd starwars-api
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Configurar la base de datos**
```bash
cd src
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

4. **Poblar la base de datos con datos de ejemplo**
```bash
python seed_data.py
```

5. **Ejecutar la aplicación**
```bash
python app.py
```

La API estará disponible en `http://localhost:3000`

## 📚 Endpoints de la API

### Usuarios
- `GET /users` - Listar todos los usuarios
- `GET /users/<user_id>/favorites` - Obtener favoritos de un usuario

### Planetas
- `GET /planets` - Listar todos los planetas
- `GET /planets/<planet_id>` - Obtener un planeta específico
- `POST /planets` - Crear un nuevo planeta
- `PUT /planets/<planet_id>` - Actualizar un planeta
- `DELETE /planets/<planet_id>` - Eliminar un planeta

### Personajes
- `GET /people` - Listar todos los personajes
- `GET /people/<people_id>` - Obtener un personaje específico
- `POST /people` - Crear un nuevo personaje
- `PUT /people/<people_id>` - Actualizar un personaje
- `DELETE /people/<people_id>` - Eliminar un personaje

### Favoritos
- `POST /favorite/planet/<planet_id>` - Añadir planeta a favoritos
- `POST /favorite/people/<people_id>` - Añadir personaje a favoritos
- `DELETE /favorite/planet/<planet_id>` - Eliminar planeta de favoritos
- `DELETE /favorite/people/<people_id>` - Eliminar personaje de favoritos

## 📖 Ejemplos de Uso

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

### Añadir un planeta a favoritos
```bash
curl -X POST http://localhost:3000/favorite/planet/1
```

### Obtener favoritos de un usuario
```bash
curl -X GET http://localhost:3000/users/1/favorites
```

## 🔧 Estructura del Proyecto

```
starwars-api/
├── src/
│   ├── app.py              # Aplicación principal con endpoints
│   ├── models.py           # Modelos de la base de datos
│   ├── admin.py            # Configuración del panel de administración
│   ├── utils.py            # Utilidades y manejo de errores
│   └── seed_data.py        # Script para poblar la base de datos
├── migrations/             # Migraciones de la base de datos
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Documentación
```

## 🎯 Modelos de Datos

### Usuario
- `id`: Identificador único
- `username`: Nombre de usuario
- `password`: Contraseña (no se serializa)

### Planeta
- `id`: Identificador único
- `nombre`: Nombre del planeta
- `clima`: Tipo de clima
- `poblacion`: Número de habitantes
- `diametro`: Diámetro del planeta
- `periodo_rotacion`: Horas de rotación
- `periodo_orbital`: Días orbitales
- `gravedad`: Fuerza gravitacional
- `terreno`: Tipo de terreno
- `superficie_agua`: Porcentaje de agua

### Personaje
- `id`: Identificador único
- `nombre`: Nombre del personaje
- `altura`: Altura en centímetros
- `peso`: Peso en kilogramos
- `color_cabello`: Color del cabello
- `color_piel`: Color de la piel
- `color_ojos`: Color de los ojos
- `año_nacimiento`: Año de nacimiento
- `genero`: Género del personaje

## 🔐 Panel de Administración

Accede al panel de administración en `http://localhost:3000/admin` para gestionar los datos de forma visual.

## 🧪 Pruebas

Puedes probar todos los endpoints usando herramientas como:
- **Postman**: Importa la colección desde [este enlace](https://documenter.getpostman.com/view/2432393/TzRSgnTS)
- **curl**: Usando los ejemplos proporcionados arriba
- **Navegador**: Para endpoints GET

## 🌟 Características Adicionales

- **Validación de datos**: Todos los endpoints validan los datos de entrada
- **Manejo de errores**: Respuestas de error consistentes y descriptivas
- **CORS habilitado**: Permite peticiones desde cualquier origen
- **Relaciones de base de datos**: Modelos relacionados con claves foráneas
- **Serialización automática**: Conversión automática de modelos a JSON

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- Datos de StarWars basados en [SWAPI](https://swapi.dev/)
- Proyecto educativo de [4Geeks Academy](https://4geeksacademy.com/)

---

¡Que la fuerza te acompañe! 🌟

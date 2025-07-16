# StarWars Blog Database Project - Complete

## Project Overview
This project implements a corrected and improved database model for a StarWars blog application, addressing multiple issues found in the original code and providing a fully functional database structure.

## Files Created/Modified

### Core Files
- `src/models.py` - **Main database models** with corrected relationships and improved structure
- `diagram.py` - **Diagram generation script** to create ER diagrams
- `diagram.png` - **Generated database diagram** showing table relationships
- `Pipfile` - **Dependency management** for Python packages
- `tmp.db` - **SQLite database** with generated tables

### Documentation
- `CORRECTIONS_MADE.md` - **Detailed list of all fixes** applied to the original code
- `PROJECT_SUMMARY.md` - **This summary file**

## Database Schema

### Tables Implemented

1. **usuario** - User management
   - `id` (Primary Key)
   - `username` (Unique)
   - `password`
   - `email` (Unique)
   - `is_active` (Boolean)

2. **planetas** - Star Wars planets
   - `id` (Primary Key)
   - `nombre` (Planet name)
   - `clima` (Climate)
   - `poblacion` (Population)
   - `terreno` (Terrain)
   - `diametro` (Diameter)

3. **personajes** - Star Wars characters
   - `id` (Primary Key)
   - `nombre` (Character name)
   - `color_cabello` (Hair color)
   - `color_ojos` (Eye color)
   - `altura` (Height)
   - `peso` (Weight)
   - `genero` (Gender)

4. **favoritos_planetas** - User favorite planets (Junction table)
   - `id` (Primary Key)
   - `usuario_id` (Foreign Key → usuario.id)
   - `planeta_id` (Foreign Key → planetas.id)

5. **favoritos_personajes** - User favorite characters (Junction table)
   - `id` (Primary Key)
   - `usuario_id` (Foreign Key → usuario.id)
   - `personaje_id` (Foreign Key → personajes.id)

## Relationships

- **Usuario ↔ Favoritos_Planetas**: One-to-Many
- **Planetas ↔ Favoritos_Planetas**: One-to-Many  
- **Usuario ↔ Favoritos_Personajes**: One-to-Many
- **Personajes ↔ Favoritos_Personajes**: One-to-Many

This creates a proper many-to-many relationship between users and planets/characters through junction tables.

## Key Improvements Made

1. **Removed Redundancy**: Eliminated duplicate User models
2. **Fixed Relationships**: Corrected foreign key references and relationships
3. **Enhanced Data Model**: Added realistic StarWars attributes
4. **Improved Security**: Removed password from serialization
5. **Better Structure**: Added explicit table naming and proper constraints
6. **Fixed Typos**: Corrected field names and references

## Usage Instructions

### Setup Environment
```bash
# Create virtual environment
python3 -m venv starwars_env

# Activate virtual environment
source starwars_env/bin/activate

# Install dependencies
pip install flask flask-sqlalchemy sqlalchemy sqlalchemy-utils eralchemy graphviz
```

### Generate Database Diagram
```bash
# Run the diagram generation script
python diagram.py
```

This will create `diagram.png` showing the Entity-Relationship diagram of your database.

### Alternative with Pipfile
```bash
# Install pipenv if not available
pip install pipenv

# Install dependencies from Pipfile
pipenv install

# Generate diagram
pipenv run python diagram.py
```

## Technical Stack
- **Python 3.13**
- **SQLAlchemy 2.0+** - ORM and database toolkit
- **Flask-SQLAlchemy** - Flask integration for SQLAlchemy
- **ERAlchemy** - Database diagram generation
- **Graphviz** - Graph visualization
- **SQLite** - Database engine

## Project Structure
```
starwars-blog/
├── src/
│   └── models.py              # Database models
├── starwars_env/              # Virtual environment
├── diagram.py                 # Diagram generation script
├── diagram.png                # Generated ER diagram
├── tmp.db                     # SQLite database
├── Pipfile                    # Dependencies
├── CORRECTIONS_MADE.md        # Detailed fixes
└── PROJECT_SUMMARY.md         # This file
```

## Success Metrics
✅ **Database Models**: All 5 tables properly defined with correct relationships  
✅ **Foreign Keys**: Proper foreign key constraints implemented  
✅ **Serialization**: Safe serialization methods without password exposure  
✅ **Diagram Generation**: Working ER diagram generation  
✅ **Documentation**: Comprehensive documentation of changes and usage  

## Future Enhancements
- Add data validation
- Implement database migrations
- Add more StarWars entities (ships, species, etc.)
- Add authentication and authorization
- Create REST API endpoints
- Add data seeding scripts

## Conclusion
The StarWars blog database model has been successfully corrected and improved, providing a solid foundation for a StarWars-themed blog application with proper user management and favorite tracking functionality.
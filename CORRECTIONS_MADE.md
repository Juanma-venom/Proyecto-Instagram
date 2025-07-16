# StarWars Blog Database Model - Corrections and Improvements

## Issues Fixed in the Original Code

### 1. **Removed Redundant User Models**
- **Issue**: Both `User` and `Usuario` models were defined, serving the same purpose
- **Fix**: Removed the `User` model and kept only `Usuario` with enhanced fields

### 2. **Fixed Typo in Usuario Model**
- **Issue**: `userrname` instead of `username`
- **Fix**: Corrected to `username`

### 3. **Improved Usuario Model**
- **Added**: `email` field for better user identification
- **Added**: `is_active` field for account management
- **Added**: `__tablename__` for explicit table naming

### 4. **Enhanced Planetas Model**
- **Issue**: Limited attributes and wrong data type for `poblacion`
- **Fix**: 
  - Changed `poblacion` from `Boolean` to `String` (population should be a number/string, not boolean)
  - Added more realistic StarWars planet attributes: `terreno`, `diametro`
  - Renamed `planetas` field to `nombre` for clarity
  - Added proper `__tablename__`

### 5. **Enhanced Personajes Model**
- **Issue**: Limited attributes and combined fields
- **Fix**: 
  - Split `color_de_cabello_y_ojos` into separate `color_cabello` and `color_ojos` fields
  - Added more character attributes: `altura`, `peso`, `genero`
  - Renamed `personajes` field to `nombre` for clarity
  - Added proper `__tablename__`

### 6. **Fixed Foreign Key Relationships**
- **Issue**: Incorrect foreign key references (`favoritos__planetas` instead of `favoritos_planetas`)
- **Fix**: Corrected all foreign key references to match actual table names

### 7. **Improved Junction Tables**
- **Issue**: 
  - Used `String` type for foreign keys instead of `Integer`
  - Incorrect field names (`id_usuario`, `id_planetas` instead of proper foreign keys)
- **Fix**: 
  - Changed to proper foreign key columns: `usuario_id`, `planeta_id`, `personaje_id`
  - Used proper `Integer` type with `ForeignKey` constraint
  - Added explicit `__tablename__` declarations

### 8. **Fixed Relationship Configurations**
- **Issue**: Incorrect relationship setups and back_populates references
- **Fix**: 
  - Corrected all `relationship()` declarations
  - Fixed `back_populates` references to match actual attribute names
  - Removed incorrect `cascade="all, delete-orphan"` from many-to-one relationships

### 9. **Enhanced Serialize Methods**
- **Issue**: 
  - Some serialize methods referenced non-existent attributes
  - Missing comprehensive serialization
- **Fix**: 
  - Fixed all serialize methods to reference correct attributes
  - Added nested serialization in junction tables to include related objects
  - Removed password serialization for security

### 10. **Added Proper Table Naming**
- **Issue**: Implicit table naming could cause conflicts
- **Fix**: Added explicit `__tablename__` declarations for all models

## Database Relationships

The corrected model implements the following relationships:

1. **Usuario ↔ Favoritos_Planetas**: One-to-Many
   - A user can have many favorite planets
   - Each favorite planet record belongs to one user

2. **Planetas ↔ Favoritos_Planetas**: One-to-Many
   - A planet can be favorited by many users
   - Each favorite planet record references one planet

3. **Usuario ↔ Favoritos_Personajes**: One-to-Many
   - A user can have many favorite characters
   - Each favorite character record belongs to one user

4. **Personajes ↔ Favoritos_Personajes**: One-to-Many
   - A character can be favorited by many users
   - Each favorite character record references one character

## Key Improvements

1. **Better Data Modeling**: More realistic attributes for StarWars entities
2. **Proper Foreign Key Constraints**: Ensures referential integrity
3. **Enhanced Serialization**: Better API response formatting
4. **Security**: Removed password from serialization
5. **Consistency**: Uniform naming conventions and structure
6. **Scalability**: Proper relationship setup for future enhancements

## Usage

To generate the database diagram:
```bash
pipenv install
pipenv run diagram
```

Or use the standalone script:
```bash
python diagram.py
```

This will create a `diagram.png` file showing the Entity-Relationship diagram of your StarWars blog database.
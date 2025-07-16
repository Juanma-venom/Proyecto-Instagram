# Fix Migration Error: ImportError with 'Ibteger'

## Problem
You're getting this error when running `pipenv run migrate`:
```
ImportError: cannot import name 'Ibteger' from 'sqlalchemy' (...). Did you mean: 'Integer'?
```

## Root Cause
1. There's a typo in your `src/models.py` file: `Ibteger` instead of `Integer`
2. The `admin.py` is trying to import `User` from models, but the corrected version only has `Usuario`

## Solution

### Step 1: Replace your models.py file
Copy the corrected `src/models.py` file from this workspace to your project directory:

```bash
# From your project directory: /workspaces/Juanma-Venom-Star-Wars_data/
cp /workspace/src/models.py src/models.py
```

### Step 2: Verify the fix
Check that the import statement in `src/models.py` is correct:
```python
from sqlalchemy import String, Boolean, ForeignKey, Integer  # <- Integer, not Ibteger
```

### Step 3: Check for User alias
The corrected file includes this line at the end for backward compatibility:
```python
# Alias for backward compatibility with existing admin.py
User = Usuario
```

### Step 4: Run migration again
```bash
pipenv run migrate
```

## If you still get errors:

### Check for duplicate models.py files
```bash
find . -name "models.py" -type f
```

### Alternative: Manual fix
If you prefer to fix it manually, edit your `src/models.py` file and:

1. **Fix the typo in line 2:**
   ```python
   # Change this:
   from sqlalchemy import String, Boolean, ForeignKey, Ibteger
   
   # To this:
   from sqlalchemy import String, Boolean, ForeignKey, Integer
   ```

2. **Add User alias at the end of the file:**
   ```python
   # Add this line at the very end:
   User = Usuario
   ```

## What the corrected models.py includes:
- ✅ Fixed import statement with correct `Integer` spelling
- ✅ `User` model alias for backward compatibility
- ✅ Proper relationship configurations
- ✅ Enhanced StarWars attributes for planets and characters
- ✅ Secure serialization methods (password excluded)
- ✅ Proper foreign key constraints

## Expected tables after migration:
- `usuario` - User management
- `planetas` - Star Wars planets  
- `personajes` - Star Wars characters
- `favoritos_planetas` - User favorite planets
- `favoritos_personajes` - User favorite characters

Once you complete these steps, the migration should work properly!
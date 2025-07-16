# Fix Database Migration Constraint Error

## Problem
The migration is failing because it can't drop the old table `favoritos__personajes` due to foreign key constraints:

```
cannot drop table favoritos__personajes because other objects depend on it
DETAIL: constraint personajes_favorito_id_fkey on table personajes depends on table favoritos__personajes
```

## Root Cause
- **Old database**: Had tables with double underscores (`favoritos__personajes`, `favoritos__planetas`)
- **New models**: Use single underscores (`favoritos_personajes`, `favoritos_planetas`)
- **Migration conflict**: Can't drop old tables because of foreign key constraints

## Solution Options

### Option 1: Reset Database (Recommended for Development)

This is the cleanest solution if you're in development and can afford to lose data:

```bash
# 1. Connect to your database and drop all tables
# For PostgreSQL:
psql -h your-host -U your-user -d your-database

# In psql, run:
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO your-user;
GRANT ALL ON SCHEMA public TO public;

# 2. Remove all migration files except __init__.py
rm migrations/versions/*.py

# 3. Create initial migration
pipenv run migrate -m "Initial migration with corrected models"

# 4. Run the migration
pipenv run upgrade
```

### Option 2: Fix the Migration File

If you need to preserve data, edit the migration file to handle constraints properly:

```bash
# 1. Find the failing migration file
ls migrations/versions/

# 2. Edit the migration file (likely 25adb0b9c724_.py)
# Add this before dropping tables:
```

```python
def upgrade():
    # Drop foreign key constraints first
    op.drop_constraint('personajes_favorito_id_fkey', 'personajes', type_='foreignkey')
    op.drop_constraint('planetas_favorito_id_fkey', 'planetas', type_='foreignkey')
    
    # Now drop the old tables
    op.drop_table('favoritos__personajes')
    op.drop_table('favoritos__planetas')
    
    # Create new tables with correct names
    # ... rest of your migration code
```

### Option 3: Manual Database Fix

If you want to fix it manually in the database:

```sql
-- Connect to your PostgreSQL database
-- Drop foreign key constraints first
ALTER TABLE personajes DROP CONSTRAINT IF EXISTS personajes_favorito_id_fkey;
ALTER TABLE planetas DROP CONSTRAINT IF EXISTS planetas_favorito_id_fkey;

-- Drop the old tables
DROP TABLE IF EXISTS favoritos__personajes CASCADE;
DROP TABLE IF EXISTS favoritos__planetas CASCADE;

-- Now run the migration
```

Then run: `pipenv run upgrade`

### Option 4: Create a New Migration

Create a manual migration to fix the constraint issue:

```bash
# Create new migration
pipenv run migrate -m "Fix foreign key constraints"
```

Edit the new migration file to:
1. Drop foreign key constraints
2. Drop old tables
3. Let the next migration create the new structure

## Recommended Steps (Development Environment)

1. **Backup your data** (if you need to preserve it)
2. **Use Option 1** (Reset Database) - it's the cleanest
3. **Run the commands**:

```bash
# Reset database (adjust connection details)
psql -h localhost -U your-user -d your-database -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public; GRANT ALL ON SCHEMA public TO your-user; GRANT ALL ON SCHEMA public TO public;"

# Remove old migrations
rm migrations/versions/*.py

# Create fresh migration
pipenv run migrate -m "Initial migration with corrected StarWars models"

# Apply migration
pipenv run upgrade
```

## What the Fixed Database Will Have

After successful migration, you'll have:
- ✅ `usuario` table (instead of conflicting User models)
- ✅ `planetas` table with enhanced StarWars attributes
- ✅ `personajes` table with detailed character info
- ✅ `favoritos_planetas` table (single underscore)
- ✅ `favoritos_personajes` table (single underscore)
- ✅ Proper foreign key relationships
- ✅ No constraint conflicts

## Prevention

To avoid this in the future:
1. Always test migrations in development first
2. Use explicit table names in models (`__tablename__`)
3. Be careful with relationship naming conventions
4. Review migration files before applying

Choose Option 1 if you're in development, or Option 2/3 if you need to preserve existing data.
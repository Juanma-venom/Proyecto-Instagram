-- Manual Database Fix for StarWars Migration Constraints
-- Run this script in your PostgreSQL database to fix the constraint issues

-- WARNING: This will drop existing tables and data!
-- Make sure to backup your data first if you need to preserve it

BEGIN;

-- Step 1: Drop foreign key constraints that are blocking table drops
ALTER TABLE personajes DROP CONSTRAINT IF EXISTS personajes_favorito_id_fkey;
ALTER TABLE planetas DROP CONSTRAINT IF EXISTS planetas_favorito_id_fkey;

-- Step 2: Drop the old tables with double underscores
DROP TABLE IF EXISTS favoritos__personajes CASCADE;
DROP TABLE IF EXISTS favoritos__planetas CASCADE;

-- Step 3: Drop other old tables if they exist
DROP TABLE IF EXISTS personajes CASCADE;
DROP TABLE IF EXISTS planetas CASCADE;
DROP TABLE IF EXISTS usuario CASCADE;
DROP TABLE IF EXISTS "user" CASCADE;

-- Step 4: Clear the alembic version table to reset migrations
DELETE FROM alembic_version;

COMMIT;

-- After running this script:
-- 1. Remove all migration files: rm migrations/versions/*.py
-- 2. Create new migration: pipenv run migrate -m "Initial migration with corrected models"
-- 3. Apply migration: pipenv run upgrade

-- Expected final structure:
-- ✅ usuario - User management
-- ✅ planetas - Star Wars planets with enhanced attributes
-- ✅ personajes - Star Wars characters with detailed info
-- ✅ favoritos_planetas - User favorite planets (single underscore)
-- ✅ favoritos_personajes - User favorite characters (single underscore)
#!/usr/bin/env python3
"""
Quick Fix Script for StarWars Database Migration Constraints
This script will help resolve the foreign key constraint issues
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔧 {description}")
    print(f"Running: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Success: {description}")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ Error: {description}")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False
    
    return True

def main():
    print("🚀 StarWars Database Migration Constraint Fix")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("src/models.py"):
        print("❌ Error: src/models.py not found. Please run this from your project root.")
        sys.exit(1)
    
    print("\n📋 This script will:")
    print("1. Remove problematic migration files")
    print("2. Create a fresh migration")
    print("3. Apply the migration")
    
    response = input("\n❓ Are you sure you want to continue? (y/N): ").strip().lower()
    if response != 'y':
        print("Aborted.")
        sys.exit(0)
    
    print("\n🗂️  Checking current migration files...")
    if os.path.exists("migrations/versions/"):
        migration_files = [f for f in os.listdir("migrations/versions/") if f.endswith('.py') and f != '__init__.py']
        print(f"Found {len(migration_files)} migration files")
        
        if migration_files:
            print("\n🗑️  Removing old migration files...")
            for file in migration_files:
                file_path = os.path.join("migrations/versions/", file)
                try:
                    os.remove(file_path)
                    print(f"  - Removed: {file}")
                except Exception as e:
                    print(f"  - Error removing {file}: {e}")
    
    # Create new migration
    success = run_command(
        "pipenv run migrate -m 'Initial migration with corrected StarWars models'",
        "Creating new migration"
    )
    
    if not success:
        print("\n❌ Failed to create migration. Please check your models.py file.")
        sys.exit(1)
    
    # Apply migration
    success = run_command(
        "pipenv run upgrade",
        "Applying migration"
    )
    
    if success:
        print("\n🎉 Migration completed successfully!")
        print("\n📊 Your database now has:")
        print("  - usuario (user management)")
        print("  - planetas (Star Wars planets)")
        print("  - personajes (Star Wars characters)")
        print("  - favoritos_planetas (user favorite planets)")
        print("  - favoritos_personajes (user favorite characters)")
    else:
        print("\n❌ Migration failed. Please check the error above.")
        print("\n🔍 Common issues:")
        print("  - Database connection problems")
        print("  - Permission issues")
        print("  - Syntax errors in models.py")
        print("\n📖 Check FIX_MIGRATION_CONSTRAINT_ERROR.md for manual solutions.")

if __name__ == "__main__":
    main()
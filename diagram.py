import os
import sys

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from eralchemy import render_er
from models import db
from sqlalchemy import create_engine

# Create database URL
db_url = 'sqlite:///tmp.db'

# Create database engine
engine = create_engine(db_url)

# Create all tables
db.metadata.create_all(engine)

# Generate the diagram using database URL string
render_er(db_url, 'diagram.png')
print("Database diagram generated successfully as 'diagram.png'")
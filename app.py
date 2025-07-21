import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
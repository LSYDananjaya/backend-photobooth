import os
import sys

# Add the project root to the Python path - works for both local and containerized environments
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to import the main module using different import strategies
try:
    # Try direct import first
    from src.main import app, socketio
except ImportError:
    # If that fails, try modifying the path and importing again
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
    from main import app, socketio

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=False)

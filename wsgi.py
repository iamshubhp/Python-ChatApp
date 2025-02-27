# Import the Flask app and socketio instance from the app module
from app import app, socketio

# Main entry point for the application
if __name__ == "__main__":
    # Run the Flask app with SocketIO support
    # This starts the web server and enables WebSocket communication
    socketio.run(app)

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random

# Initialize Flask app and configure SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Dictionary to store connected users. Key: socket ID, Value: Dictionary with username and avatar URL
users = {}

# Route to render the main chat page


@app.route('/')
def index():
    return render_template('index.html')

# Event listener for new connections


@socketio.on("connect")
def handle_connect():
    # Generate a random username
    username = f"User_{random.randint(1000, 9999)}"

    # Randomly assign a gender for avatar selection
    gender = random.choice(["girl", "boy"])

    # Generate an avatar URL based on the username and gender
    avatar_url = f"https://avatar.iran.liara.run/public/{gender}?username={username}"

    # Store the user's details in the users dictionary
    users[request.sid] = {"username": username, "avatar": avatar_url}

    # Notify all clients that a new user has joined
    emit("user_joined", {"username": username,
         "avatar": avatar_url}, broadcast=True)

    # Send the generated username back to the newly connected user
    emit("set_username", {"username": username})

# Event listener for user disconnection


@socketio.on("disconnect")
def handle_disconnect():
    # Retrieve user details and remove them from the users dictionary
    user = users.pop(request.sid, None)
    if user:
        # Notify all clients that a user has left
        emit("user_left", {"username": user["username"]}, broadcast=True)

# Event listener for incoming chat messages


@socketio.on("send_message")
def handle_message(data):
    # Retrieve user details
    user = users.get(request.sid)
    if user:
        # Broadcast the message to all clients, including sender details
        emit("new_message", {
            "username": user["username"],
            "avatar": user["avatar"],
            "message": data["message"]
        }, broadcast=True)

# Event listener for username updates


@socketio.on("update_username")
def handle_update_username(data):
    # Get old and new usernames
    old_username = users[request.sid]["username"]
    new_username = data["username"]

    # Update username in users dictionary
    users[request.sid]["username"] = new_username

    # Notify all clients about the username change
    emit("username_updated", {
        "old_username": old_username,
        "new_username": new_username
    }, broadcast=True)


# Run the Flask app with SocketIO support
if __name__ == "__main__":
    socketio.run(app)

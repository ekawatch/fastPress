from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/client")
def client():
    return render_template("client.html")

@app.route("/display")
def display():
    return render_template("display.html")

@socketio.on("press")
def handle_press(data):
    print("Received ID:", data["id"])
    emit("new_press", data, broadcast=True)

@socketio.on("reset")
def handle_reset():
    emit("reset_all", broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

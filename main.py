from flask import Flask, render_template, send_file
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
socket = SocketIO(app)

@app.route("/")
def handle():
    return render_template(
        'index.html',
        title = "page 2",
        userName = "maxence",
        table = ["max","toto","henry"],
    )

@app.route("/templates/<path:path>")
def handleGetFile(path : str):
    return send_file(f"templates/{path}")

@socket.on("connect")
def handleConnect():
    print("in socket connect")
    emit(
        "data",
        {
            "data": "salut"
        }
    )   

@socket.on("data")
def handleData(mess=None):
    print("in socket data")
    emit(
        "data",
        {
            "data": "salut"
        }
    )
socket.run(
    app,
    host='localhost',
    port=5000,
    debug=True
)
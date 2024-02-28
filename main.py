from flask import Flask, render_template, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

app.run(
    host='localhost',
    port=5000,
    debug=True
)
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def handle():
    table = [
            "max",
            "toto",
            "henry"
        ]
    headerFile = open("./templates/header.html", "r")
    return render_template(
        'index.html',
        userName = "maxence",
        table = table,
        header=headerFile.read()
    )

app.run(
    host='localhost',
    port=5000,
    debug=True
)
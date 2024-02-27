from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def handle():
    return render_template('index.html')

app.run(
    host='localhost',
    port=5000,
    debug=True
)
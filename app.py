from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

Students = [{"id": 1, "name": "elad"}, {"id": 2, "name": "ofer"}]

@app.route("/")
def index():
    return jsonify(Students)

if __name__ == "__main__":
    app.run()

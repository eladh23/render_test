from flask import Flask

app = Flask(__name__)

students = [{"id": 1, "name": "Dan"}, {"id": 2, "name": "Yochai"}]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()

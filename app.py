from flask import Flask, render_template

app = Flask(__name__)

students = [{"id": 1, "name": "Dan"}, {"id": 2, "name": "Yochai"}]

@app.route("/")
def index():
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run()

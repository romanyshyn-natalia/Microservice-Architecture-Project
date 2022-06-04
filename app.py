from flask import Flask

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    # TODO:
    return ""


@app.route("/login")
def login():
    return ""


@app.route("/home")
def home():
    # Search patients: GET (name, surname) (id) -> data
    # Search doctors: GET (name, surname) (id) -> data
    return ""


@app.route("/patients")
def patients():
    return ""


@app.route("/doctors")
def doctors():
    return ""


if __name__ == "__main__":
    app.run()

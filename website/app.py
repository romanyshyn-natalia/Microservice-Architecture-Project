from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')



@app.route("/register", methods=["GET","POST"])
def register():
    # TODO:
    return render_template('register.html')


@app.route("/login")
def login():
    return render_template('login.html')


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
    app.run(debug=True)

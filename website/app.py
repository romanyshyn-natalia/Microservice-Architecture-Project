from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')



@app.route("/register", methods=["GET","POST"])
def register_page():
    # TODO:
    return render_template('register.html')


@app.route("/login")
def login_page():
    return render_template('login.html')


@app.route("/")
def home_page():
    # Search patients: GET (name, surname) (id) -> data
    # Search doctors: GET (name, surname) (id) -> data
    return ""


@app.route("/patients")
def patients_page():
    return ""


@app.route("/doctors")
def doctors_page():
    return ""


if __name__ == "__main__":
    app.run(debug=True)

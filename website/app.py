from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/register", methods=["GET", "POST"])
def register():
    # if success:
    #     return redirect(url_for('login'))
    # else:
    #     return render_template('register_unsuccessful.html')

    return render_template('register.html')


@app.route("/login")
def login():
    # if success:
    #     return redirect(url_for('home'))
    # else:
    #     return render_template('login_unsuccessful.html')

    return render_template('login.html')


@app.route("/home")
def home():
    # Search patients: GET (name, surname) (id) -> data
    # Search doctors: GET (name, surname) (id) -> data
    return render_template('home.html')


@app.route("/results")
def results():
    return render_template('results.html', results=[
        {"name": "John", "surname": "Smith", "id": "12345", "status": "Rehabilitation", "diagnosis": "Unknown",
         "date": "12.04.2010", "age": "20", "sex": "Male", "doctor": "Tom Brown (5123)"}])


if __name__ == "__main__":
    app.run(debug=True)

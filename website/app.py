import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')
patients_service_url = "localhost:9042"
login_service_url = "localhost:8080"


@app.route("/register", methods=["GET", "POST"])
def register():
    # if success:
    #     return redirect(url_for('login'))
    # else:
    #     return render_template('register_unsuccessful.html')

    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    # if success:
    #     return redirect(url_for('home'))
    # else:
    #     return render_template('login_unsuccessful.html')

    return render_template('login.html')


@app.route("/home", methods=["GET", "POST"])
def home():
    # Search patients: GET (name, surname) (id) -> data
    # Search doctors: GET (name, surname) (id) -> data
    return render_template('home.html')


@app.route("/results", methods=["GET", "POST"])
def results(search_result=None):
    if request.method == 'POST':
        form_name = request.form.get("name")
        form_surname = request.form.get("surname")
        form_id = request.form.get("id")

        # TODO:
        if not (form_name or form_surname):
            post_response = requests.post(patients_service_url, headers={'content-type': 'application/json'},
                                          data={"id": form_id})
        else:
            post_response = requests.post(patients_service_url, headers={'content-type': 'application/json'},
                                          data={"name": form_name, "surname": form_surname})
        print(post_response.text)

        search_result = [
            {"name": "John", "surname": "Smith", "id": "12345", "status": "Rehabilitation", "diagnosis": "Unknown",
             "date": "12.04.2010", "age": "20", "sex": "Male", "doctor": "Tom Brown (5123)"},
            {"name": "John 2", "surname": "Smith 2", "id": "876545", "status": "Rehabilitation", "diagnosis": "Unknown",
             "date": "12.04.2010", "age": "20", "sex": "Male", "doctor": "Tom Brown (5123)"}
        ]

    if not search_result:
        search_result = [
            {"name": "-", "surname": "-", "id": "-", "status": "-", "diagnosis": "-",
             "date": "-", "age": "-", "sex": "-", "doctor": "-"}
        ]

    return render_template('results.html', results=search_result)


if __name__ == "__main__":
    app.run(debug=True)

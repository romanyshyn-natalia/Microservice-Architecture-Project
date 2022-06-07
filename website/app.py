import requests
from flask import Flask, render_template, request, redirect, url_for
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

app = Flask(__name__, template_folder='templates', static_folder='static')
patients_service_url = "http://localhost:9042"
login_service_url = "http://localhost:8080/login"
register_service_url = "http://localhost:8081/register"

# session = requests.Session()
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
# session.mount('http://', adapter)
# session.mount('https://', adapter)


@app.route("/", methods=["GET"])
def base():
    return redirect(url_for('home'))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        x = requests.post(register_service_url, json={
            "email": request.form.get("email"),
            "username": request.form.get("username"),
            "role": request.form.get("role"),
            "password1": request.form.get("password1"),
            "password2": request.form.get("password2")
        })

        if x.text != "success":
            return render_template('register.html', error=x.text)
        else:
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        x = requests.post(login_service_url, json={
            "username": request.form.get("username"),
            "password": request.form.get("password"),
        })

        if x.text != "success":
            return render_template('login.html', error=x.text)
        else:
            return redirect(url_for('home'))

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

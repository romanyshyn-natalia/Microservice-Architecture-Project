import pymongo
from flask import Flask, request
import hashlib

app = Flask(__name__)

client = pymongo.MongoClient(host="db", port=27017)
db = client.users
records = db['registered-users']


@app.route("/register", methods=['POST'])
def register():
    if request.method == "POST":
        response = request.json
        email = response['email']
        username = response['username']
        role = response['role']
        passwrd1 = response['password1']
        passwrd2 = response['password2']

        # checks
        user_found = records.find_one({'username': username})
        email_found = records.find_one({'email': email})

        if user_found:
            return "This username has already taken."
        elif email_found:
            return "This email is already used."
        elif passwrd1 != passwrd2:
            return "Passwords should match!"
        else:
            hashed = hashlib.sha256(passwrd1.encode('utf-8')).hexdigest()
            one_record = {'username': username, 'email': email, 'role': role, 'password': hashed}
            records.insert_one(one_record)
    return "success"


if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=8081)

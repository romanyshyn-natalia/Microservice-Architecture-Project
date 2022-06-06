import pymongo
import hashlib
from flask import Flask, request

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.users
records = db['registered-users']


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        response = request.json
        user = response['username']
        passwrd = response['password']

        user_check = records.find_one({"username": user})
        if user_check:
            pass_check = user_check['password']
            if hashlib.sha256(passwrd.encode('utf-8')).hexdigest() == pass_check:
                print("You are logged in!")
            else:
                print("Wrong password!")
        else:
            print("User not found!")

    return ""


if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=8080)

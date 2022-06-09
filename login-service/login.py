import pymongo
import hashlib
from flask import Flask, request

app = Flask(__name__)

client = pymongo.MongoClient(host="db", port=27017)
db = client.users
records = db['registered-users']


@app.route("/login", methods=['POST'])
def login():
    if request.method == "POST":
        response = request.json
        user = response['username']
        passwrd = response['password']

        user_check = records.find_one({"username": user})
        if user_check:
            pass_check = user_check['password']
            # if hashlib.sha256(passwrd.encode('utf-8')).hexdigest() == pass_check:
            if passwrd == pass_check:
                return "success"
            else:
                return "Wrong password!"
        else:
            return "User not found!"

    return "success"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)


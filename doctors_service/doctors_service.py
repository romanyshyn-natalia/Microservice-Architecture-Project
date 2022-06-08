from flask_restful import reqparse, Resource, Api
from flask import Flask
from postgres_client import get_engine, get_session, query_by_id, query_by_name
import json

app = Flask(__name__)
api = Api(app)
app.config['BUNDLE_ERRORS'] = True

parser = reqparse.RequestParser()
parser.add_argument('file_name', type=str,
                    help='File with data', required=False)
parser.add_argument('doctor_id', type=int, required=False)
parser.add_argument('doctor_name', type=str, required=False)
parser.add_argument('doctor_surname', type=str, required=False)


# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"doctor_id":"4"}' \
#   http://localhost:8881/


# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"doctor_id":"26"}' \
#   http://localhost:8881/


# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"doctor_name":"Brian", "doctor_surname":"Foster"}' \
#   http://localhost:8881/


def jsonify_result(result):
    res = {"doctors": []}
    for i in result:
        dct = {}
        dct['doctor_name'] = i[0]
        dct['doctor_surname'] = i[1]
        dct['doctor_id'] = i[2]
        dct['department'] = i[3]
        dct['experience'] = i[4]
        dct['room'] = i[5]
        dct['assigned_patients'] = i[6]

        res["doctors"].append(dct)

    return res


class RetrieveData(Resource):
    def get(self):
        args = parser.parse_args()
        print('args', args)
        if args['doctor_id'] is not None:
            result = query_by_id(session, args.doctor_id)
            return json.dumps(jsonify_result(result))
        elif args['doctor_name'] is not None and args['doctor_surname'] is not None:
            result = query_by_name(
                session, args.doctor_name, args.doctor_surname)
            print(result)
            return json.dumps(jsonify_result(result))
        else:
            return "Invalid request"


api.add_resource(RetrieveData, '/')

if __name__ == "__main__":
    engine = get_engine()
    session = get_session(engine)

    app.run(host='localhost', debug=True, port=8881)

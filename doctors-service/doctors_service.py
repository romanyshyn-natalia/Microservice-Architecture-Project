from flask_restful import reqparse, Resource, Api
from flask import Flask
import json
from cassandra_client import CassandraClient


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
#   http://localhost:8081/


# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"doctor_id":"26"}' \
#   http://localhost:8081/


# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"doctor_name":"Brian", "doctor_surname":"Foster"}' \
#   http://localhost:8081/


def jsonify_result_query_one(result):
    res = {"doctors": []}
    for i in result:
        dct = {}
        dct['doctor_name'] = i[3]
        dct['doctor_surname'] = i[4]
        dct['doctor_id'] = i[0]
        dct['department'] = i[2]
        dct['experience'] = i[5]
        dct['room'] = i[6]
        dct['assigned_patients'] = i[1]

        res["doctors"].append(dct)

    return res


def jsonify_result_query_two(result):
    res = {"doctors": []}
    for i in result:
        dct = {}
        dct['doctor_name'] = i[0]
        dct['doctor_surname'] = i[1]
        dct['doctor_id'] = i[4]
        dct['department'] = i[3]
        dct['experience'] = i[5]
        dct['room'] = i[6]
        dct['assigned_patients'] = i[2]

        res["doctors"].append(dct)

    return res


class RetrieveData(Resource):
    def get(self):
        args = parser.parse_args()
        print('args', args)
        if args['doctor_id'] is not None:
            result = client.query_by_id(args.doctor_id)
            return json.dumps(jsonify_result_query_one(result))
        elif args['doctor_name'] is not None and args['doctor_surname'] is not None:
            result = client.query_by_name(args.doctor_name, args.doctor_surname)
            return json.dumps(jsonify_result_query_two(result))
        else:
            return "Invalid request"


api.add_resource(RetrieveData, '/')

if __name__ == "__main__":
    host = 'cassandra'
    port = 9042
    keyspace = 'doctors'
    client = CassandraClient(host, port, keyspace)
    client.connect()
    client.prepare_db()

    app.run(host='0.0.0.0', debug=True, port=8084)

from flask_restful import reqparse, Resource, Api
from flask import Flask, jsonify
# # from postgres_client import get_engine, get_session, query_by_id, query_by_name
from cassandra_client import CassandraClient

import json

app = Flask(__name__)
api = Api(app)
app.config['BUNDLE_ERRORS'] = True

parser = reqparse.RequestParser()
parser.add_argument('file_name', type=str,
                    help='File with data', required=False)
parser.add_argument('patient_id', type=int, required=False)
parser.add_argument('patient_name', type=str, required=False)
parser.add_argument('patient_surname', type=str, required=False)


# curl --header "Content-Type: application/json"   --request GET   --data '{"patient_id":1}'   http://0.0.0.0:8080/


# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"patient_id":"26"}' \
#   http://localhost:8880/


# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"patient_name":"Emily", "patient_surname":"Ortiz"}' \
#   http://localhost:8880/


def jsonify_result_query1(result):
    res = {"patients": []}
    for i in result:
        # print(i)
        dct = {}
        dct['name'] = i[4]
        dct['surname'] = i[5]
        dct['patient_id'] = i[0]
        dct['status'] = i[8]
        dct['assigned_doctor_id'] = i[2]
        dct['age'] = i[1]
        dct['sex'] = i[7]
        dct['diagnosis'] = i[3]
        dct['registration_date'] = i[6]

        res["patients"].append(dct)

    return res

def jsonify_result_query2(result):
    res = {"patients": []}
    for i in result:
        # print(i)
        dct = {}
        dct['name'] = i[0]
        dct['surname'] = i[1]
        dct['patient_id'] = i[5]
        dct['status'] = i[8]
        dct['assigned_doctor_id'] = i[3]
        dct['age'] = i[2]
        dct['sex'] = i[7]
        dct['diagnosis'] = i[4]
        dct['registration_date'] = i[6]

        res["patients"].append(dct)

    return res


class RetrieveData(Resource):
    def get(self):
        client.connect()
        args = parser.parse_args()
        print('args', args)
        if args['patient_id'] is not None:
            result = client.query_by_id(args.patient_id)
            client.close()
            return json.dumps(jsonify_result_query1(result))
        elif args['patient_name'] is not None and args['patient_surname'] is not None:
            result = client.query_by_name(
                args.patient_name, args.patient_surname)
            client.close()
            return json.dumps(jsonify_result_query2(result))
        else:
            client.close()
            return "Invalid request"


api.add_resource(RetrieveData, '/')

if __name__ == "__main__":
    host = 'cassandra-node1'
    port = 9042
    keyspace = 'patients'
    client = CassandraClient(host, port, keyspace)
    client.connect()
    client.prepare_db()

    app.run(host='0.0.0.0', debug=True, port=8080)

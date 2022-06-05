from flask_restful import reqparse, Resource, Api
from flask import Flask
from cassandra_client import CassandraClient

app = Flask(__name__)
api = Api(app)
app.config['BUNDLE_ERRORS'] = True

parser = reqparse.RequestParser()
parser.add_argument('file_name', type=str, help='File with data')
parser.add_argument('patient_id', type=str)
parser.add_argument('patient_name', type=str)
parser.add_argument('patient_surname', type=str)


class RetrieveData(Resource):
    def get():
        args = parser.parse_args()
        table = 'patients'
        client.connect()
        if 'patient_id' in args:
            result = client.read_by_id(args, table)
            client.close()
            return result
        if 'patient_name' in args and 'patient_surname' in args:
            result = client.read_by_id(args, table)
            client.close()
            return result
        else:
            return "Invalid request"

    def post():
        args = parser.parse_args()
        table = 'patients'
        client.connect()
        file_name = args['file_name']
        client.insert_record(table, None)

        client.close()


if __name__ == "__main__":
    host = 'localhost'
    port = 9042
    keyspace = 'patients_info'

    client = CassandraClient(host, port, keyspace)

    app.run()

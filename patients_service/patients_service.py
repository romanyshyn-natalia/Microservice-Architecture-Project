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
parser.add_argument('patient_id', type=int, required=False)
parser.add_argument('patient_name', type=str, required=False)
parser.add_argument('patient_surname', type=str, required=False)


def jsonify_result(result):
    res = {"patients": []}
    for i in result:
        dct = {}
        dct['name'] = i[0]
        dct['surname'] = i[1]
        dct['pattient_id'] = i[2]
        dct['status'] = i[3]
        dct['assigned_doctor_id'] = i[4]
        dct['age'] = i[5]
        dct['sex'] = i[6]
        dct['diagnosis'] = i[7]
        dct['registration_date'] = i[8].strftime("%m/%d/%Y, %H:%M:%S")

        res["patients"].append(dct)

    return res


class RetrieveData(Resource):
    def get(self):
        args = parser.parse_args()
        print(args)
        if args['patient_id'] is not None:
            result = query_by_id(session, args.patient_id)
            return json.dumps(jsonify_result(result))
        elif args['patient_name'] is not None and args['patient_surname'] is not None:
            result = query_by_name(
                session, args.patient_name, args.patient_surname)
            return json.dumps(jsonify_result(result))
        else:
            return "Invalid request"

    # def post(self):
    #     args = parser.parse_args()
    #     table = 'patients'
    #     file_name = args['file_name']


api.add_resource(RetrieveData, '/')

if __name__ == "__main__":
    engine = get_engine()
    session = get_session(engine)
    # print(engine.url.database)
    # q_res = session.execute(f"""
    # SELECT * FROM patients WHERE patient_id = 1;
    # """)
    # for row in q_res:
    #     print(row)

    app.run(host='localhost', debug=True, port=8880)

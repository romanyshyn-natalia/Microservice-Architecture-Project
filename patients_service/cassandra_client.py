from cassandra.cluster import Cluster


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    def execute(self, query):
        self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def insert_record(self, table, data):
        patient_name = data['patient_name']
        patient_surname = data['patient_surname']
        patient_id = data['patient_id']
        status = data['status']
        assigned_doctor_id = data['assigned_doctor_id']
        age = data['age']
        sex = data['sex']
        diagnosis = data['diagnosis']
        registration_date = data['registration_date']
        query = f"INSERT INTO {table} (patient_name, patient_surname, patient_id, status, " + \
            f"assigned_doctor_id, age, sex, diagnosis, registration_date) VALUES ('{patient_name}', '{patient_surname}', " + \
            f"{patient_id}, '{status}', {assigned_doctor_id}, {age}, '{sex}', '{diagnosis}', '{registration_date}')"
        self.session.execute(query)

    def query_by_id(self, patient_id):
        query = f"SELECT * FROM patients_by_id WHERE patient_id={patient_id}"
        rows = self.session.execute(query)
        return rows

    def query_by_name(self, patient_name, patient_surname):
        query = f"SELECT * FROM patients_by_names WHERE patient_name='{patient_name}' AND patient_surname='{patient_surname}'"
        rows = self.session.execute(query)
        return rows

    def prepare_db(self):
        import json
        patients_file = "./patients.json"
        with open(patients_file) as f:
            data = json.load(f)
            for i in data:
                self.insert_record("patients_by_id", i)
                self.insert_record("patients_by_names", i)

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
        doctor_name = data['doctor_name']
        doctor_surname = data['doctor_surname']
        doctor_id = data['doctor_id']
        department = data['department']
        assigned_patients = data['assigned_patients']
        room = data['room']
        experience = data['experience']

        query = f"INSERT INTO {table} (doctor_name, doctor_surname, doctor_id, department, " + \
            f"assigned_patients, room, experience) VALUES ('{doctor_name}', '{doctor_surname}', " + \
            f"{doctor_id}, '{department}', {assigned_patients}, {room}, '{experience}')"
        self.session.execute(query)

    def query_by_id(self, doctor_id):
        query = f"SELECT * FROM doctors_by_id WHERE doctor_id={doctor_id}"
        rows = self.session.execute(query)
        return rows

    def query_by_name(self, doctor_name, doctor_surname):
        query = f"SELECT * FROM doctors_by_names WHERE doctor_name='{doctor_name}' AND doctor_surname='{doctor_surname}'"
        rows = self.session.execute(query)
        return rows

    def prepare_db(self):
        import json
        patients_file = "./doctors.json"
        with open(patients_file) as f:
            data = json.load(f)
            for i in data:
                self.insert_record("doctors_by_id", i)
                self.insert_record("doctors_by_names", i)

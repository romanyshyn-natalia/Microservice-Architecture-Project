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
        patient_name, patient_surname, patient_id, status, assigned_doctors, age, diagnosis, registration_date = data
        query = f"INSERT INTO {table} (patient_name, patient_surname, patient_id, status," + \
            f"assigned_doctors, age, diagnosis, registration_date) VALUES('{patient_name}', '{patient_surname}'," + \
            f"'{patient_id}', '{status}', '{assigned_doctors}', '{age}', '{diagnosis}', '{registration_date}')"
        self.execute(query)

    def read_by_id(self, table_name, patient_id):
        query = f"SELECT * FROM {table_name} WHERE patient_id == '{patient_id}'"
        rows = self.session.execute(query)
        return rows
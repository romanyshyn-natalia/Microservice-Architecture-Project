import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    url = "postgresql://postgres:postgres@localhost:5432/"
    engine = create_engine(url, pool_size=50, echo=True)
    return engine


def get_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def query_by_id(session, patient_id):
    response = session.execute(f"""
    SELECT * FROM patients WHERE patient_id = {patient_id};
    """)
    return response


def query_by_name(session, patient_name, patient_surname):
    response = session.execute(f"""
    SELECT * FROM patients WHERE patient_name='{patient_name}' AND patient_surname='{patient_surname}';
    """)
    print(response)
    return response


def insert_data(session, patient_name, patient_surname, patient_id, status, assigned_doctor_id, age, sex, diagnosis,
                registration_date):
    response = session.execute(f"""
    INSERT INTO patients VALUES ('{patient_name}', '{patient_surname}', {patient_id}, '{status}', {assigned_doctor_id}, {age}, '{sex}', '{diagnosis}', '{registration_date}');
    """)
    return response


def prepare_db(session):
    session.execute(f"""
    CREATE TABLE patients (patient_name TEXT, patient_surname TEXT, patient_id INT, status TEXT, assigned_doctor_id INT, age INT, sex TEXT, diagnosis TEXT, registration_date TIMESTAMP, PRIMARY KEY(patient_id));
    """)
    patients_file = "./patients.json"
    with open(patients_file) as f:
        data = json.load(f)
        for i in data:
            insert_data(session, i['patient_name'], i['patient_surname'], i['patient_id'], i['status'],
                        i['assigned_doctor_id'], i['age'], i['sex'], i['diagnosis'], i['registration_date'])

    session.commit()


if __name__ == '__main__':
    engine = get_engine()
    print(engine.url.database)
    session = get_session(engine)
    prepare_db(session)

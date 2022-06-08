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


def query_by_id(session, doctor_id):
    response = session.execute(f"""
    SELECT * FROM doctors WHERE doctor_id = {doctor_id};
    """)
    return response


def query_by_name(session, doctor_name, doctor_surname):
    response = session.execute(f"""
    SELECT * FROM doctors WHERE doctor_name='{doctor_name}' AND doctor_surname='{doctor_surname}';
    """)
    print(response)
    return response


def insert_data(session, doctor_name, doctor_surname, doctor_id, department, experience, room, assigned_patients):
    response = session.execute(f"""
    INSERT INTO doctors VALUES ('{doctor_name}', '{doctor_surname}', {doctor_id}, '{department}', {experience}, {room}, ARRAY {assigned_patients});
    """)
    return response


def prepare_db(session):
    session.execute(f"""
    CREATE TABLE doctors (doctor_name TEXT, doctor_surname TEXT, doctor_id INT, department TEXT, experience TEXT, room INT, assigned_patients integer[10], PRIMARY KEY(doctor_id));
    """)
    patients_file = "./doctors.json"
    with open(patients_file) as f:
        data = json.load(f)
        for i in data:
            insert_data(session, i['doctor_name'], i['doctor_surname'], i['doctor_id'], i['department'],
                        i['experience'], i['room'], i['assigned_patients'])

    session.commit()


if __name__ == '__main__':
    engine = get_engine()
    print(engine.url.database)
    session = get_session(engine)
    prepare_db(session)

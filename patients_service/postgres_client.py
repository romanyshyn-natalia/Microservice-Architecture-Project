from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    url = "postgresql://postgres:postgres@localhost:5432/"
    engine = create_engine(url, pool_size=50, echo=False)

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
    SELECT * FROM patients WHERE patient_name = {patient_name} AND patient_surname = {patient_surname};
    """)
    return response


def insert_data(session, data):
    response = session.execute(f"""
    INSERT INTO patients VALUES ();
    """)
    return response


if __name__ == '__main__':
    engine = get_engine()
    print(engine.url.database)
    session = get_session(engine)
    q_res = session.execute(f"""
    SELECT * FROM patients WHERE patient_id = 1;
    """)
    for row in q_res:
        print(row)

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


if __name__ == '__main__':
    engine = get_engine()
    print(engine.url.database)
    session = get_session(engine)
    q_res = session.execute(f"""
    SELECT * FROM patients WHERE patient_id = 1;
    """)
    for row in q_res:
        print(row)

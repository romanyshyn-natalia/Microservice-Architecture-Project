FROM python:3.8-slim

ADD . /app

WORKDIR /app

RUN pip install flask

RUN pip install flask-restful

RUN pip install cassandra-driver

#RUN pip install sqlalchemy

#RUN pip install psycopg2-binary

COPY doctors_service.py .

COPY cassandra_client.py .

COPY data/doctors.json .

COPY data/patients.json .

#ENTRYPOINT ["python3", "doctors_service.py"]

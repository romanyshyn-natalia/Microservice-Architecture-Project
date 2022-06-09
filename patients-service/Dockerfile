FROM python:3.8-slim

ADD . /app

WORKDIR /app

RUN pip install flask

RUN pip install flask-restful

RUN pip install cassandra-driver

COPY patients_service.py .

COPY cassandra_client.py .

COPY ./data/doctors.json .

COPY ./data/patients.json .

#ENTRYPOINT ["sleep", "30"]

#ENTRYPOINT ["python3", "patients_service.py"]

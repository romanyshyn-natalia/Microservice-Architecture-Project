DESCRIBE keyspaces;

CREATE  KEYSPACE patients WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 2 };

USE patients;

Create TYPE doctors(
   name text,
   surname text,
   doctor_id int
);

CREATE TABLE patients (patient_name text, patient_surname text, patient_id int, status text, assigned_doctors doctors, age int, diagnosis text, registration_date text, PRIMARY KEY (patient_id));

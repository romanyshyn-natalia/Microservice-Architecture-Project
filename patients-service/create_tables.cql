DESCRIBE keyspaces;

CREATE  KEYSPACE patients WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 2 };

USE patients;

CREATE TABLE patients_by_id (patient_name text, patient_surname text, patient_id int, status text, assigned_doctor_id int, age int, sex text, diagnosis text, registration_date text, PRIMARY KEY (patient_id));

CREATE TABLE patients_by_names (patient_name text, patient_surname text, patient_id int, status text, assigned_doctor_id int, age int, sex text, diagnosis text, registration_date text, PRIMARY KEY (patient_name, patient_surname));

CREATE TABLE patients (patient_name text, patient_surname text, PRIMARY KEY (patient_name, patient_surname));

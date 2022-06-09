DESCRIBE keyspaces;

CREATE  KEYSPACE doctors WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 2 };

USE doctors;

CREATE TABLE doctors_by_id (doctor_name text, doctor_surname text, doctor_id int, department text, assigned_patients list<int>, room int, experience text, PRIMARY KEY (doctor_id));

CREATE TABLE doctors_by_names (doctor_name text, doctor_surname text, doctor_id int, department text, assigned_patients list<int>, room int, experience text, PRIMARY KEY (doctor_name, doctor_surname));

CREATE TABLE doctors (doctor_name text, doctor_surname text, PRIMARY KEY (doctor_name, doctor_surname));

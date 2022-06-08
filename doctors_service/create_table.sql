CREATE TABLE doctors (doctor_name TEXT, doctor_surname TEXT, doctor_id INT, department TEXT, experience TEXT, room INT, assigned_patients integer[10], PRIMARY KEY(doctor_id));


INSERT INTO doctors VALUES ('Nick', 'H', 1, 'heart', 'a lot', 20, ARRAY [1]);
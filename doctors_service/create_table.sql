CREATE TABLE patients (patient_name TEXT, patient_surname TEXT, patient_id INT, status TEXT, assigned_doctor_id INT, age INT, sex TEXT, diagnosis TEXT, registration_date TIMESTAMP, PRIMARY KEY(patient_id));


INSERT INTO patients VALUES ('Joe', 'J', 1, 'sick', 2, 20, 'male', 'headache', '2016-06-22 19:10:25-07');
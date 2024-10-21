CREATE DATABASE IF NOT EXISTS ophthalmology_patients;
CREATE TABLE IF NOT EXISTS patient
(
  patientid CHAR(8) NOT NULL,
  firstName VARCHAR(255) NOT NULL,
  lastName VARCHAR(255) NOT NULL,
  PRIMARY KEY (patientid)
);

CREATE TABLE IF NOT EXISTS queue
(
  registrationid CHAR(25) NOT NULL,
  patientid CHAR(8) NOT NULL,
  queuedate DATE NOT NULL,
  queueat TIME NOT NULL,
  PRIMARY KEY (registrationid),
  FOREIGN KEY (patientid) REFERENCES patient(patientid)
);

CREATE TABLE IF NOT EXISTS queuedetail
(
  id int NOT NULL AUTO_INCREMENT,
  registrationid CHAR(25) NOT NULL,
  subspecialty VARCHAR(255) NOT NULL,
  waitingtime INT NOT NULL,
  examtime INT NOT NULL,
  caretime INT NOT NULL,
  insurance VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (registrationid) REFERENCES queue(registrationid)
);

# Patient
INSERT INTO patient(patientid, firstName, lastName) VALUES ('12632466', 'Ediyanto', ' '),
('12641025','Fatkul', 'Rozak'),
('12573804','Dharmawan', 'Utomo'),
('12683246', 'Ibnu', 'Krisdianto'),
('12697269','Arif', 'Delianto');

# Queue
INSERT INTO queue (patientid, registrationid, queuedate, queueat) VALUES
('12632466','01.18.01.201800343896.009', '2018-09-10', '04:37'),
('12641025','01.18.01.201800335888.002', '2018-09-03', '01:51'),
('12573804','01.18.01.201800352179.026', '2018-09-17', '05:35'),
('12683246','01.18.01.201800366153.007', '2018-09-10', '07:08'),
('12697269','01.18.01.201800344234.001', '2018-09-10', '07:19');

# Queue Detail
INSERT INTO queuedetail (registrationid, subspecialty, waitingtime, examtime, caretime, insurance) VALUES
('01.18.01.201800343896.009', 'Rekonstruksi', 534, 111, 645, 'BPJS'),
('01.18.01.201800335888.002', 'Rekonstruksi', 555, 86, 641, 'BPJS'),
('01.18.01.201800352179.026', 'Retina', 294, 284, 579, 'Mandiri'),
('01.18.01.201800366153.007', 'Neuro Ophthalmology', 159, 358, 517, 'BPJS'),
('01.18.01.201800344234.001', 'Glaukoma', 508, 101, 609, 'BPJS')
;
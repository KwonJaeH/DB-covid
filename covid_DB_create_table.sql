CREATE TABLE CASE_INFO(
	Case_id INT NOT NULL,
	Province VARCHAR(50),
	City VARCHAR(50),
	Infection_group TINYINT(1),
	Infection_case VARCHAR(50),
	Confirmed INT,
	Latitude FLOAT,
	Longitude FLOAT,
	PRIMARY KEY (Case_id)
	);

CREATE TABLE REGION(
	Region_code INT NOT NULL,
	Province VARCHAR(50),
	City VARCHAR(50),
	Latitude FLOAT,
	Longitude FLOAT,
	Elementary_school_count INT,
	Kindergarten_count INT,
	University_count INT,
	Academy_ratio FLOAT,
	Elderly_population_ratio FLOAT,
	Elderly_alone_ratio FLOAT,
	Nursing_home_count INT,
	PRIMARY KEY (Region_code)
	);

CREATE TABLE PATIENT_INFO(
	Patient_id BIGINT NOT NULL,
	Sex VARCHAR(10),
	Age VARCHAR(10),
	Country VARCHAR(50),
	Province VARCHAR(50),
	City VARCHAR(50),
	Infection_case VARCHAR(50),
	Infected_by BIGINT,
	Contact_number INT,
	Symptom_onset_date DATE,
	Confirmed_date DATE,
	Released_date DATE,
	Decreased_date DATE,
	State VARCHAR(20),
	PRIMARY KEY (Patient_id)
	);

CREATE TABLE WEATHER(
	Region_code INT NOT NULL,
	Province VARCHAR(50),
	Wdate DATE NOT NULL,
	Avg_temp FLOAT,
	Min_temp FLOAT,
	Max_temp FLOAT,
	PRIMARY KEY (Region_code,Wdate)
	);

CREATE TABLE TIME_INFO(
	Date DATE NOT NULL,
	Test INT(11),
	Negative INT(11),
	Confirmed INT(11),
	Released INT(11),
	Decreased INT(11),
	PRIMARY KEY (Date)
	);

CREATE TABLE TIME_AGE(
	Date DATE NOT NULL,
	Age VARCHAR(10) NOT NULL,
	Confirmed INT(11),
	Decreased INT(11),
	PRIMARY KEY (Date,Age)
	);

CREATE TABLE TIME_GENDER(
	Date DATE NOT NULL,
	Sex VARCHAR(10),
	Confirmed INT(11),
	Decreased INT(11),
	PRIMARY KEY (Date,Sex)
	);

CREATE TABLE TIME_PROVINCE(
	Date DATE NOT NULL,
	Province VARCHAR(50),
	Confirmed INT(11),
	Released INT(11),
	Decreased INT(11),
	PRIMARY KEY (Date,Province)
	);

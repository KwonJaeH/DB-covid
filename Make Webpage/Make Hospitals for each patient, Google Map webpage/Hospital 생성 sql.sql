CREATE TABLE HOSPITAL(
	Hospital_id BIGINT NOT NULL,
	Name VARCHAR(100),
	Province VARCHAR(100),
	City VARCHAR(100),
	Latitude FLOAT,
	Longitude FLOAT,
	Capacity INT,
	Current INT,
	PRIMARY KEY (Hospital_id)
	);


CREATE TABLE ALL_REGION(
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


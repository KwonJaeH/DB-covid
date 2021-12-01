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


CREATE TABLE DWH.OBSERVATION (	
	ID SERIAL PRIMARY KEY,
	BIRD_SPECIE_ID INTEGER,
	LOCATION_ID INTEGER,
	BIRD_COUNT SMALLINT DEFAULT 1,
	OBSERVATION_DTTM TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	OBSERVATION_TYPE CHAR(1) CHECK (OBSERVATION_TYPE IN ('S', 'H', 'P')),
	IS_UNSURE BOOLEAN DEFAULT FALSE,
	LOCATION_DETAILS VARCHAR(512),
	OBSERVATION_DETAILS VARCHAR(1024),
	FOREIGN KEY (BIRD_SPECIE_ID) REFERENCES DWH.BIRD_SPECIE(ID),
	FOREIGN KEY (LOCATION_ID) REFERENCES DWH.LOCATION(ID)
);
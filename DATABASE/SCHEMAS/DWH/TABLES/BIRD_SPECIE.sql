CREATE TABLE DWH.BIRD_SPECIE (
	ID SERIAL PRIMARY KEY,
	POLISH_NAME VARCHAR(32) UNIQUE,
	ENGLISH_NAME VARCHAR(32) UNIQUE,
	LATIN_NAME VARCHAR(32) UNIQUE,
	CATEGORY CHAR(1),
	STATUS VARCHAR(5),
	IS_AVIFAUNA BOOLEAN,
	TIER CHAR(1) DEFAULT '-' CHECK (TIER IN ('S', 'A', 'B', 'C', 'D', 'E', 'F', '-', 'X')),
	IS_SEEN BOOLEAN DEFAULT FALSE
);
CREATE OR REPLACE VIEW DM.BIRD_SPECIE_PL AS (
SELECT
	o.ID,
	b.POLISH_NAME,
	l.AREA,
	l.NAME,
	o.BIRD_COUNT,
	TO_CHAR(o.OBSERVATION_DTTM, 'YYYY-MM-DD HH24:MI:SS') AS OBSERVATION_DTTM,
	o.OBSERVATION_TYPE
FROM DWH.OBSERVATION o
JOIN DWH.BIRD_SPECIE b
	ON o.BIRD_SPECIE_ID = b.ID
JOIN DWH.LOCATION l
	ON o.LOCATION_ID = l.ID);
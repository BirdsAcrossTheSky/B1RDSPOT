--add new value to bird_specie_tier_check
/*
SELECT constraint_name, table_name
FROM information_schema.table_constraints
WHERE 1 = 1
	--AND table_name = 'BIRD_SPECIE' 
	AND constraint_type = 'CHECK';
*/

ALTER TABLE DWH.BIRD_SPECIE
DROP CONSTRAINT bird_specie_tier_check;

ALTER TABLE DWH.BIRD_SPECIE
ADD CONSTRAINT bird_specie_tier_check CHECK (TIER IN ('S', 'A', 'B', 'C', 'D', 'E', 'F', '-', 'X'));
--conversion to text as point data type is not supported for on conflict
CREATE UNIQUE INDEX COORDINATES_UNIQ_IDX ON DWH.LOCATION ((COORDINATES::TEXT));


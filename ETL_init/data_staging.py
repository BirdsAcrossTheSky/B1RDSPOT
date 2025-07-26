import csv
import psycopg2
import configparser
import json
import datetime

# getting connection parameters from .ini config file
config = configparser.ConfigParser()
config.read('conf/db_config.ini')
conn_params = config['postgresql']

# getting stage date
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

# getting table info from .json config_file
with open('conf/table_config.json') as tab_cfg_f:
    table_dict_list = json.load(tab_cfg_f)

# getting location data from .json file
location_data_path = 'EXTRACT/data/imported/googlemaps_location_data.json'
with open(location_data_path, 'r', encoding='utf-8') as location_file:
    location_data = json.load(location_file)

# getting lifers data
lifers_data_path = 'EXTRACT/data/imported/lifers.csv'
with open(lifers_data_path, 'r') as lifers_file:
    reader = csv.DictReader(lifers_file)
    lifers_list = [row['Nazwa gatunku'].rstrip().lower() for row in reader if row['Nazwa gatunku'] != '']
    print(lifers_list)

# loading imported data to database
with psycopg2.connect(**conn_params) as conn:

    # bird species data
    for table_dict in table_dict_list:
        with conn.cursor() as cur:
            # deleting all the data from table
            del_sql = f"DELETE FROM STAGE.{table_dict['name']} WHERE STAGEDATE = '{current_date}'"
            cur.execute(del_sql)

            with open(table_dict['csv'], 'r') as f:
                # next(f)  # skipping the header
                cur.copy_expert(sql=table_dict['copy_sql'], file=f)
                print(f"The data was inserted into STAGE.{table_dict['name']}")

            conn.commit()

    # location data
    with conn.cursor() as cur:
        cur.execute(f"DELETE FROM STAGE.GOOGLE_MAPS_LOCATION WHERE STAGEDATE = '{current_date}'")
        for feature in location_data['features']:
            cur.execute("INSERT INTO STAGE.GOOGLE_MAPS_LOCATION (NAME, COORDINATES) VALUES (%s, POINT(%s, %s))",
                        (feature['properties']['name'], feature['geometry']['coordinates'][0],
                         feature['geometry']['coordinates'][1]))
        conn.commit()
        print(f"The data was inserted into STAGE.GOOGLE_MAPS_LOCATION")

    # lifers data
    with conn.cursor() as cur:
        cur.execute(f"DELETE FROM STAGE.LIFERS WHERE STAGEDATE = '{current_date}'")
        for lifer in lifers_list:
            cur.execute(f"INSERT INTO STAGE.LIFERS (NAME) VALUES ('{lifer}')")
        conn.commit()
        print(f"The data was inserted into STAGE.LIFERS")

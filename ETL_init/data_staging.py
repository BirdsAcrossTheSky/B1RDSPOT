import psycopg2
import configparser
import json


# getting connection parameters from .ini config file
config = configparser.ConfigParser()
config.read('conf/db_config.ini')
conn_paramas = config['postgresql']

# getting table info from .json config_file
with open('conf/table_config.json') as tab_cfg_f:
    table_dict_list = json.load(tab_cfg_f)

# loading imported data to database
with psycopg2.connect(**conn_paramas) as conn:
    for table_dict in table_dict_list:
        with conn.cursor() as cur:
            # deleting all the data from table
            del_sql = f"DELETE FROM STAGE.{table_dict['name']}"
            cur.execute(del_sql)

            with open(table_dict['csv'], 'r') as f:
                next(f)  # skipping the header
                cur.copy_expert(sql=table_dict['copy_sql'], file=f)
                print(f"The data was inserted into STAGE.{table_dict['name']}")

            conn.commit()


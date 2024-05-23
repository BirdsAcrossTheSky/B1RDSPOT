import psycopg2
import configparser


config = configparser.ConfigParser()
config.read('conf/db_config.ini')
conn_paramas = config['postgresql']

# List of dictionaries to hold CSV paths and SQL copy commands
table_dict_list = [
    {
        'name': 'list',
        'csv': 'EXTRACT/data/to_db/list_db.csv',
        'copy_sql': """
COPY STAGE.LIST (LATIN_NAME, POLISH_NAME, ENGLISH_NAME, CATEGORY, STATUS)
FROM stdin WITH CSV HEADER DELIMITER as ','
"""
    },
    {
        'name': 'annex',
        'csv': 'EXTRACT/data/to_db/annex_db.csv',
        'copy_sql': """
COPY STAGE.ANNEX (LATIN_NAME, POLISH_NAME, ENGLISH_NAME, CATEGORY, STATUS)
FROM stdin WITH CSV HEADER DELIMITER as ','
"""
    },
    {
        'name': 'category',
        'csv': 'EXTRACT/data/to_db/category_db.csv',
        'copy_sql': """
COPY STAGE.CATEGORY (CATEGORY, DESCRIPTION)
FROM stdin WITH CSV HEADER DELIMITER as ','
"""
    },
    {
        'name': 'status',
        'csv': 'EXTRACT/data/to_db/status_db.csv',
        'copy_sql': """
COPY STAGE.STATUS (STATUS, DESCRIPTION)
FROM stdin WITH CSV HEADER DELIMITER as ','
"""
    }
]


with psycopg2.connect(**conn_paramas) as conn:
    for table_dict in table_dict_list:
        with conn.cursor() as cur:
            del_sql = f"DELETE FROM STAGE.{table_dict['name']}"
            with open(table_dict['csv'], 'r') as f:
                next(f)  # skipping the header
                cur.copy_expert(sql=table_dict['copy_sql'], file=f)
                print(f"The data was inserted into STAGE.{table_dict['name']}")

            conn.commit()


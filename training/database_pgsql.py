import psycopg
from psycopg.rows import dict_row
import os
from dotenv import load_dotenv


load_dotenv()

try:
    db = psycopg.connect(
        user=os.getenv("PGSQL_USER"),
        password=os.getenv("PGSQL_PASSWORD"),
        host=os.getenv("PGSQL_HOST"),
        port=int(os.getenv("PGSQL_PORT")),
        dbname=os.getenv("PGSQL_DBNAME")
    )

    with db:
        with db.cursor(row_factory=dict_row) as cursor:
            cursor.execute("SELECT * FROM rna LIMIT 1")
            # fetchone не оборачивает результат в list, сразу выдает dict
            data_dict = cursor.fetchone()
            print(data_dict)
            print(data_dict['id'])



except (psycopg.Error, TypeError, ValueError) as e:
    print(f'Error: {e}')
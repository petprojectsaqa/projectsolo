import mysql.connector as mysql
import os
from dotenv import load_dotenv

db = None

load_dotenv()

try:
    db = mysql.connect(
        user=os.getenv("USER"),
        passwd=os.getenv("PASSWD"),
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT")),
        database=os.getenv("DATABASE")
    )

    with db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            print(cursor.fetchall())

except (mysql.Error, TypeError, ValueError) as e:
    print(f'Error: {e}')
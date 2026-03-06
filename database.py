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
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM students")
            data = cursor.fetchall()
            for student in data:
                print(student['second_name'])

            cursor.execute("SELECT * FROM students WHERE id = 2")
            data2 = cursor.fetchone()
            print(data2)



except (mysql.Error, TypeError, ValueError) as e:
    print(f'Error: {e}')
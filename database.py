import mysql.connector as mysql
import os
from dotenv import load_dotenv


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
            cursor.execute("SELECT * FROM family WHERE rfam_acc = 'RF00001'")
            # fetchone не оборачивает результат в list, сразу выдает dict
            data_dict = cursor.fetchone()
            print(data_dict['rfam_acc'])

            # плохо, что реюзаем код
            cursor.execute("SELECT * FROM family WHERE rfam_acc = 'RF00001'")
            # fetchall оборачивает dict'ы в list
            data_list = cursor.fetchall()
            print(data_list[0]['rfam_acc'])



except (mysql.Error, TypeError, ValueError) as e:
    print(f'Error: {e}')
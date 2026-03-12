import mysql.connector as mysql
import os
from dotenv import load_dotenv
import json


load_dotenv()

try:
    db = mysql.connect(
        user=os.getenv("MYSQL_USER"),
        passwd=os.getenv("MYSQL_PASSWD"),
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        database=os.getenv("MYSQL_DATABASE")
    )

    with db:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM family WHERE rfam_acc = 'RF00001'")
            # fetchone не оборачивает результат в list, сразу выдает dict
            data_dict = cursor.fetchone()
            print(data_dict['rfam_acc'])

            cursor.execute("SELECT * FROM family LIMIT 10")
            # fetchall оборачивает dict'ы в list
            data_list = cursor.fetchall()
            print(data_list[0])
            print(json.dumps(data_list, indent=4, default=str))
            for line in data_list:
                print(line['rfam_id'])


except (mysql.Error, TypeError, ValueError) as e:
    print(f'Error: {e}')
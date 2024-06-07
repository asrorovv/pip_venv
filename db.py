from dotenv import load_dotenv
import os
import psycopg2 as psql
load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database=os.getenv('db_name'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            host=os.getenv('db_host'),
            port=os.getenv('db_port')
        )
        cursor = db.cursor()
        cursor.execute(query)
        data = ['alter', 'update', 'insert', 'delete']
        if query_type in data:
            return db.commit()


        else:
            return cursor.fetchall()


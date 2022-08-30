import psycopg2
import sys

def get_postgres_connection():
    conn = psycopg2.connect(
        host='localhost',
        port=54320,
        dbname='my_database',
        user='postgres',
        password='my_password',
    )
    return conn

def add_data_to_db(num, data):
    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute(f"INSERT INTO test (num, data) VALUES ({num}, '{data}')")
    cur.execute("SELECT * FROM test;")
    result = cur.fetchall()
    print(result)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    args = sys.argv
    add_data_to_db((args[1]), args[2])




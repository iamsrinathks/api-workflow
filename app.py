from flask import Flask
import psycopg2
import os

app = Flask(__name)

# Define the database connection parameters.
db_params = {
    'dbname': os.environ.get('DB_NAME', 'your-db-name'),
    'user': os.environ.get('DB_USER', 'your-db-username'),
    'password': os.environ.get('DB_PASS', 'your-db-password'),
    'host': '127.0.0.1',  # Local host where the Cloud SQL proxy is running
    'port': '5432',       # Port used by the Cloud SQL proxy
}

def query_postgres():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()[0]
        return f'Database version: {db_version}'
    except Exception as e:
        return f'Error: {str(e)}'
    finally:
        if conn:
            conn.close()

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/query_postgres')
def query_database():
    result = query_postgres()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

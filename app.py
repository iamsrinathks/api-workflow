from flask import Flask
import psycopg2

app = Flask(__name)

# Define the database connection parameters.
db_params = {
    'dbname': 'your-db-name',
    'user': 'your-db-username',
    'password': 'your-db-password',
    'host': 'your-db-host',
    'port': 'your-db-port',
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

from flask import Flask, request, render_template
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load database configuration
config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
}

def get_db_connection():
    # Ensure database configuration is complete
    if not all(config.values()):
        raise ValueError("Database configuration is incomplete. Check your .env file.")
    return mysql.connector.connect(**config)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def join():
    username = request.form['username']
    email = request.form['email']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(query, (username, email))
        conn.commit()
        cursor.close()
        conn.close()
        message = "Successfully added to the database."
    except Exception as e:
        message = f"An error occurred: {e}"

    return render_template('index.html', message=message)

@app.route('/view', methods=['GET'])
def view():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT username, email FROM users ORDER BY id"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        users = []
        message = f"An error occurred: {e}"
        return render_template('index.html', message=message, users=users)

    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)  # Listen on all interfaces for Docker

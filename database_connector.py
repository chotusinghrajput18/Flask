from flask import Flask
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)
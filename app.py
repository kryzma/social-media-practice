# app.py
from flask import Flask, jsonify, send_from_directory
from db import init_db, fetch_users

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('static', 'sus_dog.jpg')

@app.route('/users')
def users():
    user_records = fetch_users()
    users_list = [{'id': user[0], 'username': user[1], 'email': user[2]} for user in user_records]
    return jsonify(users_list)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')

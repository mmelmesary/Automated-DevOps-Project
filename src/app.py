from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import os 
mysql_port = int(os.environ.get("MYSQL_PORT", 3306))

app = Flask(__name__)

app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
app.config["MYSQL_PORT"] = mysql_port

mysql = MySQL(app)

@app.route("/")
def hello_there():
    return "Hello there!"

@app.route("/data", methods=["GET"])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user_info")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user_info WHERE id = %s", (id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    cur = mysql.connection.cursor()
    name = request.json['name']
    age = request.json['age']
    job_title = request.json['job_title']
    cur.execute('''INSERT INTO user_info (name, age, job_title) VALUES (%s, %s, %s)''', (name, age, job_title))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Data added successfully'})


@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    cur = mysql.connection.cursor()
    name = request.json['name']
    age = request.json['age']
    job_title = request.json['job_title']
    cur.execute('''UPDATE user_info SET name = %s, age = %s, job_title = %s WHERE id = %s''', (name, age, job_title, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Data updated successfully'})


@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    cur = mysql.connection.cursor()
    cur.execute('''DELETE FROM user_info WHERE id = %s''', (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Data deleted successfully'})

if __name__ == '__main__':
    app.run()
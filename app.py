from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Povezava z bazo
def get_db_connection():
    conn = psycopg2.connect(
        host="autorack.proxy.rlwy.net",
        database="railway",
        user="postgres",
        password="LTJOtlHzAuHfYZPmyFqTDuxeFQWniNQb",
        port="21288"
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Hello, World Engineer!"})   

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    name = data.get('name')
    surname = data.get('surname')
    age = data.get('age')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO temp_table (name, surname, age) VALUES (%s, %s, %s)',
                (name, surname, age))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Data inserted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

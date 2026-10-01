from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "localhost",       
    "user": "root",            
    "password": "",    
    "database": "sample"      
}


def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

#http://127.0.0.1:5000/vehicle
@app.route('/vehicle', methods=['POST'])
def add_vehicle():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    data = request.json
    number_plate = data.get('number_plate')
    # print(number_plate)

    cursor = conn.cursor()
    try:
        # Insert into parking_slots table
        cursor.execute("""
            INSERT INTO parking_slots (vehicle_number, status, booked_at, name) 
            VALUES (%s, %s, NOW(), %s)
        """, (number_plate, '1', 'Sample Name')) 
        conn.commit()
        return jsonify({"message": "Vehicle added successfully"}), 201
    except mysql.connector.Error as err:
        print(f"Insert Error: {err}")
        return jsonify({"error": "Failed to add vehicle"}), 500
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)

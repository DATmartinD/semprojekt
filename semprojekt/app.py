from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def control_panel():
    return render_template('control_panel.html')

@app.route('/gps')
def gps_data():
    return render_template('gps_data.html')

@app.route('/pulse')
def pulse_data():
    return render_template('pulse_data.html')

@app.route('/o2')
def o2_data():
    return render_template('o2_data.html')

@app.route('/get_latest_pulse')
def get_latest_pulse():
    pulse = get_pulse_reading()
    return jsonify({'pulse': pulse})

@app.route('/get_latest_o2')
def get_latest_o2():
    o2 = get_o2_reading()
    return jsonify({'o2': o2})

@app.route('/alarm')
def alarm():
    #Logic for alarm here
    pass

@app.route('/get_latest_gps')
def get_latest_gps():
    gps_data = get_gps_reading()
    return jsonify(gps_data)

def get_pulse_reading():
    # Connect to the database
    connection = mysql.connector.connect(
        host="funnyfisher-do-user-14699515-0.b.db.ondigitalocean.com",
        user="doadmin",
        password="AVNS_67OBeYl4KOwgJ3pArzP",
        database="semprojekt",
        port=25060
    )

    cursor = connection.cursor()

    # SQL query to fetch the latest pulse reading
    query = "SELECT latest_pulse_value FROM data ORDER BY id DESC LIMIT 1"
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    # Return the result
    return result[0] if result else None

def get_o2_reading():
    # Connect to the database
    connection = mysql.connector.connect(
        host="funnyfisher-do-user-14699515-0.b.db.ondigitalocean.com",
        user="doadmin",
        password="AVNS_67OBeYl4KOwgJ3pArzP",
        database="semprojekt",
        port=25060
    )

    cursor = connection.cursor()

    # SQL query to fetch the latest pulse reading
    query = "SELECT o2_concentration FROM data ORDER BY id DESC LIMIT 1"
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    # Return the result
    return result[0] if result else None

def get_gps_reading():
    # Connect to the database
    connection = mysql.connector.connect(
        host="funnyfisher-do-user-14699515-0.b.db.ondigitalocean.com",
        user="doadmin",
        password="AVNS_67OBeYl4KOwgJ3pArzP",
        database="semprojekt",
        port=25060
    )

    cursor = connection.cursor()

    # SQL query to fetch the latest GPS data
    query = "SELECT gps_latitude, gps_longitude FROM data ORDER BY id DESC LIMIT 1"
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        # If result is not None, return the data
        latitude, longitude = result
        return {'latitude': latitude, 'longitude': longitude}
    else:
        # Return a default value or None if no data is found
        return {'latitude': None, 'longitude': None}

if __name__ == '__main__':
    app.run(debug=True)

import serial
import pynmea2
import mysql.connector
from time import sleep

# Open the serial connection to the GPS module
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

connection = mysql.connector.connect(
        host="funnyfisher-do-user-14699515-0.b.db.ondigitalocean.com",
        user="doadmin",
        password="AVNS_67OBeYl4KOwgJ3pArzP",
        database="semprojekt",
        port=25060
)
cursor = connection.cursor()

while True:
    # Read a line from the serial port
    line = ser.readline()

    add_data = ("INSERT INTO data "
            "(gps_latitude, gps_longitude) "
            "VALUES (%s, %s)")

    # Try parsing the line as an NMEA sentence
    if line.startswith('$GPGGA'):
        try:
            nmea_obj = pynmea2.parse(line)
            print(f"Latitude: {nmea_obj.latitude}, Longitude: {nmea_obj.longitude}")
            data_values = (nmea_obj.latitude, nmea_obj.longitude)
            cursor.execute(add_data, data_values)
            connection.commit()
            cursor.close()
            connection.close()
        except pynmea2.ParseError:
            pass  
    sleep(50)
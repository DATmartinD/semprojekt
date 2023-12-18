from max30102 import MAX30102
from machine import SoftI2C, Pin
from time import sleep
import mysql.connector

# Example I2C setup
i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=400000)
sensor = MAX30102(i2c=i2c)

connection = mysql.connector.connect(
        host="funnyfisher-do-user-14699515-0.b.db.ondigitalocean.com",
        user="doadmin",
        password="AVNS_67OBeYl4KOwgJ3pArzP",
        database="semprojekt",
        port=25060
)
cursor = connection.cursor()

while True:
    sensor.check()
    if sensor.available():
        red_sample = sensor.pop_red_from_storage()
        ir_sample = sensor.pop_ir_from_storage()
        add_data = ("INSERT INTO data "
            "(latest_pulse_value, o2_concentration) "
            "VALUES (%s, %s)")
        data_values = (red_sample, ir_sample)
        print(red_sample, ",", ir_sample)
        cursor.execute(add_data, data_values)
        connection.commit()
        cursor.close()
        connection.close()
    sleep(50)




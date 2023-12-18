import mysql.connector

# Database connection details
connection = mysql.connector.connect(
    host="funnyfisher-do-user-14699515-0.b.db.ondigitalocean.com",
    user="doadmin",
    password="AVNS_67OBeYl4KOwgJ3pArzP",
    database="semprojekt",
    port=25060
)
cursor = connection.cursor()

# SQL statement to insert data
add_data = ("INSERT INTO data "
            "(latest_pulse_value, gps_latitude, gps_longitude, o2_concentration) "
            "VALUES (%s, %s, %s, %s)")

# Hardcoded data to insert
data_values = (79, 35.7749, -120.4194, 94.6)  # Example values

# Insert the data
cursor.execute(add_data, data_values)

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("DONE!")
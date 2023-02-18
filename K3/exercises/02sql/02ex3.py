import sqlite3 # We import sqlite3 
import matplotlib.pyplot as plt

db = sqlite3.connect('turbine.db') # We connect to our database (or create it)
cur = db.cursor() # We get the cursor

# Create temperature database
cur.execute("CREATE TABLE turbine_measurement (id INTEGER PRIMARY KEY AUTOINCREMENT, temperature FLOAT(4), power FLOAT(4), pressure INTEGER, date_time VARCHAR(256));")

# We open the file and insert each row into the database
with open("./turbine_data.txt") as f:
    for line in f:
        row = line.split(",")
        temperature = float(row[0])
        power = float(row[1])
        pressure = int(row[2])
        date_time = row[3].rstrip()
        cur.execute(f"INSERT INTO turbine_measurement(temperature, power, pressure, date_time) VALUES('{temperature}','{power}','{pressure}','{date_time}');")

# We get every temperature measurement from the database
res = cur.execute("SELECT temperature FROM turbine_measurement")
data = res.fetchall()

# We save the temperature in a file
temperature = []
for turbine_data in data:
    temperature.append(turbine_data)

# We plot the temperature over time
plt.plot(temperature)
plt.show()
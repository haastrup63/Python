import sqlite3 # We import sqlite3 

with open('populate.sql', 'r') as sql_file: # We open our sql file
    sql_script = sql_file.read() # We read it into a "script (just a string)"

db = sqlite3.connect('beers.db') # We connect to our database (or create it)
cur = db.cursor() # We get the cursor
cur.executescript(sql_script) # We populate the database with the script

# Insert new brewery first 
cur.execute("INSERT INTO brewery (name, address, country ) VALUES" + 
            "('Anders Hjemmebryggeri', 'Fantasivej 2, 5000 Odense', 'Denmark')");

# Then insert new beers
cur.execute("INSERT INTO beer (name, alc, kind, brewery_id) VALUES" +
            "('Bos Finest 45', '9', 'stout', '4')," +
            "('Bos Pilz', '4.5', 'pilsner', '4')," +
            "('Bos Klasse', '4.6', 'classic', '4')")
db.commit()

# Then get all beers with percentage larger than 4.5
result = cur.execute("SELECT * FROM beer WHERE alc > 4.6")
# Fetch all beers and save them in array
beers = result.fetchall()
# Print every beer in beers
for beer in beers:
    print(beer)
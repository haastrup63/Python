from beer import Beer 
from brewery import Brewery
import sqlite3 

db = sqlite3.connect('beers.db') # We connect to the database we created in exercise 1
cur = db.cursor() # We get the cursor

# Get all beers
beers = []
beer_results = cur.execute("SELECT * FROM beer").fetchall()
for beer_res in beer_results:
    beer = Beer(beer_res[0], beer_res[1], beer_res[2], beer_res[3], beer_res[4])
    beers.append(beer)

# Get all breweries
breweries = []
brewery_results = cur.execute("SELECT * FROM brewery").fetchall()
for brewery_res in brewery_results:
    brewery = Brewery(brewery_res[0], brewery_res[1], brewery_res[2], brewery_res[3])
    breweries.append(brewery)

# Print beers (looks pretty thanks to __str__)
print("-- Beers --")
for beer in beers:
    print(beer)

# Print breweries (looks pretty thanks to __str__)
print("-- Breweries --")
for brewery in breweries:
    print(brewery)
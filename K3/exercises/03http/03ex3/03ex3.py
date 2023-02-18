import sqlite3 # We import sqlite3 
from flask import Flask

db = sqlite3.connect('beers.db', check_same_thread=False) # We connect to our database, i copied the one from exercise 02ex1
cur = db.cursor() # We get the cursor

app = Flask(__name__) 

@app.route('/beers/')
def beers():
    res = cur.execute("SELECT * FROM beer").fetchall()
    beer_list = []
    for b in res: 
        beer_list.append({ "id" : b[0], "name" : b[1], "alc" : b[2], "kind" : b[3], "brewery_id" : b[4] })
    return { "beers" : beer_list }
 
@app.route('/beer/<kind>')
def beer(kind):
    res = cur.execute(f"SELECT * FROM beer WHERE kind = '{kind}'").fetchall()
    beer_list = []
    for b in res: 
        beer_list.append({ "id" : b[0], "name" : b[1], "alc" : b[2], "kind" : b[3], "brewery_id" : b[4] })
    return { "beers" : beer_list }

if __name__ == '__main__':
    app.run(port=8000)
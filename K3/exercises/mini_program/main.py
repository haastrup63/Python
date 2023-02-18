from flask import Flask, request
from database import DataBase
from beer import Beer

db = None
app = Flask(__name__)

@app.route('/api/beer/<name>', methods=['GET', 'POST'])
def beer(name):
    if (request.method == 'GET'):
        res = db.get_specific_beer(name)
        beer_response = list(map(lambda b: { "id" : b[0], "name" : b[1], "alc" : b[2], "kind" : b[3], "brewery_id" : b[4] }, res))
    else: 
        beer_json = request.get_json()['beer']
        print(beer_json)
        beer = Beer(beer_json['name'], beer_json['alc'], beer_json['kind'], beer_json['brewery_id'])
        res = db.insert_beer(beer)
        beer_response = list(map(lambda b: { "id" : b[0], "name" : b[1], "alc" : b[2], "kind" : b[3], "brewery_id" : b[4] }, res))
    return { "beer": beer_response }

@app.route('/api/beers/')
def beers():
    res = db.get_all_beers()
    beers = list(map(lambda b: { "id" : b[0], "name" : b[1], "alc" : b[2], "kind" : b[3], "brewery_id" : b[4] }, res))
    return { "beers" : beers }

if __name__ == '__main__':
    # type = 'SQL'
    type = 'SQLite'
    db = DataBase(type)
    db.populate("./populate_sqlite.sql")
    app.run(port=8000)
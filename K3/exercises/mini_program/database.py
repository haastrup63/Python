import sqlite3 
import psycopg2

class DataBase:
    def __init__(self, type):
        self.type = type

    def connect(self):
        if (self.type == "SQL"):    
            self.con = psycopg2.connect(
                host='localhost',
                port=54320,
                dbname='beer_db',
                user='postgres',
                password='my_password',
            )
        else: 
            self.con = sqlite3.connect('mydb.db', check_same_thread=False)

    def populate(self, path):
        self.connect()
        with open(path, 'r') as sql_file: 
            sql_script = sql_file.read()
        cur = self.con.cursor()
        cur.executescript(sql_script) 
        cur.close()
        self.con.close()

    def get_all_beers(self):
        self.connect()
        cur = self.con.cursor()
        cur.execute("SELECT * FROM beer")
        result = cur.fetchall()
        cur.close()
        self.con.close()
        return result

    def get_specific_beer(self, name):
        self.connect()
        cur = self.con.cursor()
        query = f"SELECT * FROM beer WHERE name = '{name}'"
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        self.con.close()
        return result

    def insert_beer(self, beer):
        self.connect()
        cur = self.con.cursor()
        query = f"INSERT INTO beer (name, alc, kind, brewery_id) VALUES('{beer.name}', '{beer.alc}', '{beer.kind}', '{beer.brewery_id}');"
        print(query)
        cur.execute(query)
        self.con.commit()
        cur.close()
        self.con.close()
        return self.get_specific_beer(beer.name)
from fastapi import FastAPI, Body, status
from cur_parser import parser


def take_db(url):
    return parser(url)


class Data:
    def __init__(self):
        self.db = {}

    def import_db(self, db):
        self.db = db
        return "db has set"

    def print_db(self):
        return self.db

    def edit_db(self, currency, value):
        self.db[currency] = value
        return "{} set to {}".format(currency, self.db[currency])

    def remove_db(self, currency):
        return self.db.pop(currency)


app = FastAPI()


@app.get("/")
def info():
    return "какая-то документация"

@app.post("/api/import_db")
def import_db(database):
    return Data.import_db(database)


@app.post("/api/edit_db")
def edit_db(currency, value):
    return Data.import_db(database)
import sqlite3
from flask import g
from sql import app

DATABASE = 'sql/sqlite3.db'

def get_db():
    db = getattr(g, 'main', None)
    if db is None:
        db = g.main = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'main', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

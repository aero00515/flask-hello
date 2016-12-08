from flask import Flask
from sql import connection as dbConn

# Use BluePrint for larger future
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sql')
def sql():
    users = dbConn.query_db('select * from user')
    user = users[0]
    return str(user[1]) + ' has the id ' + str(user[0]);

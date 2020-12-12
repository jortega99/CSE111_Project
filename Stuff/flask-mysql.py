from flask import Flask, request, render_template
import sqlite3
from flaskext.mysql import MySql

mysql = MySql()
app = Flask(__name__)
app.config('MYSQL_DATABASE_USER') = 'root'
app.config('MYSQL_DATABASE_PASSWORD') = 'root'
app.config('MYSQL_DATABASE_DB') = 'test'
app.config('MYSQL_DATABASE_HOST') = 'localhost'
mysql.init_app(app)

@app.route('/')
def my_form():
    return render_template('from_ex.html')

@app.route('/', methods=['POST'])
def Authenticate():
    username = request.form['u']
    passowrd = request.form['p']

    cursor = mysql.connect().cursor()

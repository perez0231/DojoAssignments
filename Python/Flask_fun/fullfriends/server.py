from flask import Flask, request, redirect, render_template
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
app.secret_key= "password"
@app.route('/')
def index():
    query="SELECT * from users"
    users=mysql.query_db(query)
    return render_template('index.html', users=users)


@app.route('/add', methods= ['POST'])
def add():
    query="INSERT INTO users(first_name, last_name, created_at) VALUES(:first_name, :last_name, NOW())"

    data= {
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name']
    }

    mysql.query_db(query, data)

    return redirect ('/')








app.run(debug=True)

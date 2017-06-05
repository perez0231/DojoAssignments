from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print mysql.query_db("SELECT * FROM users")

from flask import Flask
app = Flask(name)
@app.route('/users', methods=['GET'])
def index():
    SELECT * from users
    pass
@app.route('/users', methods=['POST'])
def create():
     INSERT INTO table ( field1, field2,...fieldN ) VALUES ( value1, value2,...valueN )
    pass
@app.route('/users/<id>', methods=['GET'])
def show():
    select * from users where id = 1
    pass
@app.route('/users/<id>', methods=['POST'])
def update():
    UPDATE table
    SET column1=updatedvalue, column2=updated value2,...
    WHERE id=1
    pass
@app.route('/users/<id>/delete')
def delete():

    DELETE FROM table where id = 1

@app.route('/users/new', methods=['GET'])
def new(): #just to show the create page
    pass
@app.route('/users/<id>/edit', methods=['GET'])
def edit(): #just to show the update page
    pass

app.run(debug=true)
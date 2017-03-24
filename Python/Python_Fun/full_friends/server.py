from flask import Flask, request, render_template, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
app.secret_key = "tacocat"
mysql = MySQLConnector(app, 'full_friends')
# an example of running a query

@app.route("/")
def index():
    query = "SELECT * FROM users"             # define your query
    users = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', users = users) # pass data to our template
@app.route("/friends", methods =["POST"])
def createFriend():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"

    data = {
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "email":request.form['email']
    }
    mysql.query_db(query, data)

    return redirect("/")
@app.route ("/friends/<id>/edit")
def edit(id):
    query = "SELECT * from users WHERE id = :id"
    data= {
    "id" : id
    }
    single_friend = mysql.query_db(query, data)
    return render_template("edit.html", users = single_friend)

@app.route("/friends/<id>", methods=["POST"])
def update(id):

    query = "UPDATE users Set first_name= :first_name, last_name= :last_name, email= :email, updated_at= NOW()  WHERE id = :id"

    data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email'],
                 "id" :id
    }

    mysql.query_db(query, data)
    return redirect("/")


@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
#     query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'email': request.form['email'],
#              'id': id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')




# @app.route('/friends/<id>')
# def show(id):
#     # Write query to select specific user by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM users WHERE id = :id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'id': id}
#     # Run query with inserted data.
#     friends = mysql.query_db(query, data)
#     # Friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_users=users[0])
#
# @app.route('/friends', methods=['POST'])
# def create():
#     print request.form['first_name']
#     print request.form['last_name']
#     print request.form['email']
#     # add a friend to the database!
#     return redirect('/')
#
# app.run(debug=True)



#
#
#
#
#
#
#
#
#
#
#
#
#

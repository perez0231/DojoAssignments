from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')


@app.route('/')
def index():
    query= "SELECT * FROM friends"
    friends = mysql.query_db(query)
    print friends
    return render_template('index.html', allfriends= friends)
@app.route('/friends', methods = ['POST'])
def create():
    #add friend
    return redirect ('/')

@app.route('/friends/<friend_id>')
# Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
   query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend=friends[0])

    
def show(friend_id)
app.run(debug=True)

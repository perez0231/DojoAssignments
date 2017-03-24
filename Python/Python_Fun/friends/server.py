from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
        friends = mysql.query_db("SELECT * FROM friends")
        print friends
        query = "SELECT * FROM friends"
        friends = mysql.query_db(query)
        return render_template('index.html', all_friends=friends)


@app.route('/friends/<friend_id>, edit')
def edit (friend_id):
        query= "Elect fr"

        # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.

    query = "SELECT *FROM friends WHERE id = :specific_id"

    data = {'specific_id': friend_id}
        # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend=friends[0])

@app.route('/friends', methods=['POST'])
def createfriends():
    query= "INSERT info users(first_name, last_name, email, created_at") Values ()

    mysql.query.db(query,data)

    return redirect ('/')

def create():
    #add a friend to the data base
    return redirect('/')

app.run(debug=True)

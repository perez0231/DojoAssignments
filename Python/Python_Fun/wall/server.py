from flask import Flask, request, redirect, render_template, session, flash

from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key ='daniel'


mysql =MySQLConnector(app, "the_wall")

import re
onlyLetters= re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)


@app.route('/')
def index():

    return render_template('index.html')

@app.route("/register", methods= ["POST"])
def registeruser():
    flag = False
    data={
        'email': request.form['email'],
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'password' :request.form['password'],
        'cpassword' :request.form['cpassword'],
    }
    if not onlyLetters.match(data['first']):
        flag = True
        flash('You can only have letters in your first name ')
    if len(data['first']) < 2:
        flag = True
        flash ('name must be 2 characters long')
    if not data['first']:
        flag =True
        flash ('MUST INPUT NAME')

    if not onlyLetters.match(data['last']):
        flag = True
        flash('You can only have letters in your first name ')
    if len(data['last']) < 2:
        flag = True
        flash ('name must be 2 characters long')
    if not data['last']:
        flag =True
        flash ('MUST INPUT NAME')

    if not EMAIL_REGEX.match(data['email']):
        flag= True
        flash ('must input valid email')
    if not data['email']:
        flag =True
        flash ('MUST INPUT EMAIL')

    if len(data['password']) < 8:
        flag = True
        flash('Password must be at LEAST 8 characters')

    if not data['password']:
        flag = True
        flash('Please enter password')

    if data['password'] != data['cpassword']:
        flag = True
        flash('Passwords do NOT match')


    if flag:
        return redirect('/')

    else:

        pw_hash = bcrypt.generate_password_hash(data['password'])

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :pass, NOW(), NOW())"


        query_data ={
        'email': data['email'],
        'first': data ['first'],
        'last': data ['last'],
        'pass' : pw_hash,
        }

        user_id= mysql.query_db(query, query_data)
        session['user_id']= user_id
        return redirect('/the_wall')

@app.route('/login', methods=['POST'])
def login():
    query="SELECT * from users where email = :email"

    data ={
        "email": request.form['email']

    }
    selecteduser= mysql.query_db(query, data)

    if not selecteduser:
        flash("invalid email")
        return redirect('/')

    else:
        if bcrypt.check_password_hash(selecteduser[0]['password'], request.form['password']):
            session['user_id']= selecteduser[0]['id']
            return redirect("/the_wall")
        else:
            flash("invalid credentials")
            return redirect('/')

@app.route("/the_wall")
def the_wall():
    if 'user_id' not in session:
        return redirect("/")

    query= "SELECT * from users where id = :id"

    data={
        "id": session['user_id']
    }

    logged_user = mysql.query_db(query, data)

    q_messages= "SELECT users.first_name, users.last_name, messages.id as message_id, messages.message from messages LEFT JOIN users on messages.user_id = users.id"
    messages= mysql.query_db(q_messages)

    c_messages= "SELECT users.first_name, users.last_name, comments.id as comment_id, comments.comment, comments.message_id from comments LEFT JOIN users on comments.user_id = users.id"
    comments= mysql.query_db(c_messages)
    #messages
    #comments
    return render_template('the_wall.html', user = logged_user[0], wall_messages= messages, wall_comments = comments)

@app.route("/addmessage", methods=['POST'])
def add_message():
    query= "INSERT into messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"

    data={
    "message": request.form['message'],
    "user_id": session['user_id'],
    }

    mysql.query_db(query, data)
    return redirect("/the_wall")

@app.route("/addcomment", methods=['POST'])
def addcomment():
    query= "INSERT into comments(message_id,user_id, comment, created_at, updated_at) VALUES(:message_id, :user_id, :comment, NOW(), NOW())"

    data ={
    "message_id": request.form['message_id'],
    "user_id" :session['user_id'],
    "comment" : request.form['comment']
    }

    mysql.query_db(query, data)
    return redirect("/the_wall")

@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")

app.run(debug=True)

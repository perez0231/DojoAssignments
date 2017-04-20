from flask import Flask, request, render_template, session, flash, redirect
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

import re
app = Flask(__name__)
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app,'the_wall')
app.secret_key= 'dmoney'
onlyLetters= re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', messages= flash)
@app.route('/register', methods= ['POST'])
def register():
    inputvalid= True ##flag

    data={
    'fname': request.form['fname'],
    'lname' : request.form['lname'],
    'email': request.form['email'],
    'password': request.form['password'],
    'cpassword': request.form['cpassword'],
    }

    if not onlyLetters.match(data['fname']):
        inputvalid= False
        flash('only letters in first name ')
    if len(data['fname']) < 2:
        inputvalid= False
        flash('first name is too short')
    if not onlyLetters.match(data['lname']):
        inputvalid= False
        flash('only letters in last name ')

    if not EMAIL_REGEX.match(data['email']):
        inputvalid= False
        flash('Not valid email')

    if not data['email']:
        inputvalid= False
        flash('must enter email')

    if len(data['password']) < 8:
        inputvalid= False
        flash('password not long enough')
    if not data['password']:
        inputvalid= False
        flash('MUST ENTER PASSWORD')

    if data['password'] != data['cpassword']:
        inputvalid= False
        flash('passwords dont match')

    if not inputvalid:
        return redirect ('/')

    else:
        pw_hash = bcrypt.generate_password_hash(data['password'])

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :pass, NOW(), NOW())"

        query_data ={
        'email': data['email'],
        'first': data ['fname'],
        'last': data ['lname'],
        'pass' : pw_hash,
        }


        userid=mysql.query_db(query, query_data)
        session['user_id']=userid
        return redirect ('/thewall')


@app.route('/login', methods=['POST'])
def login():
    query= "Select * from users where email= :email"

    data={
    'email': request.form['email']
    }
    userinsession=mysql.query_db(query, data)

    if not userinsession:
        flash('invalid email')
        print "not user"
        return redirect ('/')


    else:
        if bcrypt.check_password_hash(userinsession[0]['password'], request.form['password']):
            session['user']= userinsession[0]['id']
            print "elseif"
            return redirect('/thewall')
        else:
            flash('invalid credentials')
            "print creds"
            return redirect ('/')

    return redirect('/')

@app.route('/thewall', methods=["GET"])
def thewall():
    query="select message.id, message, from messages"
    # if 'user' not in session:
    #     return redirect ('/')
    query= "SELECT * from users where id = :id"

    data={
        "id": session['user_id']
    }
    loggeduser=  mysql.query_db(query, data)

    messagequery="SELECT messages.id, users.first_name, users.last_name, messages.message, messages.created_at from messages join users on users.id= messages.user_id"
    message_wall=mysql.query_db(messagequery)

    commentquery= "SELECT users.first_name, users.last_name, comments.message_id,  comments.comment, comments.created_at from users join comments on users.id = comments.user_id"

    comment=mysql.query_db(commentquery)

    return render_template('user.html', user=loggeduser[0], messages=message_wall, comment=comment)

@app.route('/post', methods=['POST'])
def post():
    query= "SELECT * from users where id = :id"

    data={
        "id": session['user_id']
    }
    postquery= "INSERT into `the_wall`.`messages`(`message`, created_at, updated_at,user_id) VALUES (:one, NOW(), NOW(), :two)"

    query_data={
    'one': request.form['message'],
    'two': session['user_id']
    }
    result=mysql.query_db(postquery, query_data)
    return redirect('/thewall')

@app.route('/messages/<message_id>/comments', methods=['POST'])
def comment(message_id):

    commentquery="INSERT into `comments`(`comment`, `created_at`, `updated_at`, user_id, message_id)VALUES(:one, NOW(), NOW(), :two, :three)"

    query_data={
    'one': request.form['comment'],
    'two': session['user_id'],
    'three': message_id
    }
    print commentquery
    mysql.query_db(commentquery, query_data)


    return redirect('/thewall')











app.run(debug=True)

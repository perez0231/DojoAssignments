from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key ='daniel'


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/submit', methods= ["POST"])
def create():
    if not EMAIL_REGEX.match(request.form['email']):
            flash('EMAIL IS NOT VALID!')
            return redirect('/')

    else:
        session['email']= request.form['email']
        emaildata = str(session['email'])

        query= "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"

        data = {
            'email': request.form['email']
            }

        mysql.query_db(query, data)

        emailtable = 'SELECT * FROM email'
        emailinfo = mysql.query_db(emailtable)
        flash('the email you entered' + emaildata +'this is valid ')

        return render_template('success.html', all_emailinfo = emailinfo)



app.run(debug=True)

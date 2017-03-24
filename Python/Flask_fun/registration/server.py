
from flask import Flask, render_template, redirect, request, session, flash

import re

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


app = Flask(__name__)
app.secret_key = 'secretpassword'


@app.route('/')
def index():
    print "*"*100
    print "I'm here"
    print "*"*100
    return render_template("index.html")


@app.route('/process', methods=['Post'])
def submit():
  validate_first()
  validate_last()
  validate_password()
  confirm_password()

  # email is less than 1 character
  if len(request.form['email']) < 1:
    flash("Email cannot be blank!")
    # return redirect('/')
  # email isn't in correct form
  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid email address.")
    # return redirect('/')
  # email is valid
  else:
    flash("Thanks for submitting your information!")
    return render_template("index.html")

# validate first name
def validate_first():
  if len(request.form['first_name']) < 1:
    flash("First name cannot be blank.")
    # return redirect('/')

# validate last name
def validate_last():
  if len(request.form['last_name']) < 1:
    flash("Last name cannot be blank.")
    # return redirect('/')

# validate password
def validate_password():
  if len(request.form['password']) < 9:
    flash("Password must be at least 8 characters.")
    # return redirect('/')

# confirm password
def confirm_password():
  if request.form['confirm_pwd'] != request.form['password']:
    flash("Passwords must match.")
    # return redirect('/')



app.run(debug=True)

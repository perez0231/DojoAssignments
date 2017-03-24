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

app.run(debug="True")

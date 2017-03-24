from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'mysecretkey'

import random

@app.route('/')
def index():
    if 'random' in session:
        pass
    else:
        session['random'] = random.randrange(1,100)

    print session['random']

    return render_template("numindex.html")

@app.route('/newpage', methods=["POST"])
def result():

    if  int(request.form['guess']) < session['random']:
        print "The random num is" + str(session['random'])
        print "Your guess is low"
        return render_template("numindex.html", low="Too low")

    elif int(request.form['guess']) > session['random']:
        print "Your guess is hi."
        return render_template("numindex.html", high="Too high")

    else:
        print "The random num is" + str(session['random'])
        print "You WON"

        session.pop('random')

    return render_template("win.html")

            # return render_template(numindex.html)
@app.route('/win', methods=['POST'])
def win():
    return redirect("/")


app.run(debug=True)

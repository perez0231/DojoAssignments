from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    if 'random' in session:
        pass
    else:
        session['random']= random.randrange(0,101)

    return render_template('index.html', random= session['random'])

@app.route('/guess', methods= ['POST'])
def guess():
    if int(request.form['guess']) < session['random']:
        message = "too low"
        print session['random']
        return render_template('index.html', message = message)

    if int(request.form['guess']) > session['random']:
        message = 'This guess is too high'
        return render_template('index.html', message= message)
    else:
        message = "was the number! Wanna play again???"
    return render_template('win.html',random=session['random'], message= message)


@app.route('/playagain', methods= ['POST'])
def tryagain():
    session.pop('random')

    return redirect ('/')




app.run(debug=True)

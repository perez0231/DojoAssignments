from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'mysecretkey'

#count += 1 on refresh
#count +=2 on button
#count reset on rest
@app.route('/')
def index():
    print session
    if "counter" in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    return render_template("counter.html") ##make sure server still running with Flask issues/errors

@app.route("/count", methods=["POST"])
def count():

    session['counter'] +=1

    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():

    session.clear()

    return redirect("/")
    #plus two to count

app.run(debug=True)

from flask import Flask, render_template, request, redirect

app = Flask (__name__)
app.secret_key ='tacos'

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/ninjas')
def ninjas ():

    displayAll = True

    return render_template("ninjas.html", displayAll=displayAll)


@app.route('/ninjas/<color>')
def getcColor(color):

        displayAll= False

        return render_template('ninjas.html', displayAll=displayAll, color =color)

app.run(debug=True)

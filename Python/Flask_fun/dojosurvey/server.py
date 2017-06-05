from flask import Flask, render_template, redirect, request

app= Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location= request.form['location']
    language=request.form['lang']
    comments= request.form['comments']
    print name

    return render_template("results.html", name=name, location=location, lang= language, comments= comments)



app.run(debug=True)

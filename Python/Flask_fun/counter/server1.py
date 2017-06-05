from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods =['POST'])
def users():
    if len(request.form['first']):
        return redirect('/')

    else:
        flash("success")



        return render_template("userform.html", name = name, favlocation = favlocation, comment= comment)
app.run(debug=True)

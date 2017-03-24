from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
        return render_template("index.html")


@app.route('/users', methods =['POST'])
def process():
    print "Got Post info"

    if len(request.form['name']) < 1 or \
    len(request.form['comment']) < 1:
        flash("Name/comment cannot be empty!")
         return redirect('/')

    if len(request.form['comment']) > 120:
        flash("Please make sure that Comment section is less than 120 characters.")


        return redirect('/')

    else:
        flash("success")


    name = request.form['name']
    favlocation = request.form['favlocation']
    language = request.form['language']
    comment = request.form['comment']



    print name
    print language
    print favlocation
    print comment

    return render_template("userform.html", name = name, favlocation = favlocation, comment= comment)
app.run(debug=True)

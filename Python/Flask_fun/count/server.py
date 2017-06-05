from flask import Flask, session, render_template, request, redirect

app=Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def index():
    if "count" in session:
        session['count'] += 1

    else:
        session['count']= 1

    return render_template('index.html', count= session['count'])
@app.route('/addtwo', methods=['POST'])
def addtwo():
    session['count'] +=1
    return redirect('/')
@app.route('/delete', methods=['POST'])
def delete():
    session.clear()
    return redirect('/')

app.run(debug=True)      # Run the app in debug mode.

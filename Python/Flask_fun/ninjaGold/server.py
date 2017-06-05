from flask import Flask, session, render_template, request, redirect
app= Flask(__name__)
app.secret_key= 'mysecretkey'
import random
from datetime import datetime

@app.route('/')
def index():

    if 'recap' in session:
        pass
    else:
        session['recap']= []

    if 'gold' in session:
        pass
    else:
        session['gold']= 0
    return render_template('index.html', gold= session['gold'], recap= ['recap'])



#
@app.route('/process', methods = ['POST'])
def process():
    if request.form['building'] == 'farm':
        timestamp=datetime.now()
        session['randomfarm'] = random.randrange(10, 21)
        farmgold= "Earned" +" "+ str(session['randomfarm'])+ " from the farm"+ "("+str(timestamp)+")"
        print farmgold
        session['recap'].append(farmgold)
        print session['recap']
    

        session['gold']+= session['randomfarm']
#     #
    elif request.form['building'] == 'cave':
        session['randomcave'] = random.randrange(5, 10)
        cavegold= "Earned" +" "+ str(session['randomcave'])+ " from the cave"
        print cavegold
        session['recap'].append(cavegold)
        print session['recap']
        session['gold']+= session['randomcave']

    #
    # elif request.form['building'] == 'house':
    #     session['gold'] += random.randint(2, 5)
    elif request.form['building'] == 'house':
        session['randomhouse'] = random.randrange(2, 5)
        housegold= "Earned" +" "+ str(session['randomhouse'])+ " from the house"
        print housegold
        session['recap'].append(housegold)
        print session['recap']
        session['gold']+= session['randomhouse']

    elif request.form['building'] == 'casino':
        session['randomcasino'] = random.randrange(-50, 50)
        casinogold= "Earned" +" "+ str(session['randomcasino'])+ " from the casino"
        print casinogold
        session['recap'].append(casinogold)
        print session['recap']
        session['gold']+= session['randomcasino']
    #
    #
    # else:
    #     session['gold'] += random.randint(-50, 50)

    return redirect('/')


@app.route('/reset', methods= ['POST'])
def reset():
    session.clear()
    print "Your Session has been cleared!"
    return redirect("/")



app.run(debug=True)      # Run the app in debug mode.

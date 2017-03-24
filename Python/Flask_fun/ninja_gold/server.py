from flask import Flask, render_template, request, redirect, session

import random
app=Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    if "num" in session:
        pass
    else:
        session['num']= []

    if 'gold' in session:
        pass

    else:
        session['gold'] = 0


    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():

    if request.form['Building'] == "farm":
        print "This came from farm."
        session['random_num']= random.randint(10,20)
        farm_gold= "You got" + str(session['random_num']) + "gold coins"
        print farm_gold
        session['num'].append(farm_gold)
        print session['num']

        # adds to gold
        session['gold'] += session['random_num']

    #
    elif request.form['Building'] == "cave":
        session['random_num']=random.randint(5,10)
        cave_gold= "You got" + str(session['random_num']) + "gold coins"
        print cave_gold
        session['num'].append(cave_gold)
        print session ['num']

        session['gold'] += session['random_num']

    #
    elif request.form['Building'] =="house":
        session['random_num']=random.randint(2,5)
        house_gold= "You got" + str(session['random_num']) + "gold coins"
        print house_gold
        session['num'].append(house_gold)
        print session['num']

        session['gold'] += session['random_num']

        print house_gold

    elif request.form['Building'] == "casino":
            session['random_num'] = random.randint(-50, 50)
            casino_gold = "You got " + str(session['random_num']) + " gold coins from the casino."
            print casino_gold
            session['num'].append(casino_gold)
            print session['num']

            # adds to total gold
            session['gold'] += session['random_num']
            print session['gold']
        # else:
        #     session['random_num'] = random.randint(0, 50)
        #     casino_s = "You lost " + str(session['random_num']) + " gold coins from the casino."
        #     print casino_s
        #     session['num'].append(casino_gold)
        #     print session['num']
        #
        #     # adds to total gold
        #     session['gold'] -= session['random_num']
        #     print session['gold']

    #     session['random_num']=random.randint(0,50)
    #     casino_gold= "You got" + str(session['num']) + "gold coins"
    #     print casino_gold
    #     session['num'].append(casino_gold)
    #     print session['num']
    #
    #     session['gold'] += session['random_num']



    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    print "Your Session has been cleared!"
    return redirect("/")


#
# @app.route('/reset')
# def index():
app.run(debug=True) # run our server

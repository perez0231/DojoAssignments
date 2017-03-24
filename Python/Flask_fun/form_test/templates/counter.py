from flask import Flask, session, render_template, url_for, request, redirect

app = Flask(__name__)


app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/')
def index():
    sumSessionCounter()
    return render_template('counter.html')

# from flask import Flask, render_template, request, redirect, session
#
# app = Flask(__name__)
# app.secret_key = 'mysecretkey' # you need to set a secret key for security purposes
#
# @app.route('/', methods=['POST'])
# def index():
#     count= 0
#         count +=1
# return render_template("counter.html")
#
# #
# #
# #    print "Got Post Info"
# #    # here we add two properties to session to store the name and email
# #    session['name'] = request.form['name']
# #    session['email'] = request.form['email']
# #    return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!
# #
# #
# #
# # @app.route('/')
# # def index():
# #
# # @app.route('/users', methods=['POST'])
# # def create_user():
# #    print "Got Post Info"
# #    # notice how the key we are using to access the info corresponds with the names
# #    # of the inputs from our html form
# #    name = request.form['name']
# #    email = request.form['email']
# #    return redirect('/') # redirects back to the '/' route
# # @app.route('/show')
# # def show_user():
# #   return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')
# # app.run(debug=True)

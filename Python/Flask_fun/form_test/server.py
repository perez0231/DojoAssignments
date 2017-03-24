from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=['POST'])
def process():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms

   name = request.form['name']
   favlocation = request.form['favlocation']
   language = request.form['language']
   comment=  request.form['comment']
   # # redirects back to the '/' route

   print name
   print language
   print favlocation
   print comment

   return render_template("userinfo.html", name= name, favlocation=favlocation,language=language, comment=comment)
app.run(debug=True) # run our server

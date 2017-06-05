from flask import Flask, request, redirect, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods= ['POST'])
def process():
    print request.form['name']
    return redirect("/")
app.run(debug=True)      # Run the app in debug mode.

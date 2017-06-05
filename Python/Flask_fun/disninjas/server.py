from flask import Flask, redirect, render_template

app = Flask(__name__)
app.secret_key = 'secrets'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    all_ninjas= True
    return render_template('ninjas.html', all_ninjas= all_ninjas)
@app.route('/ninjas/<color>')
def newninjas(color):
    all_ninjas=False
    return render_template('ninjas.html', all_ninjas=all_ninjas, color=color)



app.run(debug=True)

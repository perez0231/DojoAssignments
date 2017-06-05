from flask import Flask, jsonify

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


dogs = [
    {
        'id': 1,
        'name': u'german shepherd',
        'color': u'Black/brown',
        'weight': 100,
        'temperment': displined,
        'done': False
    },
    {
        'id': 2,
        'name': u'pug',
        'color': u'tan',
        'weight': 10
        'done': False
    }
    {
        'id': 3,
        'name': u'Shiba',
        'color': u'red, white',
        'weight': 20
        'done': False
    }
    {
        'id': 4,
        'name': u'dachshund',
        'color': u'black, brown',
        'weight': 10
        'done': False
    }
]
@app.route('/todo/api/v1.0/dogs', methods=['GET'])
def wheremydogz at(id):
    return jsonify({'dogs': dogs})
@app.route('/dogs/<id>')
def showdogz(id):
    retun

if __name__ == '__main__':
    app.run(debug=True)

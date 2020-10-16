#flash framework - which is micro framework

from flask import Flask
from flask import render_template ,redirect ,url_for ,jsonify

global value

# only a sample file 
# Main file is : login.py
# Genral introduction to Python  flask library
file = []
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for("login"))

@app.route('/main')
def login():
    return "this is private project"

@app.route('/innovatorved/<string:n>/<string:m>/')
def add(n,m):
    global value
    value = {"Email":n,"msg":m}
    file.append(value)
    return "Done"

@app.route('/data/')
def data01():
    return jsonify(file)

if __name__ == '__main__':
    app.run()

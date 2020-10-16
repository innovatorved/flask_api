#flash framework - which is micro framework

from flask import Flask
from flask import render_template ,redirect ,url_for ,jsonify

str n = 0
# only a sample file 
# Main file is : login.py
# Genral introduction to Python  flask library
file = [
		{
			'id':0,
			"value":1
		},
		{
			'id':1,
			"value":5
		}


]
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for("login"))

@app.route('/login')
def login():
    return "this is output"

@app.route('/innovatorved/<str:n>')
def add():
    return "Done"

@app.route('/data')
def data01():
    return jsonify(file)

if __name__ == '__main__':
    app.run()

from flask import Flask , jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/innovatorved/<string:n>')
def set_api(n):
	return n

if __name__ == '__main__':
    app.run()

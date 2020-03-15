from flask import Flask

#create a new Flask app instance
app = Flask(__name__)

#create Flask Routes
@app.route('/')
def hello_world():
	return 'Hello world'

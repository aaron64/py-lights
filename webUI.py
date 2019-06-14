from flask import Flask
from flask import render_template

import threading

data = 'foo'
webUI = Flask(__name__)

@webUI.route("/")
def main():
	return render_template('index.html')

def initialize_ui(app):
	threading.Thread(target=webUI.run(host='0.0.0.0', port=5000)).start()

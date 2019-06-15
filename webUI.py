from flask import Flask
from flask import render_template

import threading

webUI = Flask(__name__)

@webUI.route("/")
def main():
	return render_template('index.html', data=data)

def initialize_ui(d):
	global data
	data = d
	threading.Thread(target=webUI.run(host='0.0.0.0', port=5000)).start()

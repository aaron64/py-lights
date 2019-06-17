from flask import Flask
from flask import render_template, request

import threading

webUI = Flask(__name__)

@webUI.route("/")
def main():
	return render_template('index.html', data=data)

@webUI.route('/', methods=['POST'])
def my_form_post():
    print(request.form)
    return render_template('index.html', data=data)

def initialize_ui(d):
	global data
	data = d
	threading.Thread(target=webUI.run(debug=False, host='0.0.0.0', port=5000)).start()

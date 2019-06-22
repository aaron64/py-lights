from flask import Flask
from flask import render_template, request

import threading

webUI = Flask(__name__)

@webUI.route("/")
def main():
	return render_template('index.html', data=data)

@webUI.route('/', methods=['POST'])
def post():
	print(request)
	print(request.form.items())

	return render_template('index.html', data=data)

def initialize_ui(d):
	global data
	data = d
	t = threading.Thread(target=webUI.run, kwargs={"debug":False, "host":'0.0.0.0', "port":5000})
	t.start()

if __name__ == "__main__":
	pass

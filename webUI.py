from flask import Flask
from flask import render_template, request

import threading

webUI = Flask(__name__)

@webUI.route("/")
def main():
	return render_template('index.html', data=data)

@webUI.route('/', methods=['POST'])
def post():
	_id = request.form.get("id").decode("utf8")

	data.inputs[_id].type = request.form["type"].decode("utf8")
	data.inputs[_id].key = int(request.form["key"].decode("utf8"))
	data.inputs[_id].setting = request.form["setting"].decode("utf8")
	data.inputs[_id].inverse = True if request.form["inverse"].decode("utf8") == "True" else False

	return render_template('index.html', data=data)

def initialize_ui(d):
	global data
	data = d
	t = threading.Thread(target=webUI.run, kwargs={"debug":False, "host":'0.0.0.0', "port":8085})
	t.daemon = True
	t.start()

if __name__ == "__main__":
	pass

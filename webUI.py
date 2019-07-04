from flask import Flask
from flask import render_template, request, jsonify

import threading

webUI = Flask(__name__)

@webUI.route("/")
def main():
	return render_template('index.html', data=data)

@webUI.route("/update_input", methods=["POST"])
def update_input():
	print(request)
	print(request.json)
	print(request.json[0])
	print(request.json[0]["_id"])
	return jsonify("hi")



def initialize_ui(d):
	global data
	data = d
	t = threading.Thread(target=webUI.run, kwargs={"debug":False, "host":'0.0.0.0', "port":8085})
	t.daemon = True
	t.start()

if __name__ == "__main__":
	pass

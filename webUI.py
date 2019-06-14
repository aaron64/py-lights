from flask import Flask                                                         
import threading

data = 'foo'
webUI = Flask(__name__)

@webUI.route("/")
def main():
	return data

def initialize_ui(app):
	threading.Thread(target=webUI.run(host='0.0.0.0', port=5000)).start()

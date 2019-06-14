from flask import Flask                                                         
import threading

data = 'foo'

@app.route("/")
def main():
	return data

def initialize_ui():
	app = Flask(__name__)

if __name__ == "__main__":
	threading.Thread(target=app.run).start()
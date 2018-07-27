from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	print('Hello there!')
	return 'Hello, World! We here'

@app.route('/taskext', methods=['POST'])
def submitted_form():
    print(request)
    # TODO: something with this
    return 'Post request, thank you!'
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/action')
def hello_world():
    action = request.args.get('action')
    return (f"{action}")
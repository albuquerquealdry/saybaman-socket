from flask import Flask
from flask import request
import os
app = Flask(__name__)
@app.route('/action')
def hello_world():
    action = request.args.get('action')
    return (f"{action}")

def main():
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
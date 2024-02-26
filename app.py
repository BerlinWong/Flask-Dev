from flask import Flask
from flask_cors import CORS

from utils.response.json_flask import JsonFlask

# app = Flask(__name__)
app = JsonFlask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

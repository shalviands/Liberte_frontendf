from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
test=0

@app.route('/hello')
def say_hello_world():
    return {'result': "IDLE"}
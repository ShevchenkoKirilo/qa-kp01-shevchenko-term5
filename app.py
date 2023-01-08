from binary import Binary
from buffer import Buffer
from folder import Folder
from log import Log

from flask import Flask, request, jsonify
app = Flask(__name__)
deleted = []
root = Folder('root', 0, None) 


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/binary', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def binary():
    return


@app.route('/buffer', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def buffer():
    return


@app.route('/folder', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def folder():
    return


@app.route('/log', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def log():
    return




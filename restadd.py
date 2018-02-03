#!flask/bin/python

import redis
from flask import Flask, jsonify, abort, request

redis_server = redis.Redis()

app = Flask(__name__)


@app.route('/sample/api/add', methods=['POST'])
def create_key():
    if not request.json or not 'key' in request.json or not 'value' in request.json:
        abort(400)
    kv = {
        'key': request.json['key'],
        'value': request.json.get('value')
    }
    redis_server.set(request.json['key'], request.json['value'])
    return jsonify({'kv': kv}), 201

@app.route('/sample/api/read/<key>', methods=['GET'])
def get_key(key):
    if len(key) == 0:
        abort(404)
    kv = {
        'key': key,
        'value': redis_server.get(key)
    }
    return jsonify({'kv': kv})



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

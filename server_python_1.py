from flask import Flask,request
from flask_cors import CORS, cross_origin
import json
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/md5')
@cross_origin()
def md5_info():
    return '0'

@app.route('/signUpUser', methods=['POST'])
@cross_origin()
def signUpUser():
    k = request.form['key']
    b = 0
    if k == 'shitou':
        b = 1
    if k == 'jianzi':
        b = 1
    if k == 'bu':
        b = 1
    if b == 1:
        c = random.randint(1,3)
        if c == 1:
            d = 'shitou'
        if c == 2:
            d = 'jianzi'
        if c == 3:
            d = 'bu'
        if k == 'shitou':
            if d == 'shitou':
                r = 'shitou = shitou'
            if d == 'jianzi':
                r = 'shitou > jianzi'
            if d == 'bu':
                r = 'shitou < bu'
        if k == 'jianzi':
            if d == 'shitou':
                r = 'jianzi < shitou'
            if d == 'jianzi':
                r = 'jianzi = jianzi'
            if d == 'bu':
                r = 'jianzi > bu'
        if k == 'bu':
            if d == 'shitou':
                r = 'bu > shitou'
            if d == 'jianzi':
                r = 'bu < jianzi'
            if d == 'bu':
                r = 'bu = bu'
    return r

app.run(host='0.0.0.0')
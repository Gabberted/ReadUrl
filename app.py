#!/usr/bin/env python

from flask import Flask
from flask import request
import readUrl as rdu

print("Starting")
app = Flask(__name__)
print(f"app {app}")

@app.route('/headers')
def hello():
    print("hello")
    ua = request.headers.get('user-agent')
    ka = request.headers.get('connection')
    print(f"returning {ua}   {ka}")
    return f'User agent: {ua}; Connection: {ka}'

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/webopen'/<string>)
def webopen(url):
    return rdu.webOpen(url)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4452)

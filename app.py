#!/usr/bin/env python

from flask import Flask
from flask import request


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
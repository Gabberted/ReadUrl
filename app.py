#!/usr/bin/env python

from flask import Flask
from flask import request
import readUrl as rdu
import json

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
    return "Not implemented"

@app.route('/testdb')
def testdb():
    try:
        cursor, conn = rdu.Connect()        
        strQ="insert into Tags(Tag)values('TEST')"
        cursor.execute(strQ)
        conn.commit()
        return "Data stored !\n"
    except Exception as e:
        return "Connection failed!"
    
@app.route('/emptyTable/<strTableName>')
def emptyTable(strTableName):
    try:
        cursor, conn = rdu.Connect()        
        strQ="delete from " + strTableName
        cursor.execute(strQ)
        conn.commit()
        return "Table cleared !\n"
    except Exception as e:
        return "Connection failed!"



@app.route('/showall/<tablename>')
def showall(tablename):
    if len(tablename)>0:
        strQ="Select * from " + tablename 
        cursor, conn =rdu.Connect()
        cursor.execute(strQ)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return json.dumps(rows)
    else:
        return "Please provide a tablename"


@app.route('/webopen/<url>')
def webopen(url):
    return rdu.webOpen(url)

@app.route('/words/<url>')
def words(url):
    return rdu.get_all_seperate_words(url)

@app.route('/collectHTMLTags/<url>/<store>')
@app.route('/collectHTMLTags/<url>')
def collectHTMLTags(url, store=""):
    if store!="":
        strTags = rdu.collectHTMLTags(url)
        print(f"strTags: {strTags}")
        rdu.storeHTMLTags(strTags)
        return "STORED !"        
    else:
        return rdu.collectHTMLTags(url)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4452)

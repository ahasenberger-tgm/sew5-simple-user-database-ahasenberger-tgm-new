import sqlite3 as lite
import sys
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

con = lite.connect('Students')

@app.route('/')
def hello_world():
   return "Hello World"

@app.route("/userget/")
def getMember():
   with lite.connect('Students') as con:
      cur = con.cursor()
      users = cur.execute("SELECT * from students")
      users_json = json.dumps(users)

   return users_json

@app.route('/useradd/')
def addMember():
   #with con:
   with lite.connect('Students') as con:
      username = request.args['username']
      email = request.args['email']
      cur = con.cursor()
      cur.execute("INSERT INTO students (username, email) VALUES (?, ?)", (username, email))
      con.commit()
   #cur = con.cursor()
   #cur.execute("INSERT INTO students (username, email) VALUES(usernameinput, emailinput)")

   return "user"

@app.route("/user/update/<string:nameupdate>/")
def updateMember(nameupdate):
   return nameupdate

@app.route("/user/delete/<string:namedel>/")
def delMember(namedel):
   return namedel

if __name__ == '__main__':
   app.run()
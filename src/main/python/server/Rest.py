import sqlite3 as lite
import sys
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
con = lite.connect('Students')

@app.route('/')
def hello_world():
   return "Hello World"

@app.route("/userget/")
def getMember():
   with lite.connect('Students') as con:
      cur = con.cursor()
      cur.execute("SELECT * from students")
      users = cur.fetchall()
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
def updateMember():
    """with lite.connect('Students') as con:
        email = request.args['email']
        username = request.args['username']
        cur = con.cursor()
        if (username == ""):
            cur.execute("UPDATE students SET email=(?) WHERE userid=(?)", (email, userid))
        if (email == ""):
            cur.execute("UPDATE students SET username=(?) WHERE userid=(?)", (username, userid))"""

    return "X"

@app.route("/userdelete/")
def delMember():
    with lite.connect('Students') as con:
        email = request.args['email']
        username = request.args['username']
        userid = request.args['userid']
        cur = con.cursor()

        if(username == "" and userid == ""):
            cur.execute("SELECT userid FROM students WHERE email=(?)", (email))
            userid = cur.fetchall()

        if (email == "" and userid == ""):
            cur.execute("SELECT userid FROM students WHERE username=(?)", (username))
            userid = cur.fetchall()

        cur.execute("DELETE FROM students WHERE user_id=(?)", (userid))
    return "Success"

if __name__ == '__main__':
   app.run()
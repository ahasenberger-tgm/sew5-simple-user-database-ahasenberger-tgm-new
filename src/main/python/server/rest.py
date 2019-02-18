import sqlite3 as lite
import sys
import json
import validators
from flask import Flask, request, jsonify, abort
from functools import wraps
from flask_httpauth import HTTPDigestAuth
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
con = lite.connect('Students')

@app.route('/')
def hello_world():
   return "Hello World"

@app.route("/userget")
def getMember():
   with lite.connect('Students') as con:
      cur = con.cursor()
      cur.execute("SELECT * from students")
      users = cur.fetchall()
      userOut = []
      for i in range(len(users)):
          user = {"username": users[i][0], "email": users[i][1], "id": users[i][2], "picture": ""}
          userOut.append(user)

      return json.dumps(userOut)


@app.route('/useradd')
def addMember():
   #with con:
   with lite.connect('Students') as con:
      username = request.args['username']
      email = request.args['email']
      usernametry = validators.length(username,min=5,max=80)
      emailtry = validators.email(email)
      if (usernametry == True and emailtry == True):
          cur = con.cursor()
          cur.execute("INSERT INTO students (username, email) VALUES (?, ?)", (username, email))
          con.commit()
      else:
          abort(422)
   #cur = con.cursor()
   #cur.execute("INSERT INTO students (username, email) VALUES(usernameinput, emailinput)")

   return "user"

@app.route("/userupdate")
def updateMember():
    with lite.connect('Students') as con:
        userid = request.args['userid']
        email = request.args['email']
        username = request.args['username']
        usernametry = validators.length(username,min=5,max=80)
        emailtry = validators.email(email)
        if(usernametry == True and emailtry == True):
            cur = con.cursor()
            if (username == ""):
                cur.execute("UPDATE students SET email=(?) WHERE userid=(?)", (email, userid))
                con.commit()
            if (email == ""):
                cur.execute("UPDATE students SET username=(?) WHERE userid=(?)", (username, userid))
                con.commit()
        else:
            abort(422)

    return "Success"

@app.route("/userdelete")
def delMember():
    with lite.connect('Students') as con:
        email = request.args['email']
        username = request.args['username']
        userid = request.args['userid']
        cur = con.cursor()

        """if(username == "" and userid == ""):
            cur.execute("SELECT userid FROM students WHERE email=(?)", (email))
            userid = cur.fetchall()

        if (email == "" and userid == ""):
            cur.execute("SELECT userid FROM students WHERE username=(?)", (username))
            userid = cur.fetchall()
        """
        cur.execute("DELETE FROM students WHERE userid = (?)", (userid))
        cur.fetchall()
    return "Success"

if __name__ == '__main__':
   app.run()
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route("/user/get/<string:name>/")
def getMember(name):
   return "User hinzufügen %s" (name)

@app.route("/user/add/<string:name>/")
def addMember(name):
   return "Members"

@app.route("/user/update/<string:name>/")
def updateMember(name):
   return name

@app.route("/user/delete/<string:name>/")
def delMember(name):
   return name

if __name__ == '__main__':
   app.run()
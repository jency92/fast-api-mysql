from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask,request
import os
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = os.getenv("root")
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv("admin")
app.config['MYSQL_DATABASE_DB'] = os.getenv("db_name")
app.config['MYSQL_DATABASE_HOST'] = os.getenv("db_host")
mysql.init_app(app)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask App!"

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
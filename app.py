from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
import yaml # type: ignore
app = Flask(__name__)

db = yaml.safe_load(open('db.yaml'))
app.config['MySQL_HOST'] = db['mysql_host']
app.config['MySQL_USER'] = db['mysql_user']
app.config['MySQL_PASSWORD'] = db['mysql_password']
app.config['MySQL_DB'] = db['mysql_db']

mysql = MySQL(app)


@app.route("/", methods = ['GET', 'POST'])
def index():
  if request.method == 'POST':
   userDetails = request.form 
   name = userDetails['name']
   email = userDetails['email']
   cur = mysql.connect.cursor()
   cur.execuute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
   mysql.connector.connect()
   cur.close()
   return ('success')
  return render_template('index.html')
@app.route('/users')
def users():
 cur = mysql.connector.cursor()
 resultValue = cur.execute("SELECT * FROM users")
 if resultValue >0:
  userDetails = cur.fetchall()
  return render_template('users.html',userDetails=userDetails)
  
if __name__ == "__main__":
 app.run(debug = True)
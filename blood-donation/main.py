from flask import  Flask,render_template,request,url_for,redirect,flash,session
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from datetime import *
import json
import tkinter as tk
from tkinter import messagebox
import mail_alert
import mysql.connector as sql

with open("keys.json", "r") as secret_keys:
 data = json.load(secret_keys)

app=Flask(__name__)
app.secret_key='bloodbank'
app.permanent_session_lifetime=timedelta(minutes=5)
mysql=MySQL(app)

app.config['SQLALCHEMY_DATABASE_URI'] = data['database_url']
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)

class Join(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    userename = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    location= db.Column(db.String(255), nullable=True)
    blood_group= db.Column(db.String(5), nullable=False)
    last_donation_date = db.Column(db.Date, nullable=True)
    email = db.Column(db.String(255), nullable=False)
    phone_number= db.Column(db.String(15), nullable=True)
    reg_date= db.Column(db.Date, nullable=True)

#basic route to index page
@app.route('/')
def index():
 return render_template('index.html')

@app.route('/home')
def home():
 return render_template('index.html')


@app.route("/registration", methods = ['GET', 'POST'])
def join():
    if request.method == 'POST':
        obj=sql.connect(host="localhost", user="root",passwd="root", database="blooddonor")
        cursor=obj.cursor()
        user_id = request.form.get('user_id')
        name = request.form.get('name')
        username = request.form.get('username')
        password_hash = request.form.get('password_hash')
        location = request.form.get('location')
        blood_group= request.form.get('blood_group')
        last_donation_date=request.form.get('last_donation_date')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        qs="insert into donors (name, username, password_hash, location, blood_group, last_donation_date, email, phone_number) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(qs, (name, username, password_hash, location, blood_group, last_donation_date, email, phone_number))
        obj.commit()
        obj.close()
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Information", "Registerd succesfully")
        root.mainloop()
        mail_alert.thanks_donors(name,email)
        return render_template('registration.html')

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["username"]
		session["user"] = user
		return redirect(url_for("index"))
	else:
		if "user" in session:
			flash('Already logged in')
			return redirect(url_for("index"))
		return render_template("login.html")

@app.route('/signup')
def signup():
 return render_template('registration.html')

@app.route('/schedule')
def schedule():
   return render_template('schedule.html')

@app.route("/registration")
def registration():
    return render_template('registration.html')

@app.route('/certificate')
def certificate():
    return render_template('certificate.html')

if __name__=='__main__':
  app.run(debug=True)



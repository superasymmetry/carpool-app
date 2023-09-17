from flask import Blueprint, render_template, request, redirect, session, url_for
from back import store_login_data, validate_credentials, store_date
import sqlite3
import os

views = Blueprint(__name__, "views")
# PICTURE_FOLDER = os.path.join('static', 'photos')
# views.config['UPLOAD_FOLDER'] = PICTURE_FOLDER

@views.route("/")
def home():
  # img = os.path.join(views.config['UPLOAD_FOLDER'], 'homeimg.jpeg')
  return render_template("index.html")

@views.route("/profile/<username>")
def profile(username):
  return render_template("index.html", name=username)

@views.route("/user")
def user():
  if "user" in session:
    user = session["user"]
    return f"<h1>{user}</h1>"
  else:
    return redirect(url_for("views.signin"))

@views.route('/login', methods = ['GET', 'POST'])
def login():
  if request.method == "POST":
    user = request.form["nm"]
    psword = request.form["psw"]
    fname = request.form["fname"]
    lname = request.form["lname"]
    tel = request.form["tel"]
    eml = request.form["eml"]
    res = request.form["res"]
    store_login_data(user, psword, fname, lname, tel, eml, res)
   
    return "<h1>You have successfully signed up. Return to the login page to re-login. </h1>"
    # return redirect(url_for("user", usr=user))
  else:
    return render_template("login.html")

@views.route('/signin', methods = ['GET', 'POST'])
def signin():
    if request.method == "POST":
        user = request.form["nm"]
        psword = request.form["psw"]
        if validate_credentials(user, psword):
          session["user"] = user
          return redirect(url_for("views.dashboard"))
        else:
          
          return redirect(url_for("views.signin"))
    else:
        if "user" in session:
          return redirect(url_for("views.dashboard"))
        return render_template("signin.html")
        
    
# Dashboard nav bar -------------------------------------------------------------------------
    
# dashboard
# @views.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     #here we are checking whether the user is logged in or not
#     if 'user' in session:
#       user = session["user"]
#       if request.method=="GET":
#         date = request.form["dat"]
#         print("passed")
#         store_date(date)
#       else:
#         return render_template("dashboard.html", user=user)

#     else:
#       return '<h1>You are not logged in.</h1>'

@views.route('/dashboard', methods=['GET','POST'])
def dashboard():
  if 'user' in session:
    user = session["user"]
    if request.method=="POST":
      date = request.form.getlist('d')
      sum = 0
      for i, day in enumerate(date):
        if day!=None:
          sum += 2**i
      store_date(sum, user)
    else:
      return render_template("dashboard.html", user=user)
  else:
    return "<h1>You are not logged in.</h1>"
    
@views.route('/my_institution')
def my_institution():
   if 'user' in session:
     conn = sqlite3.connect("database.db")
     c = conn.cursor()
     c.execute("SELECT * FROM database")
     records = c.fetchall()
     conn.close()
     display = []
     for i, row in enumerate(records):
      display.append([])
      for j, x in enumerate(row):
        if j==1 or j==7:
          pass
        else:
          print(i,j, row)
          display[i].append(row[j])
        
          print(display)
     return render_template("institution.html", people=display)
   else:
     return '<h1>You are not logged in.</h1>'

# logout
@views.route("/logout")
def logout():
  session.pop("user", None)
  return redirect(url_for("views.home"))

@views.route("/editProfile")
def editProfile():
  if 'user' in session:
    if request.method == "POST":
      nm = request.form["nam"]
      tel = request.form["tel"]
      eml = request.form["eml"]
      res = request.form["res"]

      return redirect(url_for("views.editProfile"))
    else:
      return render_template("profile.html")
  else:
    return "<h1>You are not logged in.</h1>"

@views.route("/settings")
def settings():
   return '<h1>The settings are in the profile</h1>'
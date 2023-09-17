from flask import Flask, redirect, url_for, render_template, request, session
from views import views
import os
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "'88;+iR%=P'6owr"
app.register_blueprint(views, url_prefix="/")
# PICTURE_FOLDER = os.path.join('static', 'photos')
# app.config['UPLOAD_FOLDER'] = PICTURE_FOLDER

# app.config['SQLALCHEMY_DATABASE URI'] = 'sqlite:///db.sqlite3'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# class User(db.Model):
#   username = db.Column(db.String, primary_keys=True)
#   fname = db.Column(db.String(50))
#   lname = db.Column(db.String(50))
#   telephone = db.Column(db.String(50))
#   email = db.Column(db.String(100))
#   residence = db.Column(db.String(100))
#   days = db.Column(db.Integer)



# @app.route("/<name>")
# def user(name):
#     return f"Hello{name}!"

# @app.route("/admin/")
# def admin():
#    if a:
#     return redirect(url_for("user",name="Admin!"))

if __name__=="__main__":
  app.run(debug=True)

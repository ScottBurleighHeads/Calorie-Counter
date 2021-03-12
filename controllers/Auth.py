from models.user import User
from flask import Blueprint,json, render_template,request, jsonify, abort, redirect, url_for
from schemas.User_schema import user_schema, users_schema 
from main import db
from main import bcrypt
from flask_login import login_user, current_user, logout_user
from datetime import timedelta
from flask_jwt_extended import create_access_token

auth = Blueprint("auth",__name__,url_prefix="/login")

@auth.route("/",methods=["GET"])
def login():
    return render_template("login.html")
# There are login and log out test clients
@auth.route("/authorise",methods=["POST"])
def login_post():
    
    username=request.form.get("username")
    password=request.form.get('password')
    user = User.query.filter_by(username=username).first()
    
    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort(401, description="Incorrect username or password")
    login_user(user)

    return redirect(url_for("home.home_page"))
   

@auth.route("/register",methods=["GET","POST"])
def display_register():
    return render_template("register.html")

@auth.route("/post_register", methods=["POST"])
def auth_register():
    new_user = User()
    new_user.username=request.form.get("username")
    new_user.password=bcrypt.generate_password_hash("request.form.get('password')").decode("utf-8")
    user = User.query.filter_by(username=new_user.username).first()
    if user:
        return abort(401, description="Username is already registered")
    new_user.email=request.form.get("email")
    new_user.first_name=request.form.get("first_name")
    new_user.last_name=request.form.get("last_name")
    new_user.phone=request.form.get("phone")
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home.home_page'))
    
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.home_page'))

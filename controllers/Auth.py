from models.user import User
from flask import Blueprint,json, render_template,request, jsonify, abort
from schemas.User_schema import user_schema, users_schema 
from main import db
from main import bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token

auth = Blueprint("auth",__name__,url_prefix="/login")

# There are login and log out test clients
@auth.route("/",methods=["POST"])
def login():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(email=user_fields["email"]).first()
    
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and password")
    
    expiry = timedelta(days=1) # Expires after one day
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    return jsonify({"token": access_token})

@auth.route("/signup", methods=["GET"])
def signup():
    return render_template("sign_up.html")
    

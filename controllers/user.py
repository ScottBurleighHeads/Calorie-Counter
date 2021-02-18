from models.user import User 
from schemas.User_schema import user_schema, users_schema 
from main import db
from flask import Blueprint,jsonify,request,json,redirect
user = Blueprint("user",__name__,url_prefix="/user")


@user.route("/create_user",methods=["POST"])
def create_user():
    user_fields = user_schema.load(request.json)
    new_user = User()
    new_user.username = user_fields["username"]
    new_user.password = user_fields["password"]
    new_user.email = user_fields["email"]
    new_user.first_name = user_fields["first_name"]
    new_user.last_name = user_fields["last_name"]
    new_user.phone = user_fields["phone"]
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user))


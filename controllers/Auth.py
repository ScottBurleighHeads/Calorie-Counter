from flask import Blueprint,json, render_template,request
import requests
auth = Blueprint("auth",__name__,url_prefix="/login")

# There are login and log out test clients
@auth.route("/",methods=["GET"])
def login():
    return "Hello"


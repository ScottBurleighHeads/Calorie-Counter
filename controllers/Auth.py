from flask import Blueprint,json, render_template,request
import requests
auth = Blueprint("auth",__name__,url_prefix="/login")

@auth.route("/",methods=["GET"])
def login():
    return "Hello"

@auth.route("/create_user")
def create_user():
    pass
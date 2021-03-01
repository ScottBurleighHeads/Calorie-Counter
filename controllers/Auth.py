from flask import Blueprint,json, render_template,request
import requests
auth = Blueprint("auth",__name__,url_prefix="login")

@auth.route("/",method=["POST"])
def login():
    r
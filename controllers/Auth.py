from flask import Blueprint,json, render_template,request
import requests
auth = Blueprint("auth",__name__)

@auth.route("")
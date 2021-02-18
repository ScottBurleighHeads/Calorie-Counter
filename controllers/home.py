from flask import Blueprint,render_template
home = Blueprint("home",__name__,url_prefix="/home")

@home.route("/")
def home_page():
    return render_template("home.html")
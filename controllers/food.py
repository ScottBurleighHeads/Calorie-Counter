from models.calorie_count import Nutrient_DB
from flask import Blueprint , json, render_template, request 
import requests
import os
from flask_login import login_user, current_user, logout_user
food = Blueprint("food",__name__,url_prefix="/food")

@food.route("/")
def food_home():
    return render_template("Calorie_counter.html")

@food.route("/search", methods=["POST"])
def food_search():

    APP_ID=os.environ.get("APP_ID")
    YOUR_APP_KEY=os.environ.get("YOUR_APP_KEY")
    result = request.form["search"]
    response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?ingr={result}&app_id={APP_ID}&app_key={YOUR_APP_KEY}")
    dict_response=json.loads(response.text) 
    values=dict_response["hints"]
    length = len(dict_response["hints"])
    
    return render_template("Calorie_counter.html", values=values, length=length)

@food.route("/store_calories", methods=["POST"])
def food_database():
    
    import datetime
    current_date = datetime.datetime.now()
    date_holder = current_date.date()
    calories = current_user.nutrient_log.fat
    print(calories)
    return '',204

    




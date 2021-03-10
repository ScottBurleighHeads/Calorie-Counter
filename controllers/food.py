from models.calorie_count import Nutrient_DB
from models.user import User
from main import db
from flask import Blueprint , json, render_template, request 
import requests
import os
import datetime
from flask_login import login_user, current_user, logout_user
food = Blueprint("food",__name__,url_prefix="/food")

@food.route("/")
def food_home():
    summation = sum_calories()
    return render_template("Calorie_counter.html",summation=summation)

@food.route("/search", methods=["POST"])
def food_search():

    APP_ID=os.environ.get("APP_ID")
    YOUR_APP_KEY=os.environ.get("YOUR_APP_KEY")
    result = request.form["search"]
    response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?ingr={result}&app_id={APP_ID}&app_key={YOUR_APP_KEY}")
    dict_response=json.loads(response.text) 
    values=dict_response["hints"]
    length = len(dict_response["hints"])  
    if current_user:
        summation = sum_calories()  
    
    return render_template("Calorie_counter.html", values=values, length=length, summation=summation)

@food.route("/store_calories", methods=["POST"])
def food_database():
    
    current_date = datetime.datetime.now()

    user_id = User.query.filter_by(id=current_user.id).first()
    name = request.form["label"]    
    calories = request.form["calorie"]
    carb = request.form["carb"]
    protein = request.form["protein"]
    fat = request.form["fat"]
    date = current_date.date()

    
    nutrients = Nutrient_DB()
    nutrients.user_id = user_id.id
    nutrients.calories = calories
    nutrients.carb = carb
    nutrients.protein = protein
    nutrients.fat = fat
    nutrients.date = date 
    nutrients.name = name
    db.session.add(nutrients)
    db.session.commit()

    return '',204

# @food.route("/api", methods=["GET"])
# def api():
#     APP_ID=os.environ.get("APP_ID")
#     YOUR_APP_KEY=os.environ.get("YOUR_APP_KEY")
#     response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?ingr=banana&app_id={APP_ID}&app_key={YOUR_APP_KEY}")
#     dict_response = json.loads(response.text)
#     return dict_response["hints"]["food"][] 

def sum_calories():
    current_date = datetime.datetime.now()
    query = Nutrient_DB.query.filter_by(user_id=current_user.id, date=current_date.date())

    summation = 0
    for item in query:
        summation += item.calories

    return summation

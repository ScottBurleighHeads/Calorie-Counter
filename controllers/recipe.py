# https://rapidapi.com/spoonacular/api/recipe-food-nutrition?endpoint=55e1b3e1e4b0b74f06703be6

from flask import Blueprint,json, render_template,request
import requests
import os
recipe = Blueprint("recipe",__name__,url_prefix="/recipe")

@recipe.route("/")
def home_recipe():
    return render_template("recipe.html")

@recipe.route("/search", methods=["POST"])
def recipe_search():
    
    recipe = request.form["search"]
    calorie_result = request.form["calorie"]
    if not calorie_result:
        calorie_result = 1000
    APP_ID = os.environ.get("APP_ID_RECIPE")
    APP_KEY = os.environ.get("APP_KEY_RECIPE")
    string = f"https://api.edamam.com/search?q={recipe}&app_id={APP_ID}&app_key={APP_KEY}&from=0&to=3&calories={calorie_result}&health=alcohol-free"
    print(string)
    response = requests.get(f"https://api.edamam.com/search?q={recipe}&app_id={APP_ID}&app_key={APP_KEY}&from=0&to=10&calories={calorie_result}&health=alcohol-free")
    
    dict_response=json.loads(response.text)
    length = len(dict_response["hits"])

    return render_template("recipe.html",Recipe_data=dict_response["hits"],length=length)
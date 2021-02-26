from flask import Blueprint,json, render_template
import requests

food = Blueprint("food",__name__)

@food.route("/food", methods=["GET"])
def food_home():
    return render_template("Calorie_counter.html")

@food.route("/food/<string:food>", methods=["GET"])
def search_food(food):
  
    response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?ingr={food}&app_id=d50c6ade&app_key=71f98be59c54d6d436f8e639b4190f43")
    dict_response=json.loads(response.text)
    
    values=dict_response["hints"][0]["food"]
    return render_template("Calorie_counter.html", values=values)
    

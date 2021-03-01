from flask import Blueprint,json, render_template,request
import requests

food = Blueprint("food",__name__,url_prefix="/food")



@food.route("/")
def food_home():
    return render_template("Calorie_counter.html")

@food.route("/search", methods=["POST"])
def food_search():
    result = request.form["search"]
    response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?ingr={result}&app_id=d50c6ade&app_key=71f98be59c54d6d436f8e639b4190f43")
    dict_response=json.loads(response.text) 
    values=dict_response["hints"]
    length = len(dict_response["hints"])
    return render_template("Calorie_counter.html", values=values, length=length)

# @food.route("/<string:food>", methods=["GET"])
# def search_food(food):
#     response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?ingr={food}&app_id=d50c6ade&app_key=71f98be59c54d6d436f8e639b4190f43")
#     dict_response=json.loads(response.text) 
#     values=dict_response["hints"]
#     length = len(dict_response["hints"])
#     return render_template("Calorie_counter.html", values=values, length=length)

# @food.route("/test/<string:food>", methods=["GET"])
# def search_foods(food):
#     response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?ingr={food}&app_id=d50c6ade&app_key=71f98be59c54d6d436f8e639b4190f43")
#     dict_response=json.loads(response.text) 
#     return dict_response


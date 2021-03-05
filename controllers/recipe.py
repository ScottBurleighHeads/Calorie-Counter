# https://rapidapi.com/spoonacular/api/recipe-food-nutrition?endpoint=55e1b3e1e4b0b74f06703be6

from flask import Blueprint,json, render_template,request
import requests
import os
recipe = Blueprint("recipe",__name__,url_prefix="/recipe")

# @recipe.route("/")
# def hello():
   
#     url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

#     querystring = {"query":"chicken burger"}#,"diet":"vegetarian","excludeIngredients":"coconut","intolerances":"egg, gluten","number":"10","offset":"0","type":"main course"}

#     headers = {
#         'x-rapidapi-key': "2c61510f3bmshae4895a79feb61ap14b001jsn40a7389c2acd",
#         'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
#         }

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     return json.loads(response.text)

@recipe.route("/", methods=["GET"])
def recipe_search():
    
    APP_ID = os.environ.get("APP_ID_RECIPE")
    APP_KEY = os.environ.get("APP_KEY_RECIPE")
    response = requests.get(f"https://api.edamam.com/search?q=banana bread&app_id={APP_ID}&app_key={APP_KEY}&from=0&to=3&calories=591-722&health=alcohol-free")
    dict_response=json.loads(response.text)
    length = len(dict_response["hits"])

    return render_template("recipe.html",Recipe_data=dict_response["hits"],length=length)
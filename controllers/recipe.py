# https://rapidapi.com/spoonacular/api/recipe-food-nutrition?endpoint=55e1b3e1e4b0b74f06703be6

from flask import Blueprint,json, render_template,request
import requests

recipe = Blueprint("recipe",__name__,url_prefix="/recipe")

@recipe.route("/")
def hello():
    pass
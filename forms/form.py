from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class CalorieSearch(FlaskForm):
    search = StringField('search')
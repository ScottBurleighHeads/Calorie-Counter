import unittest
from main import create_app, db
from controllers.food import sum_calories
from models.calorie_count import Nutrient_DB
from models.user import User
import os
import requests
import datetime
import random
from flask_login import login_user, current_user, logout_user

# Good practice to set up a testing database
# We need to set up Class fixtures such as setUp() and tearDown()

class TestFood(unittest.TestCase):
    @classmethod
    def setUp(cls):
        if os.environ.get("FLASK_ENV") != "testing":
            raise EnvironmentError("FLASK_ENV is not in testing mode")
        cls.app = create_app()                      #Set up so dont have to run every test 
        cls.app_context = cls.app.app_context()     # App context
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()                                            # Push context
        
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db","seed"])
        
    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def test_food(self):
        
        response = self.client.get("/food/")
        self.assertEqual(response.status_code,200)
        
    def test_food_search(self):
        
        response = self.client.post("/food/search",data={"search":"apple"}) 
        self.assertEqual(response.status_code,200)
        
    def test_food_database(self):
        
        user = User()
        user.username = "testing"
        user.email = "testing@email.com"
        user.password = "password_test"
        user.first_name = "test"
        user.last_name = "testing"
        user.phone = 1234567890
        db.session.add(user)
        db.session.commit()

        # Testing the database takes the correct input and stores it on the database
        query_user = User.query.filter_by(id=11).first()
        self.assertEqual(query_user.username,"testing")
        self.assertEqual(query_user.email,"testing@email.com")
        self.assertEqual(query_user.password,"password_test")
        self.assertEqual(query_user.first_name,"test")
        self.assertEqual(query_user.last_name,"testing")
        self.assertEqual(query_user.phone,1234567890)
        self.assertIs(type(query_user.phone),int)
        
        current_date = datetime.datetime.now()

        query_nutrients = Nutrient_DB()
        query_nutrients.name = "Big banana b a n a n a s"
        query_nutrients.calories = 123  
        query_nutrients.protein = 1.1
        query_nutrients.fat = 2.2
        query_nutrients.carb = 3.3
        query_nutrients.date = current_date.date()
        db.session.add(query_nutrients)
        db.session.commit()
        
        #testing the database takes the correct input and stores it on the database
        query_nutrients = Nutrient_DB.query.filter_by(count_id=11).first()
        self.assertEqual(query_nutrients.name,"Big banana b a n a n a s")
        self.assertIs(type(query_nutrients.name),str)
        self.assertEqual(query_nutrients.calories,123)
        self.assertIs(type(query_nutrients.calories),int)
        self.assertEqual(query_nutrients.protein,1.1)
        self.assertIs(type(query_nutrients.protein),float)
        self.assertEqual(query_nutrients.fat,2.2)
        self.assertIs(type(query_nutrients.fat),float)
        self.assertEqual(query_nutrients.carb,3.3)
        self.assertIs(type(query_nutrients.carb),float)
        self.assertEqual(query_nutrients.date,current_date.date())

        # Testing the database takes the correct type of any user 
        query_types = Nutrient_DB.query.filter_by(count_id=random.randint(1,10)).first()
        self.assertIs(type(query_types.name),str)
        self.assertIs(type(query_types.calories),int)
        self.assertIs(type(query_types.protein),float)
        self.assertIs(type(query_types.fat),float)
        self.assertIs(type(query_types.carb),float)
        self.assertIs(type(query_types.carb),float)
        self.assertIs(type(query_types.date),type(current_date.date()))

 




        
        

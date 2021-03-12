import unittest
import os
from main import db, create_app
from flask import request

class TestFood(unittest.TestCase):
    @classmethod
    def setUp(cls):
        if os.environ.get("FLASK_ENV") != "testing":
            raise EnvironmentError("FLASK_ENV is not in testing mode")
        cls.app = create_app()                      # Set up so dont have to run every test 
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
    
    def test_home_recipe(self):

        response = self.client.get("/recipe/")
        self.assertEqual(response.status_code,200)
    
    def test_recipe_search(self):

        response = self.client.post("/recipe/search", data={"search":"banana bread","calorie":"300"})
        self.assertEqual(response.status_code,200)
        
    

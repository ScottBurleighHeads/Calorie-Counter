import unittest
from main import create_app, db
import os
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
        #db.create_all()                                            # Push context
        
        #runner = cls.app.test_cli_runner()
        #runner.invoke(args=["db","seed"])
        
    @classmethod
    def tearDown(cls):
        #db.session.remove()
        #db.drop_all()
        cls.app_context.pop()
    
    def test_food(self):
        
        response = self.client.get("/food/")

        self.assertEqual(response.status_code,200)
        
    def test_food_search(self):

        response = self.client.post("/food/search",data={"search":"apple"})

        self.assertEqual(response.status_code,200)





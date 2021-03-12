import unittest
from main import create_app,db
from models.user import User
import os
import random
import flask

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
    
    def login(self, username, password):
        integer = random.randint(1,10)
        user = User.query.filter_by(id=integer).first()
        return self.client.post('/login/authorise', data=dict(
            username=user.username,
            password="123"
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_login(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code,200)

    def test_login_post(self):
        response = self.client.post("/login/authorise",data={"username":"user1","password":"123"},follow_redirects=True)
        self.assertEqual(response.status_code,200)

  
    
    



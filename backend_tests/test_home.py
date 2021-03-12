import unittest
from main import create_app, db
# Good practice to set up a testing database
# We need to set up Class fixtures such as setUp() and tearDown()
class TestFood(unittest.TestCase):
    
    def test_home(self):
        app = create_app()
        client = app.test_client()
        response = client.get("/home/")

        self.assertEqual(response.status_code,200)
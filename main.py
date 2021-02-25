from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET")

from flask_marshmallow import Marshmallow
ma = Marshmallow()

from database import init_db
db = init_db(app)


from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET")

from flask_marshmallow import Marshmallow
ma = Marshmallow()

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.init_app(app)

from database import init_db
db = init_db(app)

from commands import db_commands
app.register_blueprint(db_commands)


from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
from dotenv import load_dotenv
load_dotenv()

# FLASK_APP="main:app()" calls the module then the app() function if the name was NOT create_app()

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
login_manager = LoginManager()
csrf = CSRFProtect()



# Create app is used so the test can no when to start up the app
# create_app is convetion to flask which is the factory pattern

def create_app():

    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")
    
    bcrypt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from models.user import User,get_user
    
    @login_manager.user_loader # Handles form validation
    def load_user(user_id):
        return get_user(user_id)

    from commands import db_commands        # They need context
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    from marshmallow.exceptions import ValidationError

    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)

    return app
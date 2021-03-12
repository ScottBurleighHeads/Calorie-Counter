# Add app.config.from_object("default_settings.app_config") to activate the default settings
# BN59-01182B
import os

class Config(object):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set")

        return value


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass
    # @property
    # def JWT_SECRET_KEY(self):
    #     value = os.environ.get("SECRET")

    #     if not value:
    #         raise ValueError("JWT Secret Key is not set")
        
    #     return value

class TestingConfig(Config):
    TESTING=True
    WTF_CSRF_ENABLED = False
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI_TEST")

        if not value:
            raise ValueError("DB_URI_TEST is not set")

        return value

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
from main import db 
from flask_login import UserMixin
from models.calorie_count import Nutrient_DB

def get_user(user_id):
    user=User.query.filter_by(id=user_id).first()
    return user

class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(320),nullable=False,unique=True)
    password = db.Column(db.String(400),nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    nutrient_log = db.relationship(Nutrient_DB, backref='user', lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.username
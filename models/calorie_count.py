from main import db 

class Nutrient_DB(db.Model):
    __tablename__= "nutrient_db"
    count_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    calories = db.Column(db.Integer,nullable=False)
    protein = db.Column(db.Float)
    fat = db.Column(db.Float)
    carb = db.Column(db.Float)
    image_food = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

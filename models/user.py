from main import db 

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(320),nullable=False,unique=True)
    password = db.Column(db.String(400),nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    
    def __repr__(self):
        return '<User %r>' % self.username
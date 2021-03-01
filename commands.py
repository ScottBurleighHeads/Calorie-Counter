from flask import Blueprint
from main import db
db_commands = Blueprint("db",__name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_db():
    from models.user import User
    from main import bcrypt
    from faker import Faker 

    fake = Faker()
    length = 10
    for i in range(length):
        user = User()
        user.username = f"user{i}"
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        user.first_name = fake.first_name()
        user.last_name = fake.first_name()
        user.phone = 123345334
        db.session.add(user)
    db.session.commit()

    print("Tables seeded")
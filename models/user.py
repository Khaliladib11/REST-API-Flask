from db import db

# Create user Model with 'users' as table model

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)  # id as primary key
    username = db.Column(db.String(80), unique=True, nullable=False)  # username of the user
    password = db.Column(db.String(80), nullable=False)  # the password of the user

from db import db

# Create Store Model with 'stores' name as table name
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)  # id as  primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # name of the model

    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")  # create one-to-many relationship with the items table

    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")  # create one-to-many relationship with the tags table
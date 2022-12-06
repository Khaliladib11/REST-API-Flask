from db import db

# Create Item Model with 'items' as table model
class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)  # id as primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # name of the item
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)  # the price of the item
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)  # the id of the store which will be foreign key
    store = db.relationship("StoreModel", back_populates="items")  # create many-to-one relationship with the store table
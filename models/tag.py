from db import db

# Create Store Model with 'stores' name as table name

class TagModel(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)  # id as  primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # name of the model

    # the id of the store which will be foreign key
    store_id = db.Column(db.String(), db.ForeignKey('stores.id'), nullable=False)  
    
    # create many-to-one relationship with the store table
    store = db.relationship("StoreModel", back_populates='tags')

    # create many-to-many relationship with the items table
    items = db.relationship("ItemModel", back_populates='tags', secondary="items_tags")
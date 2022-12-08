import uuid
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemUpdateSchema
from models import ItemModel
from db import db
from sqlalchemy.exc import SQLAlchemyError

# Create Blueprint for the items
blp = Blueprint("Items", "items", description="Opertations on Items")


# Endpoints start with /item
@blp.route("/item")
class ItemList(MethodView):

    # get all items
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()


    # create new item
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
        return item


# Endpoints start with /item/item_id
@blp.route("/item/<int:item_id>")
class Item(MethodView):

    # get item with specific item_id
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
    

    # update an item
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        
        # if the item already exites, update the value of 'name' and 'price'
        if item:
            item.name = item_data["name"]
            item.price = item_data["price"]

        # if the item doen't exicts create new row in the database
        else:
            item = ItemModel(id=item_id,**item_data)
        
        db.session.add(item)
        db.session.commit()
        return item


    # delete an item with specific item_id
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleteted successfully."}
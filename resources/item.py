import uuid
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores


blp = Blueprint("Items", __name__, description="Opertations on Items")

@blp.route("/item")
class Item(MethodView):
    def get(self):
        return {"items": list(items.values())}, 200

    def post(self):
        item_data = request.get_json()

        if (
            "price" not in item_data
            or "name" not in item_data
            or "store_id" not in item_data
        ):
            abort(
                400,
                message="Bad request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload."
            )

        for item in items.values():
            if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
            ):
                abort (400, message="Item already exists.")

        if item_data["store_id"] not in stores:
            abort(404, message="Store not found.")

        item_id = uuid.uuid4().hex
        item = {'id': item_id, "name": item_data['name'], "price": item_data['price']}
        items[item_id] = item

        return item, 201

@blp.route("/item/<string:item_id>")
class ItemList(MethodView):

    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")
    
    def put(self, item_id):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data:
            abort(400, message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")

        try:
            item = items[item_id]
            item |= item_data
            return item, 201
        except KeyError:
            abort(400, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(400, message="Item not found.")
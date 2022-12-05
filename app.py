from flask import Flask, request
from db import stores, items
import uuid

app = Flask(__name__)


"""
stores = [
    {
        "name": "My Store",
        "items": [
            {
            "name": "Chair",
            "price": 15.99
            }
        ]
    }
]

@app.get('/store')
def get_stores():
    return {"stores": stores}


@app.post('/store')
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data['name'], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
        
    return {"message": "Store not found"}, 404

@app.route('/store', methods=["GET", "POST"])
def store():
    if request.method == "GET":
        return {"stores": stores}, 200

    elif request.method == "POST":
        request_data = request.get_json()
        new_store = {"name": request_data['name'], "items": []}
        stores.append(new_store)
        return new_store, 201


@app.route("/store/<string:name>/item")
def items(name):
    if request.method == "GET":
        for store in stores:
            if store["name"] == name:
                return {'items': store['items']}, 200

        return {"message": "Store not found"}, 404

    elif request.method == "POST":
        request_data = request.get_json()
        for store in stores:
            if store["name"] == name:
                new_item = {"name": request_data["name"], "price": request_data["price"]}
                store["items"].append(new_item)
                return new_item, 201
        
        return {"message": "Store not found"}, 404

"""

@app.get("/")
def welcome():
    return {"Message": "Welcome to your stores!"}, 200

@app.get('/store')
def get_stores():
    return {"stores": list(stores.values())}, 200

@app.get('/store/<string:store_id>')
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"Message": "Store not found"}, 404

@app.post('/store')
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex 
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

@app.get("/items")
def get_all_items():
    return {"items": list(items.values())}, 200

@app.get("/items/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"Message": "Item not found"}, 404

@app.post("/items")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        {"message": "Store not found"}, 404

    item_id = uuid.uuid4().hex
    item = {'id': item_id, "name": item_data['name'], "price": item_data['price']}
    items[item_id] = item

    return item, 201


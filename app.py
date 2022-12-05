import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items


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


#################### STORES ####################

# Get all stores
@app.get('/store')
def get_stores():
    return {"stores": list(stores.values())}, 200


# Get store by ID
@app.get('/store/<string:store_id>')
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found.")


# Create a new store
@app.post('/store')
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request. Ensure 'name' is included in the JSON payload.")

    for store in stores.values():
        if store["name"] == store_data["name"]:
            abort(400, message="Store already exists.")
    store_id = uuid.uuid4().hex 
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201


# Update a store
@app.put("/store/<string:store_id>")
def update_store(store_id):
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request. Ensure 'name' is included in the JSON payload.")

    try:
        store = stores[store_id]
        store |= store_data
        return store, 201
    except KeyError:
        abort(400, message="store not found.")


# Delete a store
@app.delete('/store/<string:store_id>')
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(400, message="Store not found.")


#################### ITEMS ####################

# Get all items
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}, 200

# Get Item by ID
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")

# Create new Item
@app.post("/item")
def create_item():
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


# Delete Item by ID
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(400, message="Item not found.")


# Update Item
@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(400, message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")

    try:
        item = items[item_id]
        item |= item_data
        return item, 201
    except KeyError:
        abort(400, message="Item not found.")
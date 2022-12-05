from flask import Flask, request


app = Flask(__name__)

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


"""
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
    return {"stores": stores}, 200

@app.get('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return {"store": stores}, 200

    return {"message": "Store not found"}, 404

@app.post('/store')
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data['name'], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.get("/store/<string:name>/items")
def get_items(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store['items']}, 200

    return {"message": "Store not found"}, 404


@app.post("/store/<string:name>/items")
def add_items(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
        
    return {"message": "Store not found"}, 404
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from schemas import StoreSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import StoreModel

# Create Blueprint for the stores

blp = Blueprint("Stores", "stores", description="Opertations on stores")


# Endpoints start with /store
@blp.route("/store")
class StoreList(MethodView):

    # get all stores
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
    

    # Create new store
    @jwt_required
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occured during creating the store.")
        return store
    


# Endpoint start with /store/store_id
@blp.route("/store/<int:store_id>")
class Store(MethodView):

    # get a store with specific id
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store


    # delete a specific store with store_id
    @jwt_required
    def delete(self, store_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleteted successfully."}
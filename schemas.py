# Schemas file to add validation using the marchmallow, instead of doing it manually

from marshmallow import Schema, fields

# Plain Item Schema
class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


# Plain Store Schema
class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


# Plain Tag Schema
class PlainTagSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()


# Update Store Schema
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


# Item schema that has nested stores
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


# Store schema that has list of items
class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


# Tag Schema that has nested store
class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)


class UserSchema(Schema):
    # dump_only=True because we are never going to receive id from the client
    id = fields.Int(dump_only=True)  
    username = fields.Str(required=True)
    # load_only=True because we don't want to return the password to the client
    password = fields.Str(required=True, load_only=True) 
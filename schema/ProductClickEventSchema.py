from marshmallow import Schema, fields, post_load
from .UserSchema import UserSchema
from .ProductSchema import ProductSchema
from models.ProductClickEvent import ProductClickEvent


class ProductClickEventSchema(Schema):

    id = fields.Str()
    event = fields.Str()
    user = fields.Nested(UserSchema())
    actionField = fields.Str()
    timestamp = fields.Integer()
    products = fields.List(fields.Nested(ProductSchema))

    @post_load
    def make_object(self, data):
        return ProductClickEvent(**data)

    @property
    def table(self):
        return'ProductClickEvent'

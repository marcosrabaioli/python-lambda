from marshmallow import Schema, fields, post_load
from .UserSchema import UserSchema
from .ProductSchema import ProductSchema
from models.AddToCartEvent import AddToCartEvent


class AddToCartEventSchema(Schema):

    id = fields.Str()
    event = fields.Str()
    user = fields.Nested(UserSchema())
    timestamp = fields.Integer()
    products = fields.List(fields.Nested(ProductSchema))

    @post_load
    def make_object(self, data):
        return AddToCartEvent(**data)

    @property
    def table(self):
        return 'AddToCartEvent'

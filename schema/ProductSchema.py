from marshmallow import Schema, fields, post_load
from models.Product import Product


class ProductSchema(Schema):

        name = fields.Str()
        id = fields.Str()
        price = fields.Decimal()
        brand = fields.Str()
        category = fields.Str()
        variant = fields.Str()
        position = fields.Integer()
        quantity = fields.Integer()

        @post_load
        def make_object(self, data):
            return Product(**data)

        @property
        def table(self):
            return 'Product'


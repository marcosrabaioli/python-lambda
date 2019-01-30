from marshmallow import Schema, fields, post_load
from models.User import User

class UserSchema(Schema):

    id = fields.Str()

    @post_load
    def make_object(self, data):
        return User(**data)

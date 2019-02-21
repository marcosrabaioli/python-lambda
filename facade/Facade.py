import json
from dao.DAO import DAO
from utils.JsonEncoder import DecimalEncoder


class Facade(DAO):

    def __init__(self, schema):
        self.schema = schema
        super().__init__(schema)

    @staticmethod
    def _serialized(schema, object):
        json_not_encoded = schema.dump(object)
        return json.dumps(json_not_encoded, cls=DecimalEncoder)

    @staticmethod
    def _deserialized(schema, json_object):
        return schema.load(json_object)

    def jsonToObject(self, dict):
        if type(dict) is str:
            dict = json.loads(dict)
        return self._deserialized(self.schema, dict)

    def objectToJson(self, object):
        return self._serialized(self.schema, object)

    def create(self, object):
        item = super().create(object)
        item = json.dumps(item, cls=DecimalEncoder)
        return self.jsonToObject(item)

    def update(self, object):
        return super().update(object)

    def delete(self, object):
        return super().delete()

    def get(self, keys):
        item = super().get(keys)
        return item


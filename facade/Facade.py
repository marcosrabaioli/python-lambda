import json
from dao.DAO import DAO


class Facade(DAO):

    def __init__(self, schema):
        self.schema = schema
        super().__init__(schema)

    @staticmethod
    def _serialized(schema, object):
        return schema.dump(object)

    @staticmethod
    def _deserialized(schema, json):
        return schema.load(json)

    def jsonToObject(self, dict):
        if type(dict) is str:
            dict = json.loads(dict)
        return self._deserialized(self.schema, dict)

    def objectToJson(self, object):
        return self._serialized(self.schema, object)

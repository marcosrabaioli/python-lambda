import boto3
from configparser import ConfigParser
import json

class DAO(object):

    def __init__(self, schema):

        config = ConfigParser()
        config.read('../config.ini')
        environment = config.get('DEFAULT', 'enviroment')

        #DYNAMO CREDENTIALS
        region = config.get('DYNAMODB', 'region')
        url = config.get('DYNAMODB', 'url')
        acceskey = config.get('DYNAMODB', 'accesskey')
        secretkey = config.get('DYNAMODB', 'secretkey')

        self.dynamo = boto3.resource('dynamodb', region_name=region, endpoint_url=url, aws_access_key_id=acceskey, aws_secret_access_key=secretkey)
        self.schema = schema
        table = schema.table
        if environment:
            table = table + '_' + environment
        self.table = self.dynamo.Table(table)

    def create(self,object):
        if type(object) is not dict:
            return self.table.put_item(Item=self.schema.dump(object))
        return self.table.put_item(Item=object)

    def update(self, object):
        self.table.update_item(object)

    def delete(self, object):
        self.table.delete_item(object)

    def get(self, keys):
        if type(keys) is not dict:
            keys = json.loads(keys)
        response = self.table.get_item(Key= keys)
        item = response['Item']
        return self.schema.make_object(item)


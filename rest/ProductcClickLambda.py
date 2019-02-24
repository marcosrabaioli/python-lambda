import json
from facade.ProductClickEventFacade import ProductClickEventFacade
from rest.RestService import RestService
from utils.Logger import Logger

class ProductClickLambda(RestService):

    def lambda_handler(self, event, context):

        operations = {
            'DELETE': lambda p: self.delete(p),
            'GET': lambda p: self.get(p),
            'POST': lambda p: self.post(p),
            'PUT': lambda p: self.put(p),
        }

        operation = event['httpMethod']
        if operation in operations:
            payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
            return operations[operation](payload)
        else:
            Logger.error(ValueError('Unsupported method "{}"'.format(operation)))
            return self.responseForError((ValueError('Unsupported method "{}"'.format(operation))))

    def post(self, payload):

        productClickfacade = ProductClickEventFacade()

        try:
            productClick = productClickfacade.create(payload)
        except Exception as err:
            Logger.error(err)
            return self.responseForError(err)

        return self.responseForCreate(productClickfacade.objectToJson(productClick))

    def get(self, keys):
        productClickfacade = ProductClickEventFacade()
        try:
            productClick = productClickfacade.get(keys)
        except Exception as err:
            Logger.error(err)
            return self.responseForError(err)
        return self.responseForOK(productClickfacade.objectToJson(productClick))

    def delete(self, object):
        pass

    def put(self, object):
        pass

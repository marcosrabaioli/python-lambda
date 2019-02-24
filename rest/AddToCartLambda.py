import json
from facade.AddToCartEventFacade import AddToCartEventFacade
from rest.RestService import RestService
from utils.Logger import Logger


class AddToCartLambda(RestService):

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

        addToCartEventFacade = AddToCartEventFacade()

        try:
            addToCart = addToCartEventFacade.create(payload)
        except Exception as err:
            Logger.error(err)
            return self.responseForError(err)

        return self.responseForCreate(addToCartEventFacade.objectToJson(addToCart))

    def get(self, keys):
        addToCartEventFacade = AddToCartEventFacade()
        try:
            addToCart = addToCartEventFacade.get(keys)
        except Exception as err:
            Logger.error(err)
            return self.responseForError(err)
        return self.responseForOK(addToCartEventFacade.objectToJson(addToCart))

    def delete(self, object):
        pass

    def put(self, object):
        pass
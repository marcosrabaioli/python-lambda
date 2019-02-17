import json

from facade.ProductClickEventFacade import ProductClickEventFacade
from rest.RestService import RestService


class ProductClickLambda(RestService):

    def lambda_handler(self, event, context):
        '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
        access to the request and response payload, including headers and
        status code.

        To scan a DynamoDB table, make a GET request with the TableName as a
        query string parameter. To put, update, or delete an item, make a POST,
        PUT, or DELETE request respectively, passing in the payload to the
        DynamoDB API as a JSON body.
        '''
        #print("Received event: " + json.dumps(event, indent=2))

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
            return self.responseForError((ValueError('Unsupported method "{}"'.format(operation))))

    def post(self, payload):

        productClickfacade = ProductClickEventFacade()

        try:
            productClick = productClickfacade.jsonToObject(payload)
            productClick = productClickfacade.create(productClick)
        except Exception as err:
            return self.responseForError(err)

        return self.responseForCreate(productClick)

    def get(self, keys):
        productClickfacade = ProductClickEventFacade()
        try:
            productClick = productClickfacade.get(keys)
        except Exception as err:
            return self.responseForError(err)
        return self.responseForOK(productClick)

    def delete(self, object):
        pass

    def put(self, object):
        pass
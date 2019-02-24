from rest.AddToCartLambda import AddToCartLambda


class TestAddToCartLambda(object):

    clazz = AddToCartLambda()

    def test_post(self):
        event = dict()
        event['httpMethod'] = "POST"
        event['body'] = '''{
                           "id": "1",
                           "event":"addToCart",
                            "user":{
                                "id":"1"
                            },
                            "timestamp": 21212121212,
                            "products":[
                                    {
                                       "name":"name",
                                       "id":"1",
                                       "price":20,
                                       "brand":"brand",
                                       "category":"cat",
                                       "variant":"variant",
                                       "position": 1
                                    }
                                 ]
                              }'''

        res = self.clazz.lambda_handler(event, None)
        assert res['statusCode'] == 201

    def test_get(self):
        event = dict()
        event['httpMethod'] = "GET"
        event['queryStringParameters'] = '{"id": "1"}'

        res = self.clazz.lambda_handler(event, None)
        assert res['statusCode'] == 200

from rest.ProductcClickLambda import ProductClickLambda


class TestProductClickLambda(object):

    clazz = ProductClickLambda()

    def test_post(self):
        event = dict()
        event['httpMethod'] = "POST"
        event['body'] = '''{
                           "id": "1",
                           "event":"productClick",
                            "user":{
                                "id":"user.id"
                            },
                            "actionField":  "Search Results",
                            "timestamp": 21212121212,
                            "products":[
                                    {
                                       "name":"productObj.name",
                                       "id":"productObj.id",
                                       "price":20,
                                       "brand":"productObj.brand",
                                       "category":"productObj.cat",
                                       "variant":"productObj.variant",
                                       "position": 1
                                    }
                                 ]
                              }'''

        res = self.clazz.lambda_handler(event, None)
        assert res['statusCode'] == 200
from facade.Facade import Facade
from schema.ProductClickEventSchema import ProductClickEventSchema


class ProductClickEventFacade(Facade):

    def __init__(self):
        schema = ProductClickEventSchema()
        super().__init__(schema)




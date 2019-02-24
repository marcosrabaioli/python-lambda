from facade.Facade import Facade
from schema.AddToCartEventSchema import AddToCartEventSchema


class AddToCartEventFacade(Facade):

    def __init__(self):
        schema = AddToCartEventSchema()
        super().__init__(schema)




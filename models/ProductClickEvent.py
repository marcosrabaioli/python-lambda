class ProductClickEvent(object):

    def __init__(self, event, user, actionField, timestamp, products, id=None):
        self.id = id
        self.event = event
        self.user = user
        self.actionField = actionField
        self.timestamp = timestamp
        self.products = products

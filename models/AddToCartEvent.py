class AddToCartEvent(object):

    def __init__(self, id, event, user, timestamp, products):
        self.id = id
        self.event = event
        self.user = user
        self.timestamp = timestamp
        self.products = products

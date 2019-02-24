class Product(object):

    def __init__(self, name, price, brand, category, variant, position,quantity=None, id=None):
        self.name = name
        self.id = id
        self.price = price
        self.brand = brand
        self.category = category
        self.variant = variant
        self.position = position
        self.quantity = quantity





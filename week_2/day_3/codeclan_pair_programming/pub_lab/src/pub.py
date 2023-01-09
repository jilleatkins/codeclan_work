class Pub:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.stock = {}

    def increase_till(self, amount):
        self.till += amount

    def serve_drink(self, customer, drink):
        if self.check_age(customer):
            self.increase_till(drink.price)
            customer.decrease_wallet(drink.price)

    def check_age(self, customer):
        if customer.age >= 18:
            return True 
        else:
            return False
class Customer:

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = []
        # these properties will show up automatically every time we create a new customer


    def reduce_cash(self, cash):
        self.cash -= cash
        # equivalent to: self.cash = self.cash - cash


    def pet_count(self):
        return len(self.pets)
        # len() returns the size of the sequence


    def add_pet(self, pet):
        self.pets.append(pet)


    def get_total_value_of_pets(self):
        total = 0

        for pet in self.pets:
            total += pet.price
        
        return total



class PetShop:

    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.pets_sold = pets
        self.total_cash = total_cash
        self.pets_sold = 0
        # this value is 0 because when creating an instance of a new pet shop, it will automatically have
        # 0 stock of any pets - it will just always set this to zero when we create a new pet shop

        # we don't need to have all the list elements within the parameters() section, we can add extra stuff
        # e.g. we added pets_sold to add an initial value but didnt need to add it as an parameter
        
    def stock_count(self):
        return len(self.pets)


    def increase_pets_sold(self):
        self.pets_sold += 1


    def increase_total_cash(self, amount):
        self.total_cash += amount


    def remove_pet(self, pet):
        self.pets.remove(pet)


    def find_pet_by_name(self, name):
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

        # the following example demonstrates that you can call 
        # another method that you have either created or imported 
        # from within the same class to use
        # for another method
    def sell_pet_to_customer(self, pet_name, customer):
        pet = self.find_pet_by_name(pet_name)
        customer.reduce_cash(pet.price)
        self.increase_total_cash(pet.price)
        self.increase_pets_sold()
        # ^this method automatically increments pets_sold by 1 
        # by calling it
        self.remove_pet(pet)
        customer.add_pet(pet)
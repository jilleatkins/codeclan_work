# #1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
    
# #2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#3
def add_or_remove_cash(pet_shop,amount):
    pet_shop["admin"]["total_cash"] += amount

#4
# def add_or_remove_cash(pet_shop,amount):
#     pet_shop["admin"]["total_cash"] -= amount

#5
def get_pets_sold(pets_sold):
    return pets_sold ["admin"]["pets_sold"]
    
# 6
def increase_pets_sold(pet_stock, pets_sold):
    pet_stock ["admin"]["pets_sold"] += pets_sold

# 7
def get_stock_count(pet_shop):
    stock = 0
    for pet in pet_shop ["pets"]:
        stock += 1
    return stock
    
# ANSWER 
# def get_stock_count
#   return len(pet_shop["pets"]) 

# 8
def get_pets_by_breed(pet_shop, breed_type):
    total_breeds = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_type:
            total_breeds.append(breed_type)
    return total_breeds

# 9 
def get_pets_by_breed (pet_shop, breed_type):
    total_breeds = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_type:
            total_breeds.append(breed_type)
    return total_breeds

# 10
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return(pet)

# 11
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return(pet)
        else:
            (pet) is None
# this question doesn't really need an answer or a function written for it
# because the previous function answers this automatically
# (i.e. automatically returns None)
       
# 12
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

# ANSWER
# def remove_pet_by_name(pet_shop, name):
    # pet_to_delete = find_pet_by_name(pet_shop, name)
    # pet_shop["pets"].remove(pet_to_delete)
        
# 13
# def add_pet_to_stock (pet_shop, new_pet):
#     count = 0
#     for pet in pet_shop["pets"]:
#         count += 1
#     for pet in new_pet["name"]:
#         count += 1
#         return count

# ANSWER
# def add_pet_to_stock (pet_shop, pet):
#     pet_shop["pets"].append(pet)

# 14
def get_customer_cash (customer):
    return customer["cash"]

# 15

# 16

# 17
def add_pet_to_customer():

# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(list):
    return list["name"]

def get_total_cash(list):
    return list["admin"]["total_cash"]

def add_or_remove_cash(list, num_1):
    list["admin"]["total_cash"] += num_1
    return list["admin"]["total_cash"]

def get_pets_sold(list):
    return list["admin"]["pets_sold"]

def increase_pets_sold(list, num_1):
    list["admin"]["pets_sold"] += num_1
    return list["admin"]["pets_sold"]

def get_stock_count(list):
    return len(list["pets"])

def get_pets_by_breed(shop, breed):
    pets_list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets_list.append(pet)
        elif pet["breed"] != breed:
            pass
    return pets_list

def find_pet_by_name(shop, name):
    pet_name = None
    for pet in shop["pets"]:
        if pet["name"] == name:
            pet_name = pet
        elif pet["name"] != name: 
            pass
    return pet_name


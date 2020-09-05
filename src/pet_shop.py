# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, num_1):
    shop["admin"]["total_cash"] += num_1
    return shop["admin"]["total_cash"]

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, num_1):
    shop["admin"]["pets_sold"] += num_1
    return shop["admin"]["pets_sold"]

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets_list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets_list.append(pet)
        elif pet["breed"] != breed:
            pass
    return pets_list

def find_pet_by_name(shop, name):
    return_pet = None

    for pet in shop["pets"]:
        if pet["name"] == name:
            return_pet = pet

    return return_pet

def remove_pet_by_name(shop, name):
    index = 0
    for pet in shop["pets"]:
        if pet["name"] != name:
            index += 1
        elif pet["name"] == name:
            del(shop["pets"][index])
            return
        
def add_pet_to_stock(shop,new_pet):
    shop["pets"].append(new_pet)
           
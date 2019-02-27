import json


def find_pet(id):
    found_pet = None
    with open('data/pets.json') as f:
        pets = json.load(f)
        for pet in pets:
            if pet['id'] == id:
                found_pet = pet
                break
    return found_pet


def get_pets():
    pets = []
    with open('data/pets.json') as f:
        pets = json.load(f)
    return pets

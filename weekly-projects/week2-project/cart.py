import json


def get_cart():
    with open('data/cart.json') as f:
        cart = json.load(f)
        return cart


def save_cart(data):
    with open('data/cart.json', 'w') as f:
        json.dump(data, f)


def get_cart_total(cart):
    total = 0
    for pet in cart['pets']:
        total += float(pet['price'])
    return total
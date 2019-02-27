from flask import Flask
from flask import render_template, url_for, redirect

from cart import get_cart, save_cart, get_cart_total
from pets import get_pets, find_pet


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/pets/")
def show_pets():
    pets = get_pets()
    return render_template('pets.html', pets=pets)


@app.route("/pets/<int:pet_id>/")
def show_pet(pet_id):
    pet = find_pet(pet_id)
    return render_template('pet.html', pet=pet)


@app.route("/cart/")
def show_cart():
    cart = get_cart()
    total = get_cart_total(cart)
    return render_template('cart.html', cart=cart, total=total)


@app.route("/cart/add_pet/<int:pet_id>")
def add_pet_to_cart(pet_id):
    cart = get_cart()
    pet = find_pet(pet_id)
    if pet is not None:
        cart['pets'].append(pet)
        save_cart(cart)
    return redirect(url_for('show_cart'))


@app.route("/cart/empty/")
def empty_cart():
    cart = {"pets": []}
    save_cart(cart)
    return redirect(url_for('index'))
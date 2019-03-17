from flask import Flask
from flask import flash, render_template, request, url_for, session, redirect

from auth import Auth
from recipes import Recipes

app = Flask(__name__)
app.secret_key = b'aj(>,m87hJn9+-alkjns*jkj90($'


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username', None)
    password = request.form.get('password', None)
    auth = Auth()
    if auth.login(username, password):
        return redirect(url_for('show_recipes'))

    flash('Could not log you in')
    return render_template('login.html')



@app.route("/sign-up/", methods=["POST", "GET"])
def sign_up():
    if request.method == 'GET':
        return render_template('sign-up.html')

    username = request.form.get('username', None)
    password = request.form.get('password', None)
    password2 = request.form.get('password2', None)

    auth = Auth()
    error = None

    if auth.has_user(username):
        error = 'There is already a user with that name'
    elif password != password2:
        error = 'Passwords must match'

    if error:
        flash(error)
        return redirect(url_for('sign_up'))

    auth.create_user(username, password)
    auth.login(username, password)
    return redirect(url_for('show_recipes'))


@app.route("/logout/")
def logout():
    auth = Auth()
    auth.logout()
    return redirect(url_for('show_recipes'))


@app.route("/")
@app.route("/recipes/")
def show_recipes():
    auth = Auth()
    if auth.is_logged_in():
        recipe_manager = Recipes()
        user = auth.get_current_user()
        recipes = recipe_manager.get_recipes(user['user_id'])
        print(recipes)
        print([recipe['recipe_id'] for recipe in recipes])
        return render_template('recipes.html', recipes=recipes)
    return redirect(url_for('login'))


@app.route("/recipes/new/", methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'GET':
        return render_template('add_recipe.html')

    title = request.form.get('title', None)
    description = request.form.get('description')
    image = request.form.get('image', None)
    ingredients = request.form.get('ingredients', None)
    user_id = Auth().get_current_user()['user_id']

    recipe_manager = Recipes()
    recipe_manager.add_recipe({
        'title': title,
        'description': description,
        'image': image,
        'ingredients': ingredients
    }, user_id)
    return redirect(url_for('show_recipes'))


@app.route("/recipes/<int:recipe_id>/")
def show_recipe(recipe_id):
    recipe = Recipes().get_recipe(recipe_id)
    return render_template('recipe.html', recipe=recipe)

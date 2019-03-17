import sqlite3

DB_FILE_PATH = 'data/data.db'


class Recipes:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE_PATH)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_recipes(self, user_id):
        '''Get a list of dictionaries representing recipes that belong
        to the given user.'''
        data = (user_id, )
        self.cursor.execute('''
            select * from recipe 
            where recipe.user_id = ?''', data)
        rows = self.cursor.fetchall()
        return rows

    def get_recipe(self, recipe_id):
        data = (recipe_id, )
        self.cursor.execute('''
            select * from recipe
            where recipe_id = ?''',
            data)
        row = self.cursor.fetchone()
        return row

    def add_recipe(self, data, user_id):
        data_tuple = (data['title'], data['description'],
                      data['image'], data['ingredients'],
                      user_id)
        self.cursor.execute('''
            insert into recipe
            (title, description, image, ingredients, user_id)
            values
            (?, ?, ?, ?, ?)''', data_tuple)
        self.conn.commit()
        self.cursor.close()

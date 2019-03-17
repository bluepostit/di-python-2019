drop table if exists user;
drop table if exists recipe;
drop table if exists cocktail;

create table user (
	user_id integer primary key,
	username text not null,
	password text not null
);

create table recipe (
	recipe_id integer primary key,
	title text not null,
	description text,
	image text,
	ingredients text not null,
	user_id integer not null
);

insert into user (username, password)
values ('admin', 'root123');


insert into recipe (title, description, image, ingredients, user_id)
	values 
	('Rhubarb Pie', "It's delicious sweetness", "http://assets.simplyrecipes.com/wp-content/uploads/2014/06/strawberry-rhubarb-pie-horiz-a-1600.jpg", 
"4 cups chopped rhubarb
1 1/3 cups white sugar
6 tablespoons all-purpose flour

1 tablespoon butter
1 recipe pastry for a 9 inch double crust pie",
    1),
    ('Spinach bourekas', "Crunchy snacks", 'https://www.lurpak.com/siteassets/final-recipe-assets/global/around-the-world-2016/lurpak_b_israel_bourekas.jpg',
"8 cups spinach leaves
1 1/2 tsp. olive oil, plus 6 Tbs. for brushing phyllo, divided
1 small onion, finely chopped (1 cup)
1/4 cup part-skim ricotta cheese
1/3 cup feta cheese, finely crumbled
1 large egg, lightly beaten
12 sheets frozen phyllo dough, thawed
1 tsp. sesame seeds",
1);
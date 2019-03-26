DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS phone_call;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT NOT NULL,
	password TEXT NOT NULL
);

CREATE TABLE customer (
	customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	phone TEXT NULL,
	email TEXT NOT NULL,
	address1 TEXT NULL,
	address2 TEXT NULL,
	postal_code TEXT NULL,
	city TEXT NOT NULL,
	country TEXT NOT NULL,
	added_by INTEGER NOT NULL,
	FOREIGN KEY(added_by) REFERENCES user(user_id)
);

CREATE TABLE phone_call (
	call_id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	call_time TEXT NOT NULL,
	notes TEXT NOT NULL
);





INSERT INTO user (username, password)
	VALUES ('admin', 'password');

INSERT INTO customer (first_name, last_name, phone, email, address1, address2, postal_code, city, country, added_by)
VALUES 
	('Sandra', 'Jones', '000999', 'sandra.jones@no.spam', '1 Main Way', 'Apt. 4', '999', 'Metropolis', 'Anglerica', 1),
	('Marvin', 'Smith', '111000', 'marvin.smith@no.spam', '1 Daleview Rd', '', '999', 'Metropolis', 'Anglerica', 1),
	('Anne', 'Green', '2378787', 'anne.green@no.spam', '87 High Way', 'Apt. 22', '999', 'Metropolis', 'Anglerica', 1),
	('Bryan', 'McTavish', '231312', 'bryanmac@no.spam', '23B Central Union Way', '', '999', 'Metropolis', 'Anglerica', 1);

-- YYYY-MM-DD HH:MM:SS.SSS
INSERT INTO phone_call (customer_id, user_id, call_time, notes)
VALUES
	(1, 1, "2019-02-22 17:03:21", "Sandra was not interested in our products"),
	(2, 1, "2019-02-22 17:03:21", "Mr Smith was not in; will call back later"),
	(3, 1, "2019-02-22 17:03:21", "Anne was away, left a message."),
	(1, 1, "2019-02-22 17:03:21", "Convinced Sandra to buy our cheapest product. Yay!")
--create table with id, email, name attributes
--create table if not exist
CREATE TABLE IF NOT EXISTS users(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
)

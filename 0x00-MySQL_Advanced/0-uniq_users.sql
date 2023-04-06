--create table users with fields id, email, name
--creates the table if it does not exist
CREATE TABLE if NOT EXISTS users(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) UNIQUE NOT NULL,
	name varchar(255),
);

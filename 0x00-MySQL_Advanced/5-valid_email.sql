-- A SQL script that creates a trigger that resets the valid email on when email has been changed
DELIMETER $$ ;
CREATE TRIGGER email_trigger BEFORE UPDATE
ON users
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF
END$$

-- SQL script that creates a function that divides two numbers
DELIMITER $$ ;
CREATE FUNCTION SafeDiv(a INTEGER, B INTEGER)
RETURNS FLOAT
BEGIN
    DECLARE result FLOAT
    IF b = 0
        RETURN 0;
    END IF;
    SET result = a / b;
      RETURN result;
END;$$
DELIMITER ;

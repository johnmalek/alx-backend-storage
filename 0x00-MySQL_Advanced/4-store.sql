-- A SQL script that creates a trigger that decreases the quantity of an item
CREATE TRIGGER quantity_trigger BEFORE INSERT ON items
FOR EACH ROW UPDATE items SET @quantity = @quantity - NEW.quantity;

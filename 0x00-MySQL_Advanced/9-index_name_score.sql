-- SQL script that creates index on names and first later of name and score
CREATE INDEX idx_name_first_score ON names(name(1), score);

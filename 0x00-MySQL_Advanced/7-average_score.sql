-- A stored procedure that computes the average score
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INTEGER)
SELECT AVG(score) FROM users;

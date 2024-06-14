-- Source: https://www.codewars.com/kata/5a1a9e3c1e4b7f3b6b0000d0
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET average_score = (SELECT SUM(score) / COUNT(*) FROM corrections AS c WHERE c.user_id = user_id)
	WHERE id = user_id;
END;$$
DELIMITER ;

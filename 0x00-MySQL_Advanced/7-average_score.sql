-- Source: https://www.codewars.com/kata/5a1a9e3c1e4b7f3b6b0000d0
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    
    -- Calculate the average score for the given user_id
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
    
    -- Update the average_score in the users table
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END $$

DELIMITER ;
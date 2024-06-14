-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
--that computes and store the average weighted score for a student.
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight FLOAT;
    DECLARE weighted_score_sum FLOAT;
    
    -- Calculate the sum of weights and the sum of weighted scores for the given user_id
    SELECT SUM(weight) INTO total_weight,
           SUM(score * weight) INTO weighted_score_sum
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;
    
    -- Update the average_score in the users table with the weighted average
    UPDATE users
    SET average_score = CASE
        WHEN total_weight > 0 THEN weighted_score_sum / total_weight
        ELSE 0
    END
    WHERE id = user_id;
END $$

DELIMITER ;
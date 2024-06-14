-- Source: https://www.codewars.com/kata/5a1a9e3c1e4b7f3b6b0000d0
DELIMITER $$

DROP PROCEDURE IF EXISTS AddBonus $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    
    -- Check if the project exists and get its ID, if not, create a new project
    SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    
    -- Insert the correction with the user_id, project_id, and score
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$

DELIMITER ;
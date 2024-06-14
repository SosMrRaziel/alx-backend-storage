-- Create an index for the first letter of the name and the score
ALTER TABLE names ADD INDEX idx_name_first_score (name(1), score);
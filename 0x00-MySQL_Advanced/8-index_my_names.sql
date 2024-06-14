-- Create an index for the first letter of the name
ALTER TABLE names ADD INDEX idx_name_first (name(1));
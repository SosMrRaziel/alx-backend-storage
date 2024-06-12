-- Create a table users with the following requirements:
-- id: INT AUTO_INCREMENT PRIMARY KEY
-- email: VARCHAR(255) NOT NULL UNIQUE
-- name: VARCHAR(255)
-- country: ENUM with values US, CO, TN (default US)

CREATE TABLE if NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

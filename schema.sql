-- 1. Create the database container
CREATE DATABASE SecureAuthDB;
USE SecureAuthDB;

-- 2. Create the users data table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(64) NOT NULL, -- Holds the exact 64-character SHA-256 string
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
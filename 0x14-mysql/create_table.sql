-- create database, table, and add permissions
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (id INT AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY (id));
INSERT INTO nexus6 (name) VALUES ("leon");
GRANT SELECT ON tyrell_corp.nexus6 TO `holberton_user`@`localhost`;

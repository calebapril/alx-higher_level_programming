-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- states description:
    -- id INT unique, auto generated, can’t be null and is a primary key
    -- name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(256) NOT NULL);


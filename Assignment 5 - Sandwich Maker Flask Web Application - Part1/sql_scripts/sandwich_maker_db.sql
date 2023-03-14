-- Development code:
DROP SCHEMA IF EXISTS `sandwich_maker`;
--
CREATE SCHEMA IF NOT EXISTS `sandwich_maker` ;
USE `sandwich_maker`;

-- Development code:
DROP TABLE IF EXISTS resources;
DROP TABLE IF EXISTS sandwiches;
DROP TABLE IF EXISTS recipes;
--

CREATE TABLE resources (
	id int UNIQUE NOT NULL AUTO_INCREMENT,
	item varchar(50) NOT NULL,
    amount int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE sandwiches (
	id int UNIQUE NOT NULL AUTO_INCREMENT,
	sandwich_size varchar(50) NOT NULL,
    price decimal(8,2) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE recipes (
	sandwich_size int NOT NULL,
    item int NOT NULL,
    amount int NOT NULL,
    FOREIGN KEY (sandwich_size) REFERENCES sandwiches(id),
    FOREIGN KEY (item) REFERENCES resources(id)
);

INSERT INTO resources (item, amount) VALUES
('bread', 12),
('ham', 18),
('cheese', 24);

INSERT INTO sandwiches (sandwich_size, price) VALUES
('small', 1.75),
('medium', 3.25),
('large', 5.5);

/*
INSERT INTO recipes VALUES
(1, 1, 2),
(1, 2, 4),
(1, 3, 4),

(2, 1, 4),
(2, 2, 6),
(2, 3, 8),

(3, 1, 6),
(3, 2, 8),
(3, 3, 12);
*/
DROP SCHEMA IF EXISTS sandwich;
CREATE SCHEMA sandwich;
USE sandwich;



DROP TABLE IF EXISTS resources;
CREATE TABLE resources (
	id smallint NOT NULL AUTO_INCREMENT,
	item varchar(50) NOT NULL,
    amount int NOT NULL,
    PRIMARY KEY (id)
);



DROP TABLE IF EXISTS sandwiches;
CREATE TABLE sandwiches (
	id smallint NOT NULL AUTO_INCREMENT,
	sandwich_size varchar(50) NOT NULL,
    price decimal(5,2) NOT NULL,
    PRIMARY KEY (id)
);



DROP TABLE IF EXISTS recipes;
CREATE TABLE recipes (
	sandwich_size varchar(50),
    item varchar(50),
    amount int
);






INSERT INTO resources (item, amount) VALUES
('bread', 12),
('ham', 18),
('cheese', 24);



INSERT INTO sandwiches (sandwich_size, price) VALUES
('small', 1.75),
('medium', 3.25),
('large', 5.5);



INSERT INTO recipes VALUES
('small', 'bread', 2),
('small', 'ham', 4),
('small', 'cheese', 4),

('medium', 'bread', 4),
('medium', 'ham', 6),
('medium', 'cheese', 8),

('large', 'bread', 6),
('large', 'ham', 8),
('large', 'cheese', 12);



SELECT * FROM sandwiches;
SELECT * FROM resources;
-- SELECT * FROM recipes;

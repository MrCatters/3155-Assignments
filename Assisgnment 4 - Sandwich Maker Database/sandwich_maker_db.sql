DROP SCHEMA IF EXISTS sandwich;
CREATE SCHEMA sandwich;
USE sandwich;



DROP TABLE IF EXISTS resources;
CREATE TABLE resources (
	id smallint UNIQUE NOT NULL AUTO_INCREMENT,
	item varchar(50) NOT NULL,
    amount int NOT NULL,
    PRIMARY KEY (id)
);



DROP TABLE IF EXISTS sandwiches;
CREATE TABLE sandwiches (
	id smallint UNIQUE NOT NULL AUTO_INCREMENT,
	sandwich_size varchar(50) NOT NULL,
    price decimal(5,2) NOT NULL,
    PRIMARY KEY (id)
);



DROP TABLE IF EXISTS recipes;
CREATE TABLE recipes (
	sandwich_size smallint NOT NULL,
    item smallint NOT NULL,
    amount smallint NOT NULL,
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



-- SELECT * FROM sandwiches;
-- SELECT * FROM resources;
SELECT sandwiches.sandwich_size, resources.item, recipes.amount
FROM recipe
INNER JOIN sandwiches ON recipes.sandwich_size = sandwiches.id
INNER JOIN resources ON recipes.item = resources.id
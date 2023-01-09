DROP TABLE lightsabers;
DROP TABLE characters;


CREATE TABLE characters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    darkside BOOLEAN,
    age INT
);

CREATE TABLE lightsabers(
    id SERIAL PRIMARY KEY,
    colour VARCHAR(255) NOT NULL,
    hilt_metal VARCHAR(255) NOT NULL,
    character_id INT REFERENCES characters(id)
);

INSERT INTO characters (name, darkside, age) VALUES ('Obi-Wan Kenobi', false, 27);
INSERT INTO characters (name, darkside, age) VALUES ('Anakin Skywalker', false, 19);
INSERT INTO characters (name, darkside, age) VALUES ('Darth Maul', true, 32);
INSERT INTO characters (name, darkside, age) VALUES ('Yoda', false, 200);

INSERT INTO lightsabers (colour, hilt_metal, character_id) VALUES ('green', 'palladium', 2);
INSERT INTO lightsabers (colour, hilt_metal, character_id) VALUES ('red', 'gold', 3);
INSERT INTO lightsabers (colour, hilt_metal, character_id) VALUES ('red', 'copper', 4);


-- SELECT * FROM characters;
-- prints whole database

-- SELECT name FROM characters;
-- prints list of names from database

-- SELECT * FROM characters WHERE name='Yoda';
-- finds data for particular name in database

-- SELECT * FROM characters WHERE darkside=true;
-- selects names only if they are with the darkside

-- SELECT COUNT(*) FROM characters;
-- counts data

UPDATE characters SET darkside = true;

-- SELECT * FROM characters;
-- sets all data in database to darkside, true
-- the second line 'select from characters' needs to be copied and pasted from above and run again every time (kind of like running the 
-- 'print' function)

UPDATE characters SET darkside = false WHERE name = 'Anakin Skywalker';

-- SELECT * FROM characters;

UPDATE characters SET (name, darkside) = ('Darth Vader', true) WHERE name = 'Anakin Skywalker';

-- SELECT * FROM characters;

INSERT INTO characters (name, darkside, age) VALUES ('Luke Skywalker', false, 17);

UPDATE characters SET age = 65 WHERE name = 'Obi-Wan Kenobi';

-- SELECT * FROM characters;

-- DELETE FROM characters WHERE name = 'Darth Maul';

INSERT INTO characters (name, darkside, age) VALUES ('Storm Trooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Storm Trooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Storm Trooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Storm Trooper', true, 25);

UPDATE characters SET age = 29 WHERE id = 9;

-- SELECT * FROM characters;

SELECT * FROM lightsabers WHERE character_id = 3;
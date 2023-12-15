-- list all capital cities of califonia
SELECT id, name FROM cities WHERE id = (SELECT id FROM states WHERE id = 1) ORDER BY id;

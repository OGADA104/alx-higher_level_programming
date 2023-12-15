-- list all capital cities of califonia
SELECT id, name FROM cities WHERE id = (SELECT id from states WHERE id = 1) ORDER BY id;

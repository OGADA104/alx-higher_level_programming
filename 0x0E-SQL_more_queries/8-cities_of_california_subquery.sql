-- list all capital cities of califonia
SELECT id, name, (SELECT name FROM states WHERE id = cities.state_id) AS state_name FROM cities WHERE id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;

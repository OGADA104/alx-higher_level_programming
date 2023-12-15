-- list all capital cities of califonia
USE hbtn_0d_usa;
SELECT id, name FROM cities WHERE id = (SELECT id from states WHERE id = 1) ORDER BY id;

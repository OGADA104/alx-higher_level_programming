-- list records with same scores
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;

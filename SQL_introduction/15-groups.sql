-- Script that count how many values there is for each score
SELECT `score`, COUNT(`score`) AS `number`
FROM `second_table`
GROUP BY `score`
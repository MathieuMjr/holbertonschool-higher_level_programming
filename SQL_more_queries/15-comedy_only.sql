-- Script that list all shows that are comedies
SELECT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres sg
    ON s.id = sg.show_id
LEFT JOIN tv_genres g
    ON g.id = sg.genre_id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;

-- correction gpt : 
-- INNER JOIN sans WHERE
-- Les left and right join sont utiles pour garder
-- des NULLS (on garde les infos qui ne matchent pas avec
-- l'autre table)
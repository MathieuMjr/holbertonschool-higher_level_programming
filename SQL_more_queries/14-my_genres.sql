-- Script that tells how many genre there is for Dexter show
SELECT tg.name
FROM tv_genres tg
RIGHT JOIN tv_show_genres tsg
    ON tg.id = tsg.genre_id
RIGHT JOIN tv_shows ts
    ON  ts.id = tsg.show_id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
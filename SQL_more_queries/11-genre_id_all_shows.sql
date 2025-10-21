-- Script that gives the genre ids of each shows with left join so we can see show without genre
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM tv_shows
LEFT JOIN tv_show_genres
    ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
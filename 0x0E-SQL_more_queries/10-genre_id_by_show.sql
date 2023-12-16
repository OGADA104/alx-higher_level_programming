-- IMPORT DB
SOURCE hbtn_0d_tvshows.sql;
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_shows_genres ON tv_shows.id = tv_show_genres.genre_id WHERE tv_shows_genres.genre_id IS NOT NULL;

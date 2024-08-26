-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- and edited thoroughly
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE steam_twitch_agg (
app_id INTEGER NOT NULL,
title VARCHAR(128) NOT NULL,
hours_watched FLOAT NOT NULL,
hours_streamed FLOAT NOT NULL,
average_streamers INTEGER NOT NULL,
average_viewers INTEGER NOT NULL,
average_channels INTEGER NOT NULL,
release_date DATE NOT NULL,
reviews_total INTEGER NOT NULL,
review_avg_percent INTEGER NOT NULL,
launch_price_cents INTEGER NOT NULL,
dataset_est_rev_cents INTEGER NOT NULL,
PRIMARY KEY (app_id)
);

CREATE TABLE twitch_monthly (
app_id INTEGER NOT NULL REFERENCES steam_twitch_agg(app_id),
title VARCHAR(128) NOT NULL,
rank INTEGER NOT NULL,
month INTEGER NOT NULL,
year INTEGER NOT NULL,
hours_watched INTEGER NOT NULL,
hours_streamed INTEGER NOT NULL,
peak_viewers INTEGER NOT NULL,
peak_channels INTEGER NOT NULL,
streamers INTEGER NOT NULL,
average_viewers INTEGER NOT NULL,
average_channels INTEGER NOT NULL,
PRIMARY KEY (app_id, month, year)
);

CREATE TABLE tags (
app_id INTEGER NOT NULL REFERENCES steam_twitch_agg(app_id),
tag VARCHAR(128) NOT NULL,
PRIMARY KEY (app_id, tag)
);

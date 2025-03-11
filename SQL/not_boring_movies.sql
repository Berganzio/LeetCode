-- create cinema table
CREATE TABLE IF NOT EXISTS cinema (
    id int primary key,
    movie varchar(255),
    description varchar(255),
    rating float
);
-- insert data into cinema
INSERT INTO cinema(id, movie, description, rating)
VALUES (1, "War", "Great 3D", 8.9),
    (2, "Science", "Fiction", 8.5),
    (3, "Irish", "Boring", 6.2),
    (4, "Ice song", "Fantasy", 8.6),
    (5, "House Card", "Interesting", 9.1);
-- query to select the movies with an odd-numbered ID and a description that is not "boring"
SELECT *
FROM cinema c
WHERE c.id % 2 <> 0
    AND c.description <> "Boring"
ORDER BY c.rating DESC;
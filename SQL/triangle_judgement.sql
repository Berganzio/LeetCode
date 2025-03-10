-- create triangle table
CREATE TABLE IF NOT EXISTS triangle (x int, y int, z int, PRIMARY KEY (x, y, z));
-- insert data into triangle
INSERT INTO triangle (x, y, z)
values (13, 15, 30);
INSERT INTO triangle (x, y, z)
values (10, 20, 15);
-- query to determine if the given values form a triangle or not
SELECT t.x,
    t.y,
    t.z,
    CASE
        WHEN t.x + t.y > t.z
        AND t.x + t.z > t.y
        AND t.y + t.z > t.x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM triangle t;
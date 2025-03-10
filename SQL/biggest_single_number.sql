-- create mynumbers table
CREATE TABLE IF NOT EXISTS mynumbers (num int);
-- insert data into mynumbers
INSERT INTO mynumbers (num)
values (8),
    (8),
    (3),
    (3),
    (1),
    (4),
    (5),
    (6);
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
-- query to find the largest single number if exists, else return Null
SELECT MAX(s.num) AS num
FROM (
        SELECT n.num
        FROM mynumbers n
        GROUP BY n.num
        HAVING COUNT(n.num) = 1
    ) as s;
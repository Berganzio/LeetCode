-- create actordirector table
CREATE TABLE IF NOT EXISTS actordirector(
    actor_id int,
    director_id int,
    timestamp int unique primary key
);
-- insert data into actordirector
INSERT INTO actordirector(actor_id, director_id, timestamp)
values(1, 1, 0),
(1, 1, 1),
(1, 1, 2),
(1, 2, 3),
(1, 2, 4),
(2, 1, 5),
(2, 1, 6);
-- query to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times
SELECT actor_id, director_id
from actordirector
GROUP BY actor_id, director_id
HAVING count(actor_id) and count(director_id) >= 3;
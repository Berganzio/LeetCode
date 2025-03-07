-- create requestaccepted table
CREATE TABLE
    IF NOT EXISTS requestaccepted (
        requester_id INT,
        accepter_id INT,
        accept_date DATE,
        PRIMARY KEY (requester_id, accepter_id)
    );

-- insert data into requestaccepted
INSERT INTO
    requestaccepted (requester_id, accepter_id, accept_date)
values
    (1, 2, '2021-01-01'),
    (1, 3, '2021-01-02'),
    (2, 3, '2021-01-03'),
    (3, 4, '2021-01-04');

-- insert this data for creating the query which includes more than one Id with the same number of friends
INSERT INTO
    requestaccepted (requester_id, accepter_id, accept_date)
    values
    (1, 4, '2021-01-05');
    
-- query to find the requester ID with the most number of friends and their count, including the requests that have been accepted. Include more than a single Id if there are multiple Ids with the same number of friends.
WITH all_friends AS (
    SELECT requester_id AS id FROM requestaccepted
    UNION ALL
    SELECT accepter_id FROM requestaccepted
),
friend_counts AS (
    SELECT id, COUNT(*) AS num
    FROM all_friends
    GROUP BY id
),
max_count AS (
    SELECT MAX(num) AS max_num
    FROM friend_counts
)
SELECT fc.id, fc.num AS num
FROM friend_counts fc
JOIN max_count mc ON fc.num = mc.max_num;
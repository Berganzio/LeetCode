-- create Scores table
CREATE TABLE IF NOT EXISTS Scores (id INTEGER PRIMARY KEY, score INTEGER NOT NULL);
-- insert data into Scores table
INSERT INTO Scores (id, score)
VALUES (1, 3);
INSERT INTO Scores (id, score)
VALUES (2, 4);
INSERT INTO Scores (id, score)
VALUES (3, 5);
INSERT INTO Scores (id, score)
VALUES (4, 2);
INSERT INTO Scores (id, score)
VALUES (5, 2);
-- using DENSE_RANK() to get the rank of each score. If there are ties, the same rank should be assigned to all scores with equal value
SELECT score,
    DENSE_RANK() OVER (
        ORDER BY score DESC
    ) AS "rank"
FROM Scores
ORDER BY score DESC;
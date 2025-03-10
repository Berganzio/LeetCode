-- create the Person table
CREATE TABLE IF NOT EXISTS Person (Id INT, Email VARCHAR(255));
-- insert data into Person table
INSERT INTO Person (Id, Email)
VALUES (1, 'a@b.com');
INSERT INTO Person (Id, Email)
VALUES (2, 'c@d.com');
INSERT INTO Person (Id, Email)
VALUES (3, 'a@b.com');
-- query to report all duplicate emails, guaranteed not NULL
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1
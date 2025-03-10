-- insert data into the person table
INSERT INTO person (id, email)
VALUES (4, 'john@example.com');
INSERT INTO person (id, email)
VALUES (5, 'bob@example.com');
INSERT INTO person (id, email)
VALUES (6, 'john@example.com');
-- query to delete duplicate emails
DELETE p1
FROM person p1
    JOIN person p2
WHERE p1.id > p2.id
    AND p1.email = p2.email;
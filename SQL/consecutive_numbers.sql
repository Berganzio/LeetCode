-- create Logs table
CREATE TABLE
    IF NOT EXISTS Logs (id INTEGER PRIMARY KEY, num VARCHAR(255) NOT NULL);

-- insert synthetic data into Logs table
INSERT INTO
    Logs (id, num)
VALUES
    (1, '1');
INSERT INTO
    Logs (id, num)
VALUES
    (2, '1');
INSERT INTO
    Logs (id, num)
VALUES
    (3, '1');
INSERT INTO
    Logs (id, num)
VALUES
    (4, '2');
INSERT INTO
    Logs (id, num)
VALUES
    (5, '1');
INSERT INTO
    Logs (id, num)
VALUES
    (6, '2');
INSERT INTO
    Logs (id, num)
VALUES
    (7, '2');

-- query to find the longest consecutive numbers
select DISTINCT
     num as ConsecutiveNums
     FROM (
        SELECT
            num,
            lag(num, 1) over( ORDER BY id) lag1,
            LEAD(num, 1) over(ORDER BY id) lead1
        from logs
    ) as a
    WHERE num = lag1 and num = lead1
    and lag1 = lead1;
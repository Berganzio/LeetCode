-- create weather table
CREATE TABLE
    IF NOT EXISTS weather (
        id INT PRIMARY KEY,
        recordDate date,
        temperature int
    );

-- insert data into table
INSERT INTO
    weather (id, recordDate, temperature)
VALUES
    (1, '2023-10-01', 10);

INSERT INTO
    weather (id, recordDate, temperature)
VALUES
    (2, '2023-10-02', 25);

INSERT INTO
    weather (id, recordDate, temperature)
VALUES
    (3, '2023-10-03', 20);

INSERT INTO
    weather (id, recordDate, temperature)
VALUES
    (4, '2023-10-04', 30);

-- query for finding temperature bigger than the day before, return the date
SELECT DISTINCT
    w.id
from
    weather w
    join weather ww on w.recordDate = DATE_ADD (ww.recordDate, INTERVAL 1 DAY)
    and w.temperature > ww.temperature;
-- create world database
CREATE table
    IF NOT EXISTS world (
        name varchar(255) PRIMARY KEY,
        continent varchar(255),
        area int,
        population int,
        gdp bigint
    );

-- insert data into world
INSERT INTO
    world
VALUES
    (
        'Afghanistan',
        'Asia',
        652230,
        25500100,
        20343000000
    );

INSERT INTO
    world
VALUES
    ('Albania', 'Europe', 28748, 2831741, 12960000000);

INSERT INTO
    world
VALUES
    (
        'Algeria',
        'Africa',
        2381741,
        37100000,
        188681000000
    );

INSERT INTO
    world
VALUES
    ('Andorra', 'Europe', 468, 78115, 3712000000);

INSERT INTO
    world
VALUES
    (
        'Angola',
        'Africa',
        1246700,
        20609294,
        100990000000
    );

-- query to get the name of the largest country in each continent. A BIG country is defined if it has an area of more than 3 million km^2, or it has a population of more than 25 million
SELECT
    name,
    population,
    area
FROM
    world
WHERE
    area >= 3000000
    or population >= 25000000
ORDER BY
    name;
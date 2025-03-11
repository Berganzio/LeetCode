-- create salary table
CREATE TABLE IF NOT EXISTS salary(
    id int primary key,
    name varchar(255),
    sex ENUM('M', 'F'),
    salary int
);
-- insert data into salary
INSERT INTO salary(id, name, sex, salary)
VALUES (1, "A", "M", 2500),
    (2, "B", "F", 1500),
    (3, "C", "M", 5500),
    (4, "D", "F", 500);
-- query to swap all 'f' and 'm' values with a single update statement and no intermediate temporary tables
update salary
set sex = if(sex = 'm', 'f', 'm');
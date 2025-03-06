-- create Employee table in mysql
CREATE TABLE
    Employee (Id INT NOT NULL PRIMARY KEY, Salary INT);

-- insert data into Employee table
INSERT INTO
    Employee (Id, Salary)
VALUES
    ('1', '100');

INSERT INTO
    Employee (Id, Salary)
VALUES
    ('2', '200');

INSERT INTO
    Employee (Id, Salary)
VALUES
    ('3', '300');

-- solution to find the nth highest salary from the Employee table
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary;
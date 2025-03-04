-- create table Employee (id int, salary int);
CREATE TABLE IF NOT EXISTS Employee (
    id INTEGER PRIMARY KEY,
    salary INTEGER NOT NULL
);

-- insert data into Employee table
INSERT INTO Employee (id, salary) VALUES (1, 50000), (2, 60000), (3, 70000);

-- select the second highest salary from Employee table
SELECT DISTINCT max(salary) AS SecondHighestSalary
    FROM Employee
    WHERE salary < ( SELECT MAX( salary) from Employee);
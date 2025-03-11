-- create project table
CREATE TABLE IF NOT EXISTS project(
    project_id int,
    employee_id int,
    primary key(project_id, employee_id)
);
-- create employees table
CREATE TABLE IF NOT EXISTS employees(
    employee_id int primary key,
    name VARCHAR(255),
    experience_years int
);
-- insert data into project
INSERT INTO project(project_id, employee_id)
values (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 4);
-- insert data into employees
INSERT INTO employees(employee_id, name, experience_years)
values(1, 'Khaled', 3),
    (2, 'Ali', 2),
    (3, 'John', 1),
    (4, 'Doe', 2);
-- query to report the average experience years of all the employees for each project, rounded to 2 digits
SELECT p.project_id,
    round(avg(e.experience_years), 2) as average_years
FROM project p
JOIN employees e on e.employee_id = p.employee_id
GROUP BY p.project_id;
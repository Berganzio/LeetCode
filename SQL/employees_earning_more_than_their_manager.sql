-- add rows (name, managerId) to the employee table
ALTER TABLE employee
ADD COLUMN name varchar(255),
    ADD COLUMN managerId int;
-- insert data into employee table
insert into employee (id, salary, managerId, name)
values (4, 2000, null, 'Eric');
-- add name to row 1
update employee
set name = 'John',
    managerId = 4,
    Salary = 30000
where id = 1;
-- add name to row 2
update employee
set name = 'Jane',
    managerId = 3,
    Salary = 20000
where id = 2;
-- add name to row 3
update employee
set name = 'Alice',
    managerId = NULL,
    Salary = 15000
where id = 3;
-- query to find employeeds who earn more than their manager
select e1.name as Employee
from employee e1
    join employee e2 on e1.managerId = e2.id
where e1.salary > e2.salary;
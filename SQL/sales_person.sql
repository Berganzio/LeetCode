-- create salesperson table
CREATE TABLE IF NOT EXISTS salesperson (
    sales_id INT primary key,
    name varchar(255),
    salary int,
    commission_rate int,
    hire_date date
);
-- create company table
CREATE TABLE IF NOT EXISTS company (
    com_id int primary key,
    name varchar(255),
    city varchar(255)
);
-- alter orders table
ALTER TABLE orders
ADD order_id int;
ALTER table orders
ADD order_date date;
ALTER table orders
ADD com_id int;
ALTER table orders
ADD sales_id int;
ALTER table orders
ADD amount int;
-- insert data into salesperson
INSERT INTO salesperson (
        sales_id,
        name,
        salary,
        commission_rate,
        hire_date
    )
values (1, "John", 100000, 6, '2006-04-01'),
    (2, "Amy", 120000, 5, '2010-05-01'),
    (3, "Mark", 65000, 12, '2008-12-25'),
    (4, "Pam", 25000, 25, '2005-01-01'),
    (5, "Alex", 50000, 10, '2007-02-03');
-- insert data into company
INSERT INTO company (com_id, name, city)
values (1, "RED", "Boston"),
    (2, "ORANGE", "New York"),
    (4, "YELLOW", "Boston"),
    (5, "GREEN", "Austin");
-- insert data into orders
INSERT INTO orders (
        id,
        order_id,
        order_date,
        com_id,
        sales_id,
        amount
    )
values (7, 1, "2014-1-1", 3, 4, 10000),
    (8, 2, "2014-1-2", 1, 2, 15000),
    (9, 3, "2014-1-3", 2, 1, 20000),
    (10, 4, "2014-1-4", 4, 3, 25000),
    (11, 5, "2014-1-5", 5, 5, 30000);
-- query to find the names of all the salespersons who did not have any orders related to the company with the name "RED", return the result in any order
SELECT s.name
FROM salesperson s
WHERE s.sales_id NOT IN (
        SELECT o.sales_id
        FROM orders o
            JOIN company c on o.com_id = c.com_id
        WHERE c.name = "RED"
    );
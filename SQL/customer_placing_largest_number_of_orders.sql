-- add columns to orders table
ALTER TABLE orders
ADD order_number INT;
ALTER TABLE orders
ADD customer_number int;
select *
from orders;
-- insert data into new columns
INSERT INTO orders (id, order_number, customer_number)
VALUES (3, 1, 1);
INSERT INTO orders (id, order_number, customer_number)
VALUES (4, 2, 2);
INSERT INTO orders (id, order_number, customer_number)
VALUES (5, 3, 3);
INSERT INTO orders (id, order_number, customer_number)
VALUES (6, 4, 3);
-- query for finding the customer with the highest number of purchases, if nothing found return empty table
SELECT customer_number
FROM (
        SELECT customer_number,
            COUNT(*) AS order_count
        FROM orders
        GROUP BY customer_number
    ) AS sub
ORDER BY order_count DESC
LIMIT 1;
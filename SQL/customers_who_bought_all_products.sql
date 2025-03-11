-- create product table
CREATE TABLE IF NOT EXISTS product(product_key int primary key);
-- create customer table with foreign key from product table
CREATE TABLE IF NOT EXISTS customer(
    customer_id int,
    product_key int,
    FOREIGN KEY (product_key) REFERENCES product(product_key)
);
-- insert data into product
INSERT INTO product(product_key)
values(5),
    (6);
-- insert data into customer
INSERT INTO customer(customer_id, product_key)
values(1, 5),
    (2, 6),
    (3, 5),
    (3, 6),
    (1, 6);
-- query to find the customer ids from the customer table who bought all the products in the product table
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(distinct product_key) = (
        SELECT COUNT(product_key)
        FROM Product
    );
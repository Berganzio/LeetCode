-- create products table
CREATE TABLE IF NOT EXISTS products(
    product_id INT UNIQUE PRIMARY KEY,
    product_name VARCHAR(255)
);
-- create sales table
CREATE TABLE IF NOT EXISTS sales(
    sale_id INT,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    year INT,
    quantity INT,
    price INT,
    PRIMARY KEY(sale_id, year)
);
-- insert data into products
INSERT INTO products (product_id, product_name)
VALUES (100, 'Nokia'),
    (200, 'Apple'),
    (300, 'Samsung');
-- insert data into sales
INSERT INTO sales (sale_id, product_id, year, quantity, price)
VALUES (2, 100, 2008, 10, 5000),
    (2, 100, 2009, 12, 5000),
    (7, 200, 2011, 15, 9000);
-- query to report the product_name, year, price, sale_id in the sales table
SELECT p.product_name,
    s.year,
    s.price
FROM sales s
    join products p ON p.product_id = s.product_id;
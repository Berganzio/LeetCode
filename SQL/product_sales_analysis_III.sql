-- both products and sales tables exists, data filled in already too
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
-- query to select the product_id, year, quantity and price for the first year of every product sold
SELECT s.product_id,
    s.year as first_year,
    s.quantity,
    s.price
FROM sales s
    JOIN (
        SELECT product_id,
            MIN(year) as first_year
        FROM sales
        GROUP BY product_id
    ) first_sales ON s.product_id = first_sales.product_id
    AND s.year = first_sales.first_year;
CREATE DATABASE IF NOT EXISTS sales_management;
USE sales_management;

CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    customer_name VARCHAR(100),
    quantity INT NOT NULL,
    total_amount DECIMAL(10,2),
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Optional sample products. Run these only if you want sample data.
INSERT INTO products (product_name, category, price, stock)
VALUES
    ('Pen', 'Stationery', 10.00, 100),
    ('Notebook', 'Stationery', 50.00, 50),
    ('Water Bottle', 'Accessories', 150.00, 30),
    ('School Bag', 'Bags', 800.00, 20),
    ('Calculator', 'Electronics', 500.00, 15);

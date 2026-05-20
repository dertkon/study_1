CREATE TABLE customers
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(55) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE orders
(
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers (id),
    order_date DATE NOT NULL
);

CREATE TABLE order_items
(
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders (id),
    product_name VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
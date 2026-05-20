INSERT INTO customers (name, email)
VALUES
('Ivan Ivanov', 'ivan@gmail.com'),
('Denis Denisov', 'denis@mail.ru'),
('Anton Antonov', 'antonov@yahoo.com');


INSERT INTO orders (customer_id, order_date)
VALUES
(
    (SELECT id FROM customers WHERE email = 'ivan@gmail.com'),
    '2026-05-19'
),
(
    (SELECT id FROM customers WHERE email = 'denis@mail.ru'),
    '2025-12-31'
),
(
    (SELECT id FROM customers WHERE email = 'denis@mail.ru'),
    '2026-01-01'
),
(
    (SELECT id FROM customers WHERE email = 'antonov@yahoo.com'),
    '2026-03-08'
);


INSERT INTO order_items (order_id, product_name, quantity, price)
VALUES
(
    (
        SELECT orders.id FROM orders
        JOIN customers ON orders.customer_id = customers.id
        WHERE customers.email = 'ivan@gmail.com' AND orders.order_date = '2026-05-19'
    ),
    'iPhone 17 ProMax 256Gb',
    2,
    110000
),
(
    (
        SELECT orders.id
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        WHERE customers.email = 'ivan@gmail.com' AND orders.order_date = '2026-05-19'
    ),
    'AirPods Pro',
    1,
    25000
),
(
    (
        SELECT orders.id FROM orders
        JOIN customers ON orders.customer_id = customers.id
        WHERE customers.email = 'denis@mail.ru' and orders.order_date = '2025-12-31'
    ),
    'xiaomi powerbank 10000mah',
    1,
    1500
),
(
    (
        SELECT orders.id FROM orders
        JOIN customers ON orders.customer_id = customers.id
        WHERE customers.email = 'denis@mail.ru' and orders.order_date = '2026-01-01'
    ),
    'Logitech K380 Bluetooth',
    1,
    5500
),
(
    (
        SELECT orders.id FROM orders
        JOIN customers ON orders.customer_id = customers.id
        WHERE customers.email = 'antonov@yahoo.com' AND orders.order_date = '2026-03-08'
    ),
    'Wireless Mouse',
    1,
    9000
);
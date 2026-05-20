INSERT INTO order_items (order_id, product_name, quantity, price)
SELECT
    floor(random() * 4 + 1)::INTEGER,
    'Product ' || floor(random() * 500 + 1)::INTEGER,
    floor(random() * 10 + 1)::INTEGER,
    floor(random() * 99901 + 100)::DECIMAL(10, 2)
FROM generate_series(1, 1000000);
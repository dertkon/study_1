BEGIN;

INSERT INTO orders (customer_id, order_date)
VALUES
(
    (SELECT id FROM customers WHERE email = 'ivan@gmail.com'),
    CURRENT_DATE
)
RETURNING id

-- Отдал мне айдишник со значением 5

INSERT INTO order_items (order_id, product_name, quantity, price)
VALUES
(5, 'Product 101', 2, 1500),
(5, 'Product 202', 1, 12000),
(5, 'Product 303', 3, 700);

COMMIT;

-- Пробую потестить:
SELECT *
FROM orders
WHERE id = 5;

SELECT *
FROM order_items
WHERE order_id = 5;
-- Все работает


-- Пробую ошибочный сценарий

BEGIN;

INSERT INTO orders (customer_id, order_date)
VALUES
(
    (SELECT id FROM customers WHERE email = 'ivan@gmail.com'),
    CURRENT_DATE
)
RETURNING id

-- Отдал мне айдишник со значением 6

INSERT INTO order_items (order_id, product_name, quantity, price)
VALUES
(6, 'Test Product 1', 5, 500),
(6, NULL, 2, 300),
(6, 'Test product 2', 2, 1000);

-- Ошибку отдает:
-- SQL Error [23502]: ERROR: null value in column "product_name" of relation "order_items" violates not-null constraint
-- Detail: Failing row contains (1000020, 6, null, 2, 300.00).
-- Error position:

-- Откатываюсь
ROLLBACK;


-- Тестинг:
SELECT *
FROM orders
WHERE id = 6;

SELECT *
FROM order_items
WHERE order_id = 6;
-- Таблички пустые — все ок
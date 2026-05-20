SELECT orders.id, orders.order_date
FROM orders
JOIN customers ON customers.id = orders.customer_id
WHERE customers.name = 'Ivan Ivanov';


SELECT oi.product_name, oi.quantity, oi.price
FROM order_items oi
WHERE oi.order_id = 3
ORDER BY oi.price DESC;


SELECT customers.name, SUM(oi.price * oi.quantity) AS total_spent
FROM order_items oi
JOIN orders ON orders.id = oi.order_id
JOIN customers ON customers.id = orders.customer_id
GROUP BY customers.name
HAVING SUM(oi.price * oi.quantity) > 5000;

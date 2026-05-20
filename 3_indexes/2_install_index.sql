CREATE INDEX idx_orders_customer_id
ON orders(customer_id);

CREATE INDEX idx_order_items_order_id_price
ON order_items(order_id, price);

CREATE INDEX idx_order_items_product_name
ON order_items(product_name);
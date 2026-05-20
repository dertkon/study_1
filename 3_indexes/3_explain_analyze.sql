EXPLAIN ANALYZE
SELECT io.order_id, io.price
FROM order_items io
WHERE io.price > 10000 AND io.order_id = 123;

-- Result:
--Index Only Scan using idx_order_items_order_id_price on order_items io  (cost=0.42..8.31 rows=1 width=10) (actual time=0.549..0.549 rows=0 loops=1)
--  Index Cond: ((order_id = 123) AND (price > '10000'::numeric))
--  Heap Fetches: 0
--Planning Time: 3.688 ms
--Execution Time: 0.567 ms



EXPLAIN ANALYZE
SELECT o.id, o.order_date
FROM orders o
WHERE o.customer_id = 1;

-- Result:
--Seq Scan on orders o  (cost=0.00..1.05 rows=1 width=8) (actual time=0.039..0.041 rows=1 loops=1)
--  Filter: (customer_id = 1)
--  Rows Removed by Filter: 3
--Planning Time: 5.969 ms
--Execution Time: 0.063 ms
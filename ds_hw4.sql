
SELECT COUNT(Order_id) AS total_orders
FROM SALES
WHERE Date = '2023-03-18';


SELECT COUNT(SALES.Order_id) AS total_orders_john_doe
FROM SALES
JOIN CUSTOMERS ON SALES.Customer_id = CUSTOMERS.Customer_id
WHERE SALES.Date = '2023-03-18'
  AND CUSTOMERS.first_name = 'John'
  AND CUSTOMERS.last_name = 'Doe';


SELECT COUNT(DISTINCT Customer_id) AS total_customers,
       AVG(Revenue) AS avg_spent_per_customer
FROM SALES
WHERE Date BETWEEN '2023-01-01' AND '2023-01-31';


SELECT department
FROM ITEMS
JOIN SALES ON ITEMS.Item_id = SALES.Item_id
WHERE Date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY department
HAVING SUM(SALES.Revenue) < 600;


SELECT MAX(Revenue) AS max_revenue,
       MIN(Revenue) AS min_revenue
FROM SALES;


WITH Top_Order AS (
    SELECT Order_id, Revenue
    FROM SALES
    ORDER BY Revenue DESC
    LIMIT 1
)

SELECT SALES.Order_id, ITEMS.Item_name, SALES.Quantity, SALES.Revenue
FROM SALES
JOIN ITEMS ON SALES.Item_id = ITEMS.Item_id
WHERE SALES.Order_id = (SELECT Order_id FROM Top_Order);

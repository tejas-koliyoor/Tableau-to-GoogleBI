-- ======================================================
-- Tableau to Google BI Migration Demo
-- KPI Validation Queries
-- ======================================================

-- Purpose:
-- These SQL queries are used to validate whether the KPIs
-- in the migrated Google BI dashboard match the source
-- Tableau-style dashboard logic.

-- Assumption:
-- The sales dataset is available as a table named sales_data.

-- ======================================================
-- 1. Total Revenue
-- ======================================================

SELECT
    SUM(Revenue) AS total_revenue
FROM sales_data;


-- ======================================================
-- 2. Total Profit
-- ======================================================

SELECT
    SUM(Profit) AS total_profit
FROM sales_data;


-- ======================================================
-- 3. Total Orders
-- ======================================================

SELECT
    COUNT(DISTINCT Order_ID) AS total_orders
FROM sales_data;


-- ======================================================
-- 4. Average Order Value
-- Formula: Total Revenue / Total Orders
-- ======================================================

SELECT
    SUM(Revenue) / COUNT(DISTINCT Order_ID) AS average_order_value
FROM sales_data;


-- ======================================================
-- 5. Profit Margin
-- Formula: Total Profit / Total Revenue
-- ======================================================

SELECT
    SUM(Profit) / SUM(Revenue) AS profit_margin
FROM sales_data;


-- ======================================================
-- 6. Revenue by Region
-- ======================================================

SELECT
    Region,
    SUM(Revenue) AS total_revenue
FROM sales_data
GROUP BY Region
ORDER BY total_revenue DESC;


-- ======================================================
-- 7. Revenue by Country
-- ======================================================

SELECT
    Country,
    SUM(Revenue) AS total_revenue
FROM sales_data
GROUP BY Country
ORDER BY total_revenue DESC;


-- ======================================================
-- 8. Revenue by Product Category
-- ======================================================

SELECT
    Product_Category,
    SUM(Revenue) AS total_revenue
FROM sales_data
GROUP BY Product_Category
ORDER BY total_revenue DESC;


-- ======================================================
-- 9. Profit by Sales Channel
-- ======================================================

SELECT
    Sales_Channel,
    SUM(Profit) AS total_profit
FROM sales_data
GROUP BY Sales_Channel
ORDER BY total_profit DESC;


-- ======================================================
-- 10. Revenue by Customer Segment
-- ======================================================

SELECT
    Customer_Segment,
    SUM(Revenue) AS total_revenue
FROM sales_data
GROUP BY Customer_Segment
ORDER BY total_revenue DESC;


-- ======================================================
-- 11. Monthly Revenue Trend
-- Generic SQL version
-- ======================================================

SELECT
    EXTRACT(YEAR FROM Order_Date) AS order_year,
    EXTRACT(MONTH FROM Order_Date) AS order_month,
    SUM(Revenue) AS monthly_revenue
FROM sales_data
GROUP BY
    EXTRACT(YEAR FROM Order_Date),
    EXTRACT(MONTH FROM Order_Date)
ORDER BY
    order_year,
    order_month;


-- ======================================================
-- 12. Google BigQuery Version: Monthly Revenue Trend
-- Use this if the data is loaded into BigQuery
-- ======================================================

SELECT
    DATE_TRUNC(Order_Date, MONTH) AS order_month,
    SUM(Revenue) AS monthly_revenue
FROM sales_data
GROUP BY order_month
ORDER BY order_month;


-- ======================================================
-- 13. Data Quality SQL Check: Duplicate Order IDs
-- ======================================================

SELECT
    Order_ID,
    COUNT(*) AS order_count
FROM sales_data
GROUP BY Order_ID
HAVING COUNT(*) > 1;


-- ======================================================
-- 14. Data Quality SQL Check: Revenue Formula Mismatch
-- Revenue should equal Quantity * Unit_Price
-- ======================================================

SELECT
    Order_ID,
    Quantity,
    Unit_Price,
    Revenue,
    Quantity * Unit_Price AS expected_revenue
FROM sales_data
WHERE Revenue <> Quantity * Unit_Price;


-- ======================================================
-- 15. Data Quality SQL Check: Profit Formula Mismatch
-- Profit should equal Revenue - Cost
-- ======================================================

SELECT
    Order_ID,
    Revenue,
    Cost,
    Profit,
    Revenue - Cost AS expected_profit
FROM sales_data
WHERE ROUND(Profit, 2) <> ROUND(Revenue - Cost, 2);


-- ======================================================
-- 16. Data Quality SQL Check: Missing Critical Values
-- ======================================================

SELECT *
FROM sales_data
WHERE
    Order_ID IS NULL
    OR Order_Date IS NULL
    OR Region IS NULL
    OR Country IS NULL
    OR Product_Category IS NULL
    OR Revenue IS NULL
    OR Profit IS NULL;


-- ======================================================
-- 17. Data Quality SQL Check: Negative Revenue or Quantity
-- ======================================================

SELECT *
FROM sales_data
WHERE
    Revenue < 0
    OR Quantity < 0
    OR Unit_Price < 0;
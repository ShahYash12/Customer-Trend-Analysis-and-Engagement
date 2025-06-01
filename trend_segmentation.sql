-- trend_segmentation.sql

WITH cohort_data AS (
    SELECT 
        customer_id,
        MIN(DATE_TRUNC('month', signup_date)) AS cohort_month,
        DATE_TRUNC('month', last_active_date) AS activity_month
    FROM customer_events
    GROUP BY customer_id, activity_month
)
SELECT 
    cohort_month,
    activity_month,
    COUNT(DISTINCT customer_id) AS active_users
FROM cohort_data
GROUP BY cohort_month, activity_month
ORDER BY cohort_month, activity_month;
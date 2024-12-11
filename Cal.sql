WITH RECURSIVE rolling_lookup AS (
    -- Base case: Start from the current date - 1 (Period 0)
    SELECT 
        DATEADD(DAY, -1, CURRENT_DATE) AS from_date,
        DATEADD(DAY, -30, DATEADD(DAY, -1, CURRENT_DATE)) AS to_date,
        0 AS time_period
    UNION ALL
    -- Recursive case: Add previous 30-day period
    SELECT 
        DATEADD(DAY, -1, to_date) AS from_date,
        DATEADD(DAY, -30, DATEADD(DAY, -1, to_date)) AS to_date,
        time_period - 1
    FROM rolling_lookup
    WHERE DATEADD(DAY, -30, DATEADD(DAY, -1, to_date)) >= DATE_TRUNC('YEAR', CURRENT_DATE)
)
SELECT 
    from_date, 
    to_date, 
    CONCAT('Period ', time_period) AS time_period
FROM rolling_lookup
ORDER BY time_period;  -- Order by time_period for clarity

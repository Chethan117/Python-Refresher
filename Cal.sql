CREATE TEMPORARY TABLE temp_date_ranges AS
WITH RECURSIVE date_ranges AS (
    -- Anchor: Start with the first period (yesterday and 30 days before)
    SELECT 
        DATEADD(DAY, -1, CURRENT_DATE) AS to_date,
        DATEADD(DAY, -31, CURRENT_DATE) AS from_date,
        0 AS period
    UNION ALL
    -- Recursive part: Generate earlier periods until reaching the start of the year
    SELECT 
        DATEADD(DAY, -30, from_date) AS to_date,
        DATEADD(DAY, -30, DATEADD(DAY, -30, from_date)) AS from_date,
        period + 1
    FROM date_ranges
    WHERE DATEADD(DAY, -30, from_date) >= DATE_TRUNC('YEAR', CURRENT_DATE)
)
SELECT 
    period,
    from_date,
    to_date
FROM date_ranges
ORDER BY period;
Non-Execution Impact:
Failure to remove vulnerable accounts from the SCA bypass list exposes the system to increased fraud risks, leading to potential financial losses, regulatory non-compliance, and reputational damage.

Why Critical:
It ensures secure transactions, protects customer data, and aligns with compliance standards, minimizing risks associated with unauthorized access

CREATE OR REPLACE TABLE TABLE_1 AS
WITH CTE_C AS (
    SELECT A.* 
    FROM tablea A
    GROUP BY A.DT
)
SELECT 
    A.*, 
    B.*, 
    C.*
FROM tablea A
LEFT JOIN TABLEB B
    ON /* specify your join condition between A and B here */
LEFT JOIN CTE_C C
    ON A.DT = C.DT
WHERE 
    (
        CASE 
            WHEN DATE_PART('WEEKDAY', CURRENT_DATE()) = 2 
            THEN (A.DT >= CURRENT_DATE() - INTERVAL '3 DAY' AND A.DT < CURRENT_DATE())
            ELSE (A.DT = CURRENT_DATE() - INTERVAL '1 DAY')
        END
    )
    OR (A.REDT IS NULL AND A.REQDT IS NULL)
HAVING SOME_IND = 0 OR SAMEB_IND = 0
ORDER BY 1, 2, 3;

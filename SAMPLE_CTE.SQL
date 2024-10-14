  (EXTRACT(DAYOFWEEK FROM CURRENT_DATE) = 2 
        AND a.dt >= DATEADD(day, -3, CURRENT_DATE) 
        AND a.dt < CURRENT_DATE)  -- If today is Monday, check if dt is in the last 3 days
    OR 
    (EXTRACT(DAYOFWEEK FROM CURRENT_DATE) != 2 
        AND a.dt = DATEADD(day, -1, CURRENT_DATE))  -- If not Monday, check if dt is yesterday

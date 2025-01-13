WITH monthly_base AS (
    SELECT
          'MONTHLY_CHECK'                           AS check_type
        , a.account_id                              AS approved_account_id
        , a.card_number                             AS approved_card_number
        , a.authorisation_request_process_date      AS approved_date
        , a.authorization_amount                    AS approved_amount
        , a.merchant_id                             AS approved_merchant_id
        , a.merchant_name                           AS approved_merchant_name
        
        , b.authorisation_request_process_date      AS blocked_date
        , b.authorization_amount                    AS blocked_amount
        , b.merchant_id                             AS blocked_merchant_id
        , b.merchant_name                           AS blocked_merchant_name
        
    FROM authzn a
    INNER JOIN authzn b
        ON  a.account_id  = b.account_id
        AND a.card_number = b.card_number
        -- Approx. 27–32 days later
        AND a.authorisation_request_process_date BETWEEN 
              DATEADD(day, 27, b.authorisation_request_process_date)
          AND DATEADD(day, 32, b.authorisation_request_process_date)
    WHERE
        -- a is APPROVED
        a.authorization_response_code IN (1,2,3)
        AND a.pos_entry_mthd_cd IN (01,10,81)
        
        -- b is BLOCKED (declined, referred, pickup, or scheme reason)
        AND (
               b.authorization_response_code NOT IN (1,2,3)
            OR b.switch_reason_code IN ('9201','0041')
        )
        AND b.pos_entry_mthd_cd IN (01,10,81)
        
        -- Merchant changed
        AND (
            a.merchant_id <> b.merchant_id
            OR a.merchant_name <> b.merchant_name
        )
        
        -- Exclude PayPal
        AND a.merchant_name NOT ILIKE '%PAYPAL%'
        AND b.merchant_name NOT ILIKE '%PAYPAL%'
),

annual_base AS (
    SELECT
          'ANNUAL_CHECK'                            AS check_type
        , a.account_id                              AS approved_account_id
        , a.card_number                             AS approved_card_number
        , a.authorisation_request_process_date      AS approved_date
        , a.authorization_amount                    AS approved_amount
        , a.merchant_id                             AS approved_merchant_id
        , a.merchant_name                           AS approved_merchant_name
        
        , b.authorisation_request_process_date      AS blocked_date
        , b.authorization_amount                    AS blocked_amount
        , b.merchant_id                             AS blocked_merchant_id
        , b.merchant_name                           AS blocked_merchant_name
        
    FROM authzn a
    INNER JOIN authzn b
        ON  a.account_id  = b.account_id
        AND a.card_number = b.card_number
        -- Approx. 12–13 months later
        AND a.authorisation_request_process_date BETWEEN
              DATEADD(month, 12, b.authorisation_request_process_date)
          AND DATEADD(month, 13, b.authorisation_request_process_date)
    WHERE
        -- a is APPROVED
        a.authorization_response_code IN (1,2,3)
        AND a.pos_entry_mthd_cd IN (01,10,81)
        
        -- b is BLOCKED (declined, referred, pickup, or scheme reason)
        AND (
               b.authorization_response_code NOT IN (1,2,3)
            OR b.switch_reason_code IN ('9201','0041')
        )
        AND b.pos_entry_mthd_cd IN (01,10,81)
        
        -- Merchant changed
        AND (
            a.merchant_id <> b.merchant_id
            OR a.merchant_name <> b.merchant_name
        )
        
        -- Exclude PayPal
        AND a.merchant_name NOT ILIKE '%PAYPAL%'
        AND b.merchant_name NOT ILIKE '%PAYPAL%'
)

SELECT *
FROM monthly_base
UNION ALL
SELECT *
FROM annual_base
ORDER BY 
     check_type
   , approved_account_id
   , approved_card_number
   , blocked_date
   , approved_date;

WITH monthly_base AS (
    SELECT
          'MONTHLY_CHECK'                                            AS check_type
        -- Blocked details first
        , b.account_id                                              AS blocked_account_id
        , b.card_number                                             AS blocked_card_number
        , b.authorisation_request_process_date                      AS blocked_date
        , b.authorization_amount                                    AS blocked_amount
        , b.merchant_id                                             AS blocked_merchant_id
        , b.merchant_name                                           AS blocked_merchant_name
        , b.acquiring_bank_identification_number                    AS blocked_acq_bin
        , b.merchant_category_code                                  AS blocked_mcc
        
        -- Approved details next
        , a.authorisation_request_process_date                      AS approved_date
        , a.authorization_amount                                    AS approved_amount
        , a.merchant_id                                             AS approved_merchant_id
        , a.merchant_name                                           AS approved_merchant_name
        , a.acquiring_bank_identification_number                    AS approved_acq_bin
        , a.merchant_category_code                                  AS approved_mcc

    FROM authzn b
    INNER JOIN authzn a
        ON  b.account_id  = a.account_id
        AND b.card_number = a.card_number
        
        -- Example: Looking 27–32 days later for monthly
        AND a.authorisation_request_process_date BETWEEN 
              DATEADD(day, 27, b.authorisation_request_process_date)
          AND DATEADD(day, 32, b.authorisation_request_process_date)

    WHERE
        -- b is BLOCKED (Declined, Referred, Pickup, or scheme reason)
        (
           b.authorization_response_code NOT IN (1,2,3)
           OR b.switch_reason_code IN ('9201','0041')
        )
        AND b.pos_entry_mthd_cd IN (01,10,81)  -- CNP

        -- a is APPROVED
        AND a.authorization_response_code IN (1,2,3)
        AND a.pos_entry_mthd_cd IN (01,10,81)  -- CNP

        -- Merchant changed
        AND (
            b.merchant_id   <> a.merchant_id
            OR b.merchant_name <> a.merchant_name
        )
        
        -- Exclude PayPal (optional)
        AND b.merchant_name NOT ILIKE '%PAYPAL%'
        AND a.merchant_name NOT ILIKE '%PAYPAL%'
),

annual_base AS (
    SELECT
          'ANNUAL_CHECK'                                             AS check_type
        -- Blocked details first
        , b.account_id                                              AS blocked_account_id
        , b.card_number                                             AS blocked_card_number
        , b.authorisation_request_process_date                      AS blocked_date
        , b.authorization_amount                                    AS blocked_amount
        , b.merchant_id                                             AS blocked_merchant_id
        , b.merchant_name                                           AS blocked_merchant_name
        , b.acquiring_bank_identification_number                    AS blocked_acq_bin
        , b.merchant_category_code                                  AS blocked_mcc
        
        -- Approved details next
        , a.authorisation_request_process_date                      AS approved_date
        , a.authorization_amount                                    AS approved_amount
        , a.merchant_id                                             AS approved_merchant_id
        , a.merchant_name                                           AS approved_merchant_name
        , a.acquiring_bank_identification_number                    AS approved_acq_bin
        , a.merchant_category_code                                  AS approved_mcc

    FROM authzn b
    INNER JOIN authzn a
        ON  b.account_id  = a.account_id
        AND b.card_number = a.card_number

        -- Example: Looking 12–13 months later for annual
        AND a.authorisation_request_process_date BETWEEN
              DATEADD(month, 12, b.authorisation_request_process_date)
          AND DATEADD(month, 13, b.authorisation_request_process_date)

    WHERE
        -- b is BLOCKED
        (
           b.authorization_response_code NOT IN (1,2,3)
           OR b.switch_reason_code IN ('9201','0041')
        )
        AND b.pos_entry_mthd_cd IN (01,10,81)  -- CNP

        -- a is APPROVED
        AND a.authorization_response_code IN (1,2,3)
        AND a.pos_entry_mthd_cd IN (01,10,81)  -- CNP

        -- Merchant changed
        AND (
            b.merchant_id   <> a.merchant_id
            OR b.merchant_name <> a.merchant_name
        )
        
        -- Exclude PayPal
        AND b.merchant_name NOT ILIKE '%PAYPAL%'
        AND a.merchant_name NOT ILIKE '%PAYPAL%'
)

-- Combine monthly and annual results
SELECT *
FROM monthly_base
UNION ALL
SELECT *
FROM annual_base
ORDER BY
    check_type,
    blocked_account_id,
    blocked_card_number,
    blocked_date,
    approved_date;

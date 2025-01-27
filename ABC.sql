WITH distinct_transactions AS (
    SELECT
        b.account_id,
        b.card_number,
        b.merchant_id AS blocked_merchant_id,
        a.merchant_id AS approved_merchant_id,
        b.authorization_amount AS blocked_amount,
        a.authorization_amount AS approved_amount,
        b.authorization_response_code AS blocked_response_code,
        a.authorization_response_code AS approved_response_code,
        b.acquiring_bank_identification_number AS blocked_acq_bin,
        a.acquiring_bank_identification_number AS approved_acq_bin,
        b.merchant_category_code AS blocked_mcc,
        a.merchant_category_code AS approved_mcc,
        b.merchant_name AS blocked_merchant_name,
        a.merchant_name AS approved_merchant_name,
        b.authorisation_request_process_date AS blocked_date,
        a.authorisation_request_process_date AS approved_date
    FROM authzn b
    INNER JOIN authzn a
        ON b.account_id = a.account_id
        AND b.card_number = a.card_number
        AND a.authorisation_request_process_date BETWEEN DATEADD(day, 27, b.authorisation_request_process_date)
                                                   AND DATEADD(day, 32, b.authorisation_request_process_date)
    WHERE
        -- Filter conditions for blocked and approved transactions
        b.authorization_response_code NOT IN (1,2,3)  -- Blocked
        AND a.authorization_response_code IN (1,2,3)   -- Approved
        AND b.pos_entry_mthd_cd IN (01,10,81)  -- CNP
        AND a.pos_entry_mthd_cd IN (01,10,81)  -- CNP
        AND b.switch_reason_code IN ('9201','0041') 
        AND b.authzn = 0210
        AND a.authzn = 0100
        AND a.authzn_amt >= 0.9 * b.authzn_amt
        AND a.authzn_amt <= 1.1 * b.authzn_amt
        AND UPPER(TRIM(b.merchant_name)) = UPPER(TRIM(b.merchant_name))
        -- Exclude PayPal (optional)
        AND b.merchant_name NOT ILIKE '%PAYPAL%'
        AND a.merchant_name NOT ILIKE '%PAYPAL%'
)
SELECT
    account_id,
    card_number,
    
    -- Track total blocked and approved amounts for the customer
    SUM(blocked_amount) AS total_blocked_amount,
    SUM(approved_amount) AS total_approved_amount,
    
    -- Count the number of declined and approved transactions per unique merchant
    COUNT(DISTINCT blocked_merchant_id) AS unique_blocked_merchants,
    COUNT(DISTINCT approved_merchant_id) AS unique_approved_merchants,
    
    -- Concatenate unique blocked merchant IDs using LISTAGG
    LISTAGG(DISTINCT blocked_merchant_id, ',') WITHIN GROUP (ORDER BY blocked_merchant_id) AS blocked_merchant_ids,
    
    -- Concatenate unique approved merchant IDs using LISTAGG
    LISTAGG(DISTINCT approved_merchant_id, ',') WITHIN GROUP (ORDER BY approved_merchant_id) AS approved_merchant_ids,
    
    -- Count the number of blocked and approved transactions for each unique merchant
    COUNT(CASE WHEN blocked_response_code NOT IN (1,2,3) THEN 1 END) AS blocked_transactions_count,
    COUNT(CASE WHEN approved_response_code IN (1,2,3) THEN 1 END) AS approved_transactions_count,
    
    -- Include the merchant details for blocked and approved transactions
    LISTAGG(DISTINCT blocked_mcc, ',') WITHIN GROUP (ORDER BY blocked_mcc) AS blocked_mccs,
    LISTAGG(DISTINCT approved_mcc, ',') WITHIN GROUP (ORDER BY approved_mcc) AS approved_mccs,
    LISTAGG(DISTINCT blocked_acq_bin, ',') WITHIN GROUP (ORDER BY blocked_acq_bin) AS blocked_acq_bins,
    LISTAGG(DISTINCT approved_acq_bin, ',') WITHIN GROUP (ORDER BY approved_acq_bin) AS approved_acq_bins,
    LISTAGG(DISTINCT blocked_merchant_name, ',') WITHIN GROUP (ORDER BY blocked_merchant_name) AS blocked_merchant_names,
    LISTAGG(DISTINCT approved_merchant_name, ',') WITHIN GROUP (ORDER BY approved_merchant_name) AS approved_merchant_names,
    
    -- Include the earliest blocked and approved dates (you can also use MAX() depending on your requirements)
    MIN(blocked_date) AS earliest_blocked_date,
    MAX(approved_date) AS latest_approved_date
    
FROM distinct_transactions
GROUP BY account_id, card_number;

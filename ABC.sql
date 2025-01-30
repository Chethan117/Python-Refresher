-- Step 1: Create temporary table for the most recent blocked (declined) transaction
CREATE TEMPORARY TABLE last_decline AS
SELECT 
    b.account_id,
    b.card_number,
    b.merchant_name,
    b.authorization_amount AS blocked_amount,
    b.authorisation_request_process_date AS blocked_date
FROM authzn b
WHERE b.authorization_response_code NOT IN (1, 2, 3)  -- Blocked transactions
    AND b.pos_entry_mthd_cd IN (01, 10, 81)  -- CNP
    AND b.switch_reason_code IN ('9201', '0041') 
    AND b.authzn = 0210
    -- Get the most recent decline for each customer, account, and merchant
    AND b.authorisation_request_process_date = (
        SELECT MAX(b2.authorisation_request_process_date)
        FROM authzn b2
        WHERE b2.account_id = b.account_id
        AND b2.card_number = b.card_number
        AND b2.merchant_name = b.merchant_name
        AND b2.authorization_response_code NOT IN (1, 2, 3)  -- Blocked
    );

-- Step 2: Create temporary table for the most recent approved transaction
CREATE TEMPORARY TABLE recent_approval AS
SELECT 
    a.account_id,
    a.card_number,
    a.merchant_name,
    a.authorization_amount AS approved_amount,
    a.authorisation_request_process_date AS approved_date
FROM authzn a
WHERE a.authorization_response_code IN (1, 2, 3)  -- Approved transactions
    AND a.pos_entry_mthd_cd IN (01, 10, 81)  -- CNP
    AND a.authzn = 0100
    -- Get the most recent approval for each customer, account, and merchant
    AND a.authorisation_request_process_date = (
        SELECT MAX(a2.authorisation_request_process_date)
        FROM authzn a2
        WHERE a2.account_id = a.account_id
        AND a2.card_number = a.card_number
        AND a2.merchant_name = a.merchant_name
        AND a2.authorization_response_code IN (1, 2, 3)  -- Approved
    );

-- Step 3: Create temporary table to calculate the date difference between last decline and recent approval
CREATE TEMPORARY TABLE date_difference AS
SELECT 
    ld.account_id,
    ld.card_number,
    ld.merchant_name,
    ld.blocked_date,
    ra.approved_date,
    DATEDIFF(day, ld.blocked_date, ra.approved_date) AS days_diff
FROM last_decline ld
INNER JOIN recent_approval ra
    ON ld.account_id = ra.account_id
    AND ld.card_number = ra.card_number
    AND ld.merchant_name = ra.merchant_name;

-- Step 4: Final select to flag Monthly or Annual CPAs based on the date difference
SELECT 
    account_id,
    card_number,
    merchant_name,
    blocked_date,
    approved_date,
    days_diff,
    CASE
        WHEN days_diff < 330 THEN 'Monthly CPA'  -- If the date difference is less than 330 days, it's a monthly CPA
        ELSE 'Annual CPA'  -- If the date difference is 330 days or more, it's an annual CPA
    END AS cpa_type
FROM date_difference;

-- Cleanup: Drop temporary tables after use
DROP TEMPORARY TABLE last_decline;
DROP TEMPORARY TABLE recent_approval;
DROP TEMPORARY TABLE date_difference;

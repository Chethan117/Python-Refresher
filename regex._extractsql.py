MDES Token Deletion Process
This document provides a simple explanation of the MDES Token Deletion process, including its purpose, goals, and steps.

Background (Why this process is needed)
Fraudulent activity involving MasterCard Digital Enablement Service (MDES) tokens can impact customers and the business. This process helps identify and remove tokens associated with confirmed fraud cases. By removing these tokens, we can prevent further misuse and secure accounts effectively.

Intent (What this process does)
The goal of this process is to:

Identify fraud accounts where MDES transactions have been confirmed as fraudulent.
Gather all related account details, transactions, and fraud indicators.
Push this information into a workstream for agents to review and take action (e.g., token deletion).
Method (How this process works)
This process involves the following steps:

Identify Blocked Accounts:

Fetch all accounts that are currently blocked due to a security fraud status code.
Filter by Recent Blocks:

From the accounts found in Step 1, only include those blocked in the last 3 months.
Locate Token Transactions:

Find accounts where a token was added within the last 90 days.
Check Merchant Requests:

Look for transactions in the last 90 days where the merchant made a request and completed the transaction rather than directly authorizing it.
Exclude Accounts with Token Deletion:

Remove any cases where a token was already deleted after the fraud was reported on the account.
Join with CardGuard:

Match the accounts with the CardGuard system to retrieve additional fraud indicators.
Fetch Final MDES Fraud Output:

Extract the final list of fraud accounts where MDES tokens were added.
Push to Workstream:

Send this output to the workstream for agents to review and process.
Key Notes
MDES tokens are unique digital identifiers linked to a customer's card, used for secure transactions.
This process ensures tokens associated with fraudulent activity are removed promptly, safeguarding customers and preventing further fraud.
The workstream allows agents to review and act on flagged accounts systematically.
By following this method, we ensure robust fraud detection and prevention measures are in place for MDES transactions.







Non-Execution Impact
If the MDES Token Deletion Process is not executed, the following risks and impacts may occur:

1. Increased Fraud Exposure
Fraudulent tokens will remain active, allowing malicious actors to continue unauthorized transactions.
This could lead to financial losses for both customers and the business.


Background and Intent
The task involves checking for transactions and events related to countries that are either sanctioned or high-risk, based on compliance rules. Financial institutions are required to monitor such transactions to comply with global sanctions regulations, prevent money laundering, and ensure that no prohibited parties are involved in financial activities. Monitoring transactions, events, and associated details such as authorization requests helps ensure that the company adheres to regulations and identifies any breach promptly. These checks and balances mitigate risks associated with high-risk countries and protect the institution from penalties.

The intent here is to:

Identify Transactions Linked to Embargoed or High-Risk Countries: Detect any transactions that involve customers or accounts associated with embargoed countries.
Ensure Correct Authorization Handling: Make sure that transactions where the authorization amount exceeds or falls short of the available balance are being handled properly (approved/declined), based on compliance thresholds.
Track Sanctioned Country Transactions: Ensure that any transactions tied to sanctioned countries are correctly flagged, approved, or declined.
Set KPIs Based on Compliance Metrics: Generate a set of compliance KPIs to assess how well the process handles authorization, approvals, declines, and transactions with embargoed and sanctioned countries.
What to Check
Embargo Country Transactions: Check for any posted transactions in the last three days that match the embargo country list, including the event details (card number, account number, customer ID, agent, and screen where the event was initiated).
Authorization Requests: Compare the authorization amount with the available balance for the last three days. Identify when:
Transactions are approved when the authorization amount exceeds the available balance (flag as a breach).
Transactions are declined when the authorization amount is lower than the available balance (flag as a breach).
Risk Country Lookup: Join the event data with the risk country lookup table and the embargo country lookup to flag any sanctions.
Compliance Metrics: Aggregate the following:
Wrong approvals and wrong declines (based on compliance thresholds).
Risk-adjusted volume of declined and approved transactions for sanctioned countries.
Sanctioned countries' approvals and declines based on defined volume thresholds.
Final Compliance KPIs: Combine all tables to build a set of compliance KPIs with metrics related to approval, decline, sanctions, and embargo country volume, using a threshold-based risk-adjusted grading (RAG) system.
Method: How to Execute
Identify Transactions with Embargo Countries:

Query the posted transactions for the last three days and compare the country code to the embargo country list.
Join with the event table to capture the associated details (card number, account number, etc.).
Use ISO country codes to determine if the address or transaction country is in the embargo list.
Authorization Requests and Approvals:

For transactions where the authorization amount exceeds the available balance but are still approved, flag them as a breach.
For transactions where the authorization amount is below the available balance but are declined, flag them as a breach.
Use an inner join with the lookup tables for risk countries and a left join with embargo country lookup to identify sanctioned countries and flag them.
Set RAG Status for Approvals and Declines:

Define thresholds for approvals and declines:
If approved volume > 10 transactions, mark as "Red" (high risk); otherwise, "Green" (low risk).
If declined volume > 1, mark as "Red"; otherwise, "Green."
Check both approvals and declines for sanctioned countries and flag based on the volume.
Create a Compliance KPI Table:

Union the above checks (approval, decline, sanctions) into a single table to create a comprehensive compliance KPI table.
Ensure the table includes columns for the authorization request process date, metric name, metric value, threshold, and the RAG (Red/Amber/Green) status based on the thresholds.
Include sanctioned countries' PIN and plastic volume check for the last two days.

Background and Intent
Fraud detection and prevention are critical components of risk management for any financial institution or company handling sensitive customer data. Fraudulent activities, especially those related to financial transactions, often involve customer interactions via inbound and outbound calls. Monitoring these calls can provide insights into potential fraud risks, help identify patterns, and improve the overall fraud prevention strategy.

The intent of this task is to extract inbound and outbound fraud-related calls from the last seven days, consolidate the data into a structured datamart, and store the resulting dataset in a repository for further analysis or reporting. This will help the fraud management team monitor and investigate potentially fraudulent interactions, enabling them to react more quickly and efficiently to suspicious activities.

What to Check
Inbound and Outbound Fraud Calls: Identify and extract the calls flagged as fraud-related from the base AWS table, specifically for inbound and outbound call types. This should include customer interactions where:

Fraudulent activity was reported or suspected by the customer.
The agent flagged the call as suspicious based on internal protocols.
Follow-ups on fraud-related activities initiated by the company (outbound calls).
Time Frame: Focus on calls made within the last 7 days to ensure the data is current and relevant for ongoing investigations.

Key Data Points: Capture critical information, such as:

Call type (inbound or outbound)
Customer ID
Call timestamp
Agent details
Fraud type (if available)
Call status (whether the case was escalated, resolved, or pending)
Method: How to Execute
Extract Data from AWS Base Table:

Query the base table in AWS that contains call records, filtering for the last 7 days and ensuring that only fraud-related calls (both inbound and outbound) are included in the extraction.
Use attributes such as call_type, fraud_flag, call_timestamp, customer_id, and agent_id to capture the necessary data.
Perform a time window filter to ensure only calls within the last 7 days are considered.
Example SQL query:

sql
Copy code
SELECT call_type, customer_id, agent_id, call_timestamp, fraud_flag, fraud_type
FROM aws_base_table
WHERE fraud_flag = 'TRUE' 
AND call_timestamp BETWEEN CURRENT_DATE - INTERVAL '7' DAY AND CURRENT_DATE
Transform Data into a Datamart:

Create a datamart (a subset of the data warehouse that is specific to fraud monitoring). The datamart should contain relevant, cleaned, and well-structured data to be used for fraud analysis.
Perform necessary data cleaning, such as removing duplicates, formatting timestamps, and adding derived columns (e.g., calculating the duration of the call or flagging critical cases).
Store in a Repository Dataset:

Once the datamart is built, store the cleaned data in a designated repository dataset. This could be in a cloud data warehouse or on-premises storage, depending on the organization's infrastructure.
Ensure the dataset is well-indexed and tagged for easy retrieval and further analysis by the fraud investigation team.
Automation and Scheduling:

Schedule this process to run on a regular basis (daily or weekly) to keep the datamart updated with the most recent fraud call data.
Set up notifications or alerts for the fraud management team if any anomalies or large volumes of fraud calls are detected.

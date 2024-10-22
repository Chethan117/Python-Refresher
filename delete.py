Background:
In fraud detection, it is critical to identify and monitor charge-off and non-charge-off transactions in inbound app fraud. Charge-offs represent financial losses that cannot be collected, while non-charge-offs reflect recoverable amounts or disputes under investigation. By separating these two categories, the company can better assess risk exposure and potential recovery strategies. This daily monitoring system will improve fraud risk management, streamline reporting, and enhance decision-making.

Intent:
The goal of this initiative is to develop a system that monitors app fraud inbound data, splitting it into charge-off and non-charge-off transactions. This process enables daily reporting and generates a datamart that stores relevant fraud insights, empowering stakeholders with timely data for operational and strategic decisions.

Method:
Data Collection:

Extract inbound fraud data from relevant sources (e.g., app logs, fraud detection systems, or databases).
Ensure data includes information on whether transactions have been marked as charge-off or non-charge-off.
Data Processing:

Apply necessary business rules to classify each transaction as either charge-off or non-charge-off.
Use SQL queries or Python scripts to transform and clean the data.
Data Storage:

Store processed data in a datamart, ensuring proper structuring for easy access and reporting.
Datamart will be designed for optimal retrieval of charge-off and non-charge-off transactions.
Daily Monitoring:

Automate the daily extraction and processing of inbound fraud data.
Create dashboards and daily reports in Tableau or Power BI to visualize the split between charge-off and non-charge-off transactions.
Implement alerts for anomalies or significant changes in transaction patterns.
Reporting:

Generate daily reports for fraud risk analysts and stakeholders.
Highlight trends, potential issues, and recovery opportunities based on the split data.
